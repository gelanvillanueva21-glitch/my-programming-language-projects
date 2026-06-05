"""
AI ASSISTANT - Powered by Claude
Can do anything: code, write, translate, solve math, debug, brainstorm, and more.

Requirements:
    pip install anthropic

Usage:
    python ai_assistant.py
    python ai_assistant.py --key YOUR_API_KEY
"""

import os
import sys
import argparse
import textwrap

try:
    import anthropic
except ImportError:
    print("Missing dependency. Run: pip install anthropic")
    sys.exit(1)


# ── Config ────────────────────────────────────────────────────────────────────

SYSTEM_PROMPT = """You are an all-purpose AI assistant. You can do anything:
- Write, debug, and explain code in any programming language
- Solve math problems step by step
- Write stories, essays, emails, and creative content
- Translate text to any language
- Explain complex topics simply
- Brainstorm ideas and give recommendations
- Analyze data and summarize information
- Answer any question on any topic

Be helpful, clear, and concise. Format code in markdown code blocks."""

MODEL = "claude-opus-4-5"
MAX_TOKENS = 4096
HISTORY_LIMIT = 40  # max messages to keep in memory


# ── Colors ────────────────────────────────────────────────────────────────────

class C:
    RESET  = "\033[0m"
    BOLD   = "\033[1m"
    DIM    = "\033[2m"
    CYAN   = "\033[96m"
    GREEN  = "\033[92m"
    YELLOW = "\033[93m"
    RED    = "\033[91m"
    BLUE   = "\033[94m"
    MAGENTA= "\033[95m"
    WHITE  = "\033[97m"

def supports_color():
    return hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()

USE_COLOR = supports_color()

def c(color, text):
    return f"{color}{text}{C.RESET}" if USE_COLOR else text


# ── Formatting ────────────────────────────────────────────────────────────────

def print_banner():
    banner = f"""
{c(C.CYAN, '╔══════════════════════════════════════════════════╗')}
{c(C.CYAN, '║')}  {c(C.BOLD + C.WHITE, '🤖  AI ASSISTANT  —  Powered by Claude')}          {c(C.CYAN, '║')}
{c(C.CYAN, '║')}  {c(C.DIM, 'Code · Write · Translate · Math · Anything')}      {c(C.CYAN, '║')}
{c(C.CYAN, '╚══════════════════════════════════════════════════╝')}
"""
    print(banner)

def print_help():
    help_text = f"""
{c(C.BOLD, 'Commands:')}
  {c(C.YELLOW, '/help')}       Show this help message
  {c(C.YELLOW, '/clear')}      Clear conversation history
  {c(C.YELLOW, '/history')}    Show conversation history
  {c(C.YELLOW, '/save')}       Save conversation to a file
  {c(C.YELLOW, '/mode')}       Switch mode (chat / code / creative / translate)
  {c(C.YELLOW, '/quit')}       Exit the assistant

{c(C.BOLD, 'Quick prompts:')}
  {c(C.DIM, 'Type anything — the AI handles it automatically.')}
  {c(C.DIM, 'Examples:')}
    {c(C.DIM, '• Write a Python web scraper')}
    {c(C.DIM, '• Explain quantum computing simply')}
    {c(C.DIM, '• Translate "hello world" to Spanish, French, Japanese')}
    {c(C.DIM, '• Solve: 3x² - 12 = 0')}
    {c(C.DIM, '• Write a horror story opening')}
    {c(C.DIM, '• Debug this: for i in range(10) print(i)')}

{c(C.BOLD, 'Multi-line input:')}
  {c(C.DIM, 'End your message with \\ to continue on the next line.')}
  {c(C.DIM, 'Or paste multi-line content — it will be handled correctly.')}
"""
    print(help_text)

def print_separator():
    width = min(os.get_terminal_size().columns, 60) if hasattr(os, 'get_terminal_size') else 60
    print(c(C.DIM, '─' * width))

def wrap_text(text, width=80, indent="  "):
    lines = text.split('\n')
    result = []
    in_code_block = False
    for line in lines:
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            result.append(c(C.MAGENTA, line))
        elif in_code_block:
            result.append(c(C.GREEN, line))
        else:
            if len(line) > width:
                wrapped = textwrap.fill(line, width=width, subsequent_indent=indent)
                result.append(wrapped)
            else:
                result.append(line)
    return '\n'.join(result)


# ── Modes ─────────────────────────────────────────────────────────────────────

MODES = {
    "chat": {
        "label": "General Chat",
        "system": SYSTEM_PROMPT,
        "color": C.CYAN,
    },
    "code": {
        "label": "Code Expert",
        "system": SYSTEM_PROMPT + "\n\nFocus on providing clean, well-commented code with explanations. Always include usage examples.",
        "color": C.GREEN,
    },
    "creative": {
        "label": "Creative Writer",
        "system": SYSTEM_PROMPT + "\n\nFocus on vivid, engaging creative writing. Use rich descriptions, strong characters, and compelling narratives.",
        "color": C.MAGENTA,
    },
    "translate": {
        "label": "Translator",
        "system": SYSTEM_PROMPT + "\n\nWhen translating, provide the translation clearly, note any nuances, and give pronunciation hints if helpful.",
        "color": C.YELLOW,
    },
}

current_mode = "chat"


# ── Core AI ───────────────────────────────────────────────────────────────────

def chat(client, history, user_message, mode="chat"):
    history.append({"role": "user", "content": user_message})

    # Trim history if too long
    if len(history) > HISTORY_LIMIT:
        history = history[-HISTORY_LIMIT:]

    try:
        response = client.messages.create(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            system=MODES[mode]["system"],
            messages=history,
        )
        reply = response.content[0].text
        history.append({"role": "assistant", "content": reply})
        return reply, history

    except anthropic.AuthenticationError:
        raise Exception("Invalid API key. Check your key and try again.")
    except anthropic.RateLimitError:
        raise Exception("Rate limit hit. Please wait a moment and try again.")
    except anthropic.APIConnectionError:
        raise Exception("Connection error. Check your internet connection.")
    except Exception as e:
        raise Exception(f"API error: {e}")


# ── Commands ──────────────────────────────────────────────────────────────────

def save_conversation(history):
    if not history:
        print(c(C.YELLOW, "  Nothing to save yet."))
        return
    filename = "conversation.txt"
    with open(filename, "w", encoding="utf-8") as f:
        for msg in history:
            role = "You" if msg["role"] == "user" else "AI"
            f.write(f"[{role}]\n{msg['content']}\n\n{'─'*60}\n\n")
    print(c(C.GREEN, f"  Saved to {filename}"))

def show_history(history):
    if not history:
        print(c(C.YELLOW, "  No conversation history yet."))
        return
    print()
    for i, msg in enumerate(history):
        role_label = c(C.CYAN, "You") if msg["role"] == "user" else c(C.GREEN, "AI")
        content_preview = msg["content"][:120].replace('\n', ' ')
        if len(msg["content"]) > 120:
            content_preview += "..."
        print(f"  {i+1}. {role_label}: {content_preview}")
    print()

def switch_mode():
    global current_mode
    print(f"\n  {c(C.BOLD, 'Available modes:')}")
    for key, val in MODES.items():
        marker = " ◀ current" if key == current_mode else ""
        print(f"    {c(val['color'], key):<20} {val['label']}{c(C.DIM, marker)}")
    choice = input(f"\n  {c(C.BOLD, 'Choose mode:')} ").strip().lower()
    if choice in MODES:
        current_mode = choice
        print(c(C.GREEN, f"  Switched to {MODES[current_mode]['label']} mode."))
    else:
        print(c(C.RED, "  Invalid mode. Keeping current mode."))


# ── Main loop ─────────────────────────────────────────────────────────────────

def get_api_key(args_key):
    if args_key:
        return args_key
    key = os.environ.get("ANTHROPIC_API_KEY", "")
    if key:
        return key
    print(c(C.YELLOW, "\n  No API key found."))
    print(c(C.DIM,    "  Get yours at: https://console.anthropic.com\n"))
    key = input(c(C.BOLD, "  Enter your Anthropic API key: ")).strip()
    if not key:
        print(c(C.RED, "  API key required. Exiting."))
        sys.exit(1)
    return key

def get_multiline_input(prompt):
    """Collect possibly multi-line input. End with \\ to continue."""
    lines = []
    first = True
    while True:
        try:
            line = input(prompt if first else "... ")
        except EOFError:
            break
        first = False
        if line.endswith("\\"):
            lines.append(line[:-1])
        else:
            lines.append(line)
            break
    return "\n".join(lines)

def main():
    global current_mode

    parser = argparse.ArgumentParser(description="AI Assistant powered by Claude")
    parser.add_argument("--key", help="Anthropic API key")
    parser.add_argument("--mode", choices=MODES.keys(), default="chat", help="Starting mode")
    args = parser.parse_args()

    current_mode = args.mode
    api_key = get_api_key(args.key)

    print_banner()
    print(c(C.DIM, f"  Mode: {MODES[current_mode]['label']}  |  Type /help for commands\n"))

    try:
        client = anthropic.Anthropic(api_key=api_key)
    except Exception as e:
        print(c(C.RED, f"  Failed to initialize client: {e}"))
        sys.exit(1)

    history = []

    while True:
        mode_label = c(MODES[current_mode]["color"], current_mode)
        prompt_str = f"\n{c(C.BOLD, 'You')} [{mode_label}]: "

        try:
            user_input = get_multiline_input(prompt_str).strip()
        except (KeyboardInterrupt, EOFError):
            print(f"\n\n{c(C.DIM, '  Goodbye!')}\n")
            break

        if not user_input:
            continue

        # Commands
        if user_input.lower() in ("/quit", "/exit", "/q"):
            print(f"\n{c(C.DIM, '  Goodbye!')}\n")
            break
        elif user_input.lower() == "/help":
            print_help()
            continue
        elif user_input.lower() == "/clear":
            history = []
            print(c(C.GREEN, "  Conversation cleared."))
            continue
        elif user_input.lower() == "/history":
            show_history(history)
            continue
        elif user_input.lower() == "/save":
            save_conversation(history)
            continue
        elif user_input.lower() == "/mode":
            switch_mode()
            continue

        # Send to AI
        print(f"\n{c(C.GREEN, 'AI')}: ", end="", flush=True)
        print(c(C.DIM, "(thinking...)"), end="\r", flush=True)

        try:
            reply, history = chat(client, history, user_input, current_mode)
            print(" " * 20, end="\r")  # clear "thinking..."
            print(f"{c(C.GREEN, 'AI')}:")
            print_separator()
            print(wrap_text(reply))
            print_separator()

        except Exception as e:
            print(" " * 20, end="\r")
            print(c(C.RED, f"\n  Error: {e}\n"))


if __name__ == "__main__":
    main()