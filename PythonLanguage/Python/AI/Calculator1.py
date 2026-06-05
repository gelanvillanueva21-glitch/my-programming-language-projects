import tkinter as tk

# ── colours ──────────────────────────────────────────────
BG        = "#181818"
DISP_BG   = "#242424"
DISP_FG   = "#FFFFFF"
NUM_BG    = "#323232"
NUM_FG    = "#FFFFFF"
OP_BG     = "#FF9500"
OP_FG     = "#FFFFFF"
EQ_BG     = "#4CD964"
EQ_FG     = "#000000"
CLR_BG    = "#FF3B30"
CLR_FG    = "#FFFFFF"
SPEC_BG   = "#505050"
SPEC_FG   = "#FFFFFF"
PRESS_CLR = "#888888"

# ── state ────────────────────────────────────────────────
expr       = ""   # e.g.  "12+3*4"
disp       = ""   # same but with × ÷ − shown
just_eval  = False

root = tk.Tk()
root.title("Calculator")
root.configure(bg=BG)
root.geometry("380x680")
root.resizable(False, False)

# ── display ──────────────────────────────────────────────
hist_var = tk.StringVar(value="")
main_var = tk.StringVar(value="0")

hist_label = tk.Label(root, textvariable=hist_var,
                      bg=DISP_BG, fg="#888888",
                      font=("Helvetica", 18), anchor="e",
                      padx=12, pady=4)
hist_label.pack(fill=tk.X)

main_label = tk.Label(root, textvariable=main_var,
                      bg=DISP_BG, fg=DISP_FG,
                      font=("Helvetica", 48, "bold"), anchor="e",
                      padx=12, pady=10)
main_label.pack(fill=tk.X)

tk.Frame(root, bg="#444444", height=2).pack(fill=tk.X)

# ── helpers ───────────────────────────────────────────────
def show(text):
    main_var.set(text)

def press(text):
    global expr, disp, just_eval

    OPERATORS = ('+', '-', '*', '/')

    if text == "C":
        expr = disp = ""
        hist_var.set("")
        show("0")
        just_eval = False
        return

    if text == "⌫":
        if just_eval:
            expr = disp = ""
            show("0")
            just_eval = False
            return
        disp = disp[:-1]
        expr = expr[:-1]
        # ** takes two chars when user pressed ^
        if disp.endswith("*"):   # shouldn't happen but guard
            expr = expr[:-1]
        show(disp if disp else "0")
        return

    if text == "=":
        if not expr:
            return
        try:
            hist_var.set(disp + " =")
            result = eval(expr)           # Python eval = full PEMDAS
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            elif isinstance(result, float):
                result = round(result, 8)
            expr = disp = str(result)
            show(expr)
            just_eval = True
        except ZeroDivisionError:
            show("Can't ÷ 0")
            expr = disp = ""
            just_eval = False
        except:
            show("Error")
            expr = disp = ""
            just_eval = False
        return

    if text == "±":
        try:
            val = eval(expr) * -1
            if isinstance(val, float) and val.is_integer():
                val = int(val)
            expr = disp = str(val)
            show(expr)
        except:
            pass
        return

    if text == "%":
        try:
            val = eval(expr) / 100
            if isinstance(val, float) and val.is_integer():
                val = int(val)
            expr = disp = str(val)
            show(expr)
        except:
            pass
        return

    # After evaluation: operator continues, digit restarts
    if just_eval:
        if text in ("+", "−", "×", "÷", "^"):
            just_eval = False
        else:
            expr = disp = ""
            just_eval = False

    # Map pretty symbols → Python operators
    MAP = {"×": "*", "÷": "/", "−": "-", "^": "**"}

    if text in MAP:
        expr += MAP[text]
        disp += text
    else:
        expr += text
        disp += text

    show(disp)

# ── button factory ────────────────────────────────────────
def make_btn(parent, label, bg, fg, cmd):
    b = tk.Button(parent, text=label, bg=bg, fg=fg,
                  font=("Helvetica", 24, "bold"),
                  relief=tk.FLAT, bd=0,
                  activebackground=PRESS_CLR, activeforeground="#fff",
                  command=cmd)
    b.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=3, pady=3)
    return b

# ── button grid ───────────────────────────────────────────
# Each row: list of (label, bg, fg)
ROWS = [
    [("C",   CLR_BG,  CLR_FG),
     ("±",   SPEC_BG, SPEC_FG),
     ("%",   SPEC_BG, SPEC_FG),
     ("÷",   OP_BG,   OP_FG)],

    [("7",   NUM_BG,  NUM_FG),
     ("8",   NUM_BG,  NUM_FG),
     ("9",   NUM_BG,  NUM_FG),
     ("×",   OP_BG,   OP_FG)],

    [("4",   NUM_BG,  NUM_FG),
     ("5",   NUM_BG,  NUM_FG),
     ("6",   NUM_BG,  NUM_FG),
     ("−",   OP_BG,   OP_FG)],

    [("1",   NUM_BG,  NUM_FG),
     ("2",   NUM_BG,  NUM_FG),
     ("3",   NUM_BG,  NUM_FG),
     ("+",   OP_BG,   OP_FG)],

    [("0",   NUM_BG,  NUM_FG),
     (".",   NUM_BG,  NUM_FG),
     ("⌫",  SPEC_BG, SPEC_FG),
     ("=",   EQ_BG,   EQ_FG)],
]

btn_area = tk.Frame(root, bg=BG)
btn_area.pack(fill=tk.BOTH, expand=True, padx=4, pady=6)

for row_def in ROWS:
    row_frame = tk.Frame(btn_area, bg=BG)
    row_frame.pack(fill=tk.BOTH, expand=True)
    for (label, bg, fg) in row_def:
        make_btn(row_frame, label, bg, fg, lambda l=label: press(l))

root.mainloop()
