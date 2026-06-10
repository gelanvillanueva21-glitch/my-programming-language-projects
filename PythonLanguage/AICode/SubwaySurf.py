"""
SURF RUN - Subway Surfers-style game in Python
Requirements: pip install pygame
Run: python subway_surfers.py

Controls:
  Arrow Left / A  -> Move left lane
  Arrow Right / D -> Move right lane
  Arrow Up / Space -> Jump
  Arrow Down / S  -> Slide
"""

import pygame
import random
import math
import json
import os
import sys

pygame.init()
pygame.mixer.init()

# ─── Constants ────────────────────────────────────────────────────────────────
SCREEN_W, SCREEN_H = 480, 720
FPS = 60
SAVE_FILE = "surf_run_save.json"

LANE_COUNT = 3
LANE_SPACING = 110
LANE_CENTER_X = SCREEN_W // 2
LANE_XS = [LANE_CENTER_X - LANE_SPACING, LANE_CENTER_X, LANE_CENTER_X + LANE_SPACING]
GROUND_Y = int(SCREEN_H * 0.78)

# Colors
BLACK       = (0, 0, 0)
WHITE       = (255, 255, 255)
GOLD        = (255, 215, 0)
DARK_GOLD   = (180, 140, 0)
SKY_TOP     = (13, 0, 37)
SKY_BOT     = (26, 0, 80)
GROUND_TOP  = (50, 50, 50)
GROUND_BOT  = (25, 25, 25)
RAIL_COLOR  = (120, 120, 120)
TIE_COLOR   = (74, 63, 46)
RED         = (220, 50, 50)
BLUE        = (30, 100, 200)
GREEN       = (30, 140, 60)
PURPLE      = (100, 30, 160)
ORANGE      = (220, 100, 20)
CYAN        = (0, 200, 220)
PINK        = (240, 100, 160)
YELLOW      = (240, 220, 40)

OBSTACLE_COLORS = [RED, BLUE, GREEN, PURPLE, ORANGE]

CHARACTERS = [
    {"id": "jake",   "name": "Jake",   "color": (80, 195, 247),  "price": 0,    "emoji": "J"},
    {"id": "tricky", "name": "Tricky", "color": (244, 143, 177), "price": 200,  "emoji": "T"},
    {"id": "fresh",  "name": "Fresh",  "color": (165, 214, 167), "price": 350,  "emoji": "F"},
    {"id": "dino",   "name": "Dino",   "color": (255, 204, 128), "price": 500,  "emoji": "D"},
    {"id": "ghost",  "name": "Ghost",  "color": (224, 224, 224), "price": 800,  "emoji": "G"},
    {"id": "robot",  "name": "Robot",  "color": (128, 222, 234), "price": 1200, "emoji": "R"},
]

POWERUPS = [
    {"id": "magnet", "name": "Magnet",   "color": PINK,   "price": 150,
     "desc": "Auto-collects coins nearby", "duration": 600},
    {"id": "shield", "name": "Shield",   "color": CYAN,   "price": 300,
     "desc": "Absorbs one hit",            "duration": 600},
    {"id": "boost",  "name": "2x Score", "color": YELLOW, "price": 250,
     "desc": "Doubles score gain",         "duration": 600},
]

# ─── Save / Load ──────────────────────────────────────────────────────────────
def load_save():
    default = {"coins": 0, "best": 0, "owned": ["jake"],
                "active_char": "jake", "powerups": {}}
    if os.path.exists(SAVE_FILE):
        try:
            with open(SAVE_FILE) as f:
                data = json.load(f)
                for k, v in default.items():
                    data.setdefault(k, v)
                return data
        except Exception:
            pass
    return default

def write_save(save):
    with open(SAVE_FILE, "w") as f:
        json.dump(save, f)

# ─── Helpers ──────────────────────────────────────────────────────────────────
def lerp(a, b, t):
    return a + (b - a) * t

def draw_rounded_rect(surf, color, rect, radius=10):
    pygame.draw.rect(surf, color, rect, border_radius=radius)

def shade(color, amt):
    return tuple(max(0, min(255, c + amt)) for c in color)

def draw_text(surf, text, size, color, x, y, center=True, bold=False):
    font = pygame.font.SysFont("Arial", size, bold=bold)
    rendered = font.render(text, True, color)
    rect = rendered.get_rect()
    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)
    surf.blit(rendered, rect)
    return rect

# ─── Particle ─────────────────────────────────────────────────────────────────
class Particle:
    def __init__(self, x, y, color):
        angle = random.uniform(0, math.pi * 2)
        spd = random.uniform(2, 6)
        self.x = x
        self.y = y
        self.vx = math.cos(angle) * spd
        self.vy = math.sin(angle) * spd
        self.r = random.randint(3, 7)
        self.color = color
        self.life = 30
        self.max_life = 30

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += 0.15
        self.life -= 1

    def draw(self, surf):
        alpha = int(255 * self.life / self.max_life)
        r = max(1, int(self.r * self.life / self.max_life))
        s = pygame.Surface((r * 2, r * 2), pygame.SRCALPHA)
        pygame.draw.circle(s, (*self.color, alpha), (r, r), r)
        surf.blit(s, (int(self.x) - r, int(self.y) - r))

# ─── Coin ─────────────────────────────────────────────────────────────────────
class Coin:
    def __init__(self, lane, y):
        self.lane = lane
        self.x = float(LANE_XS[lane])
        self.y = float(y)
        self.r = 13

    def update(self, speed, player_x, player_y, magnet_active):
        self.y += speed
        if magnet_active:
            dx = player_x - self.x
            dy = player_y - self.y
            dist = math.hypot(dx, dy)
            if dist < 100:
                self.x += dx * 0.13
                self.y += dy * 0.13

    def draw(self, surf, frame):
        pulse = math.sin(frame * 0.1 + self.lane) * 0.12 + 1
        r = int(self.r * pulse)
        # Glow
        glow = pygame.Surface((r * 5, r * 5), pygame.SRCALPHA)
        pygame.draw.circle(glow, (255, 215, 0, 50), (r * 2 + r // 2, r * 2 + r // 2), r * 2)
        surf.blit(glow, (int(self.x) - r * 2 - r // 2, int(self.y) - r * 2 - r // 2))
        # Body
        pygame.draw.circle(surf, GOLD, (int(self.x), int(self.y)), r)
        pygame.draw.circle(surf, DARK_GOLD, (int(self.x), int(self.y)), r, 2)
        draw_text(surf, "$", max(8, r), DARK_GOLD, int(self.x), int(self.y))

    def get_rect(self):
        return pygame.Rect(self.x - self.r, self.y - self.r, self.r * 2, self.r * 2)

# ─── Obstacle ─────────────────────────────────────────────────────────────────
class Obstacle:
    def __init__(self, lane):
        self.lane = lane
        self.x = LANE_XS[lane]
        self.y = -90
        self.w = 72
        self.h = random.choice([50, 60, 44])
        self.color = random.choice(OBSTACLE_COLORS)
        self.is_low = self.h == 44   # low = can jump over, else must slide around

    def update(self, speed):
        self.y += speed

    def draw(self, surf):
        rect = pygame.Rect(self.x - self.w // 2, int(self.y), self.w, self.h)
        draw_rounded_rect(surf, self.color, rect, 8)
        draw_rounded_rect(surf, shade(self.color, -40), rect, 8)
        pygame.draw.rect(surf, shade(self.color, -40), rect, 3, border_radius=8)
        # Windows
        for i in range(2):
            wx = rect.x + 8 + i * 22
            wy = rect.y + 8
            pygame.draw.rect(surf, (150, 220, 255, 180), (wx, wy, 14, 10), border_radius=3)
        # Wheels
        for side in [-1, 1]:
            cx = self.x + side * (self.w // 2 - 12)
            cy = int(self.y) + self.h - 6
            pygame.draw.circle(surf, (30, 30, 30), (cx, cy), 8)
            pygame.draw.circle(surf, (80, 80, 80), (cx, cy), 8, 2)
        # Warning stripes if low barrier
        if self.is_low:
            for i in range(3):
                sx = rect.x + 8 + i * 18
                stripe = pygame.Surface((8, self.h - 10), pygame.SRCALPHA)
                stripe.fill((255, 200, 0, 160))
                surf.blit(stripe, (sx, rect.y + 5))

    def get_rect(self):
        margin = 10
        return pygame.Rect(
            self.x - self.w // 2 + margin,
            int(self.y) + margin,
            self.w - margin * 2,
            self.h - margin * 2
        )

# ─── Player ───────────────────────────────────────────────────────────────────
class Player:
    def __init__(self, char_data):
        self.lane = 1
        self.x = float(LANE_XS[1])
        self.target_x = self.x
        self.y = float(GROUND_Y - 60)
        self.vy = 0.0
        self.on_ground = True
        self.sliding = False
        self.slide_timer = 0
        self.w = 36
        self.h = 60
        self.anim_frame = 0
        self.anim_tick = 0
        self.invincible = 0
        self.char = char_data

    def move_lane(self, direction):
        new_lane = self.lane + direction
        if 0 <= new_lane <= 2:
            self.lane = new_lane

    def jump(self):
        if self.on_ground:
            self.vy = -16
            self.on_ground = False
            self.sliding = False

    def slide(self):
        if self.on_ground and not self.sliding:
            self.sliding = True
            self.slide_timer = 45

    def update(self):
        # Lane lerp
        self.target_x = float(LANE_XS[self.lane])
        self.x = lerp(self.x, self.target_x, 0.18)

        # Gravity
        if not self.on_ground:
            self.vy += 0.7
            self.y += self.vy
            if self.y + self.h >= GROUND_Y:
                self.y = float(GROUND_Y - self.h)
                self.vy = 0
                self.on_ground = True

        # Slide countdown
        if self.sliding:
            self.slide_timer -= 1
            if self.slide_timer <= 0:
                self.sliding = False

        # Animation
        self.anim_tick += 1
        if self.anim_tick % 6 == 0:
            self.anim_frame += 1

        if self.invincible > 0:
            self.invincible -= 1

    def get_rect(self):
        draw_h = int(self.h * 0.55) if self.sliding else self.h
        draw_y = GROUND_Y - draw_h if self.sliding else int(self.y)
        return pygame.Rect(
            int(self.x) - self.w // 2 + 4,
            draw_y + 4,
            self.w - 8,
            int(draw_h * 0.85)
        )

    def draw(self, surf, shield_active, magnet_active, boost_active):
        bounce = int(math.sin(self.anim_frame * 0.35) * 2) if self.on_ground else 0
        draw_h = int(self.h * 0.55) if self.sliding else self.h
        draw_y = GROUND_Y - draw_h if self.sliding else int(self.y)
        cx = int(self.x)
        color = self.char["color"]

        # Shadow
        shadow = pygame.Surface((50, 16), pygame.SRCALPHA)
        pygame.draw.ellipse(shadow, (0, 0, 0, 80), (0, 0, 50, 16))
        surf.blit(shadow, (cx - 25, GROUND_Y - 4))

        # Shield ring
        if shield_active:
            s = pygame.Surface((100, 100), pygame.SRCALPHA)
            pygame.draw.ellipse(s, (100, 200, 255, 80), (0, 0, 100, 100), 4)
            surf.blit(s, (cx - 50, draw_y + draw_h // 2 - 50 + bounce))

        # Magnet ring
        if magnet_active:
            s = pygame.Surface((160, 160), pygame.SRCALPHA)
            pygame.draw.ellipse(s, (255, 100, 255, 55), (0, 0, 160, 160), 3)
            surf.blit(s, (cx - 80, draw_y + draw_h // 2 - 80 + bounce))

        # Legs (only when not sliding)
        if not self.sliding:
            leg_swing = int(math.sin(self.anim_frame * 0.5) * 10) if self.on_ground else 0
            draw_rounded_rect(surf, (30, 30, 30),
                (cx - 14, draw_y + int(draw_h * 0.62) + bounce, 13, draw_h - int(draw_h * 0.62) - leg_swing // 2), 5)
            draw_rounded_rect(surf, (30, 30, 30),
                (cx + 1, draw_y + int(draw_h * 0.62) + bounce, 13, draw_h - int(draw_h * 0.62) + leg_swing // 2), 5)

        # Torso
        body_rect = (
            cx - self.w // 2,
            draw_y + (0 if self.sliding else int(draw_h * 0.25)) + bounce,
            self.w,
            draw_h if self.sliding else int(draw_h * 0.5)
        )
        draw_rounded_rect(surf, color, body_rect, 10)
        draw_rounded_rect(surf, shade(color, -30), body_rect, 10)
        pygame.draw.rect(surf, shade(color, -30), body_rect, 2, border_radius=10)

        # Head
        if not self.sliding:
            head_cx = cx
            head_cy = draw_y + int(draw_h * 0.13) + bounce
            pygame.draw.circle(surf, shade(color, 30), (head_cx, head_cy), 14)
            pygame.draw.circle(surf, shade(color, -20), (head_cx, head_cy), 14, 2)
            draw_text(surf, self.char["emoji"], 14, (50, 50, 50), head_cx, head_cy)

        # Boost trail
        if boost_active:
            for i in range(3):
                s = pygame.Surface((30, 40), pygame.SRCALPHA)
                s.fill((255, 210, 0, 30 - i * 8))
                surf.blit(s, (cx - 15 - i * 10, draw_y + draw_h // 2 - 20 + bounce))

        # Invincibility flash
        if self.invincible > 0 and (self.invincible // 4) % 2 == 0:
            flash = pygame.Surface((self.w, draw_h), pygame.SRCALPHA)
            flash.fill((255, 255, 255, 100))
            surf.blit(flash, (cx - self.w // 2, draw_y + bounce))

# ─── Background ───────────────────────────────────────────────────────────────
class Background:
    def __init__(self):
        self.buildings = []
        self.stars = [(random.randint(0, SCREEN_W), random.randint(0, int(SCREEN_H * 0.55)),
                       random.uniform(0.5, 1.5)) for _ in range(60)]
        self._gen_buildings()
        self.tie_offset = 0.0

    def _gen_buildings(self):
        self.buildings = []
        x = 0
        while x < SCREEN_W + 100:
            w = random.randint(55, 110)
            h = random.randint(80, 180)
            color = (random.randint(15, 28), random.randint(5, 18), random.randint(30, 55))
            self.buildings.append({"x": float(x), "w": w, "h": h, "color": color,
                                   "rows": random.randint(2, 5), "cols": random.randint(2, 4)})
            x += w + random.randint(5, 20)

    def update(self, speed):
        for b in self.buildings:
            b["x"] -= speed * 0.15
        if self.buildings and self.buildings[0]["x"] + self.buildings[0]["w"] < 0:
            self.buildings.pop(0)
            last = self.buildings[-1]
            nx = last["x"] + last["w"] + random.randint(5, 20)
            w = random.randint(55, 110)
            h = random.randint(80, 180)
            color = (random.randint(15, 28), random.randint(5, 18), random.randint(30, 55))
            self.buildings.append({"x": float(nx), "w": w, "h": h, "color": color,
                                   "rows": random.randint(2, 5), "cols": random.randint(2, 4)})
        self.tie_offset = (self.tie_offset + speed * 0.4) % 40

    def draw(self, surf, frame):
        # Sky gradient (manual)
        for y in range(int(SCREEN_H * 0.6)):
            t = y / (SCREEN_H * 0.6)
            r = int(SKY_TOP[0] + (SKY_BOT[0] - SKY_TOP[0]) * t)
            g = int(SKY_TOP[1] + (SKY_BOT[1] - SKY_TOP[1]) * t)
            b = int(SKY_TOP[2] + (SKY_BOT[2] - SKY_TOP[2]) * t)
            pygame.draw.line(surf, (r, g, b), (0, y), (SCREEN_W, y))

        # Stars
        for sx, sy, ss in self.stars:
            br = int(180 + math.sin(frame * 0.05 + sx) * 55)
            pygame.draw.circle(surf, (br, br, br), (sx, sy), max(1, int(ss)))

        # Buildings
        for b in self.buildings:
            bx = int(b["x"])
            by = GROUND_Y - b["h"]
            pygame.draw.rect(surf, b["color"], (bx, by, b["w"], b["h"]))
            ww, wh = 10, 13
            for r in range(b["rows"]):
                for c in range(b["cols"]):
                    wx = bx + 8 + c * (ww + 8)
                    wy = by + 10 + r * (wh + 9)
                    if wx + ww < bx + b["w"] - 6:
                        lit = math.sin(bx * 0.07 + r * 5 + c * 9 + frame * 0.004) > 0.15
                        wcolor = (240, 220, 100) if lit else (0, 0, 40)
                        pygame.draw.rect(surf, wcolor, (wx, wy, ww, wh), border_radius=2)

        # Ground
        for y in range(GROUND_Y, SCREEN_H):
            t = (y - GROUND_Y) / (SCREEN_H - GROUND_Y)
            r = int(GROUND_TOP[0] + (GROUND_BOT[0] - GROUND_TOP[0]) * t)
            g = int(GROUND_TOP[1] + (GROUND_BOT[1] - GROUND_TOP[1]) * t)
            b = int(GROUND_TOP[2] + (GROUND_BOT[2] - GROUND_TOP[2]) * t)
            pygame.draw.line(surf, (r, g, b), (0, y), (SCREEN_W, y))

        # Rails and ties
        for lx in LANE_XS:
            # Ties
            y = GROUND_Y + self.tie_offset
            while y < SCREEN_H:
                pygame.draw.rect(surf, TIE_COLOR, (lx - 28, int(y), 56, 7), border_radius=2)
                y += 40
            # Rails
            pygame.draw.line(surf, RAIL_COLOR, (lx - 20, GROUND_Y), (lx - 20, SCREEN_H), 4)
            pygame.draw.line(surf, RAIL_COLOR, (lx + 20, GROUND_Y), (lx + 20, SCREEN_H), 4)

# ─── HUD ──────────────────────────────────────────────────────────────────────
def draw_hud(surf, score, coins_run, best, magnet_t, shield_t, boost_t, frame):
    font_sm = pygame.font.SysFont("Arial", 11, bold=True)
    font_lg = pygame.font.SysFont("Arial Black", 22, bold=True)

    def hud_box(label, value, x, y, val_color=GOLD):
        bg = pygame.Surface((100, 48), pygame.SRCALPHA)
        bg.fill((0, 0, 0, 140))
        surf.blit(bg, (x, y))
        pygame.draw.rect(surf, (80, 80, 80), (x, y, 100, 48), 1, border_radius=10)
        lbl = font_sm.render(label, True, (170, 170, 170))
        surf.blit(lbl, (x + 50 - lbl.get_width() // 2, y + 5))
        val = font_lg.render(str(value), True, val_color)
        surf.blit(val, (x + 50 - val.get_width() // 2, y + 20))

    hud_box("SCORE", int(score), 5, 5)
    hud_box("🪙 COINS", coins_run, SCREEN_W // 2 - 50, 5)
    hud_box("BEST", best, SCREEN_W - 105, 5)

    # Powerup bars
    items = []
    if magnet_t > 0:  items.append(("MAG", magnet_t, 600, PINK))
    if shield_t > 0:  items.append(("SHD", shield_t, 600, CYAN))
    if boost_t > 0:   items.append(("2X",  boost_t,  600, YELLOW))

    for i, (label, t, max_t, color) in enumerate(items):
        bx = SCREEN_W // 2 - len(items) * 55 // 2 + i * 55
        by = 62
        pygame.draw.rect(surf, (40, 40, 40), (bx - 22, by, 44, 8), border_radius=4)
        fill_w = int(44 * t / max_t)
        if fill_w > 0:
            pygame.draw.rect(surf, color, (bx - 22, by, fill_w, 8), border_radius=4)
        lbl = font_sm.render(label, True, color)
        surf.blit(lbl, (bx - lbl.get_width() // 2, by - 13))

# ─── Shop Screen ──────────────────────────────────────────────────────────────
def draw_shop(surf, save_data, selected=None, message=""):
    surf.fill((10, 0, 30))
    draw_text(surf, "SHOP", 38, GOLD, SCREEN_W // 2, 34, bold=True)
    draw_text(surf, f"Your coins: {save_data['coins']}", 18, GOLD, SCREEN_W // 2, 68)

    buttons = []

    # Characters section
    draw_text(surf, "CHARACTERS", 13, (170, 170, 170), SCREEN_W // 2, 98)
    pygame.draw.line(surf, (60, 60, 60), (20, 108), (SCREEN_W - 20, 108))

    cols = 3
    cw, ch_h = 120, 90
    start_x = (SCREEN_W - cols * cw) // 2 + cw // 2
    for i, ch in enumerate(CHARACTERS):
        col = i % cols
        row = i // cols
        cx = start_x + col * cw
        cy = 155 + row * (ch_h + 10)
        owned = ch["id"] in save_data["owned"]
        active = save_data["active_char"] == ch["id"]
        border_color = GOLD if active else ((40, 200, 100) if owned else (80, 80, 80))
        box_color = (40, 20, 80) if active else (25, 10, 45)
        rect = pygame.Rect(cx - 50, cy - ch_h // 2, 100, ch_h)
        draw_rounded_rect(surf, box_color, rect, 10)
        pygame.draw.rect(surf, border_color, rect, 2, border_radius=10)
        # Character circle
        pygame.draw.circle(surf, ch["color"], (cx, cy - 18), 18)
        draw_text(surf, ch["emoji"], 16, (30, 30, 30), cx, cy - 18, bold=True)
        draw_text(surf, ch["name"], 12, WHITE, cx, cy + 5, bold=True)
        if active:
            draw_text(surf, "ACTIVE", 10, GOLD, cx, cy + 22)
        elif owned:
            draw_text(surf, "SELECT", 10, (40, 200, 100), cx, cy + 22)
        else:
            draw_text(surf, f"🪙 {ch['price']}", 11, GOLD, cx, cy + 22)
        buttons.append({"type": "char", "id": ch["id"], "rect": rect, "data": ch})

    # Powerups section
    pu_start_y = 340
    draw_text(surf, "POWER-UPS", 13, (170, 170, 170), SCREEN_W // 2, pu_start_y)
    pygame.draw.line(surf, (60, 60, 60), (20, pu_start_y + 10), (SCREEN_W - 20, pu_start_y + 10))

    pu_cols = 3
    pu_cw = SCREEN_W // pu_cols
    for i, pu in enumerate(POWERUPS):
        px = pu_cw * i + pu_cw // 2
        py = pu_start_y + 65
        owned = save_data["powerups"].get(pu["id"], False)
        border_color = (40, 200, 100) if owned else (80, 80, 80)
        rect = pygame.Rect(px - 60, py - 40, 120, 90)
        draw_rounded_rect(surf, (20, 10, 40), rect, 10)
        pygame.draw.rect(surf, border_color, rect, 2, border_radius=10)
        pygame.draw.circle(surf, pu["color"], (px, py - 15), 18)
        draw_text(surf, pu["name"][0], 16, (30, 30, 30), px, py - 15, bold=True)
        draw_text(surf, pu["name"], 11, WHITE, px, py + 8, bold=True)
        draw_text(surf, pu["desc"][:18], 9, (180, 180, 180), px, py + 22)
        if owned:
            draw_text(surf, "OWNED", 10, (40, 200, 100), px, py + 36)
        else:
            draw_text(surf, f"🪙 {pu['price']}", 11, GOLD, px, py + 36)
        buttons.append({"type": "powerup", "id": pu["id"], "rect": rect, "data": pu})

    # Close button
    close_rect = pygame.Rect(SCREEN_W // 2 - 80, SCREEN_H - 60, 160, 44)
    draw_rounded_rect(surf, (80, 20, 140), close_rect, 22)
    pygame.draw.rect(surf, (140, 60, 220), close_rect, 2, border_radius=22)
    draw_text(surf, "✕  CLOSE", 18, WHITE, SCREEN_W // 2, SCREEN_H - 38, bold=True)
    buttons.append({"type": "close", "rect": close_rect})

    if message:
        msg_color = RED if "Not enough" in message else (40, 200, 100)
        draw_text(surf, message, 14, msg_color, SCREEN_W // 2, SCREEN_H - 75)

    return buttons

# ─── Menu / Game Over screens ─────────────────────────────────────────────────
def draw_menu(surf, best, frame):
    # Animated background gradient
    surf.fill(SKY_TOP)
    draw_text(surf, "SURF RUN", 52, GOLD, SCREEN_W // 2, SCREEN_H // 2 - 120, bold=True)
    draw_text(surf, "Dodge obstacles · Collect coins", 15, (180, 180, 200),
              SCREEN_W // 2, SCREEN_H // 2 - 65)
    draw_text(surf, f"Best: {best}", 16, GOLD, SCREEN_W // 2, SCREEN_H // 2 - 40)

    play_rect = pygame.Rect(SCREEN_W // 2 - 90, SCREEN_H // 2 - 10, 180, 52)
    draw_rounded_rect(surf, (200, 80, 20), play_rect, 26)
    pygame.draw.rect(surf, (255, 140, 60), play_rect, 2, border_radius=26)
    draw_text(surf, "▶  PLAY", 22, WHITE, SCREEN_W // 2, SCREEN_H // 2 + 16, bold=True)

    shop_rect = pygame.Rect(SCREEN_W // 2 - 80, SCREEN_H // 2 + 60, 160, 44)
    draw_rounded_rect(surf, (60, 20, 110), shop_rect, 22)
    pygame.draw.rect(surf, (120, 60, 200), shop_rect, 2, border_radius=22)
    draw_text(surf, "🛒  SHOP", 18, WHITE, SCREEN_W // 2, SCREEN_H // 2 + 82, bold=True)

    draw_text(surf, "← → or A/D  move lanes", 13, (140, 140, 160), SCREEN_W // 2, SCREEN_H // 2 + 122)
    draw_text(surf, "↑ or SPACE  jump  |  ↓ or S  slide", 13, (140, 140, 160), SCREEN_W // 2, SCREEN_H // 2 + 142)

    return play_rect, shop_rect

def draw_gameover(surf, score, coins_run, best, total_coins):
    overlay = pygame.Surface((SCREEN_W, SCREEN_H), pygame.SRCALPHA)
    overlay.fill((10, 0, 30, 220))
    surf.blit(overlay, (0, 0))

    draw_text(surf, "GAME OVER", 44, RED, SCREEN_W // 2, SCREEN_H // 2 - 130, bold=True)
    draw_text(surf, f"Score:  {int(score)}", 20, WHITE, SCREEN_W // 2, SCREEN_H // 2 - 72)
    draw_text(surf, f"Coins collected:  {coins_run}", 18, GOLD, SCREEN_W // 2, SCREEN_H // 2 - 44)
    draw_text(surf, f"Total coins:  {total_coins}", 18, GOLD, SCREEN_W // 2, SCREEN_H // 2 - 16)
    draw_text(surf, f"Best:  {best}", 18, (100, 240, 150), SCREEN_W // 2, SCREEN_H // 2 + 12)

    retry_rect = pygame.Rect(SCREEN_W // 2 - 90, SCREEN_H // 2 + 46, 180, 52)
    draw_rounded_rect(surf, (200, 80, 20), retry_rect, 26)
    pygame.draw.rect(surf, (255, 140, 60), retry_rect, 2, border_radius=26)
    draw_text(surf, "↺  RETRY", 22, WHITE, SCREEN_W // 2, SCREEN_H // 2 + 72, bold=True)

    shop_rect = pygame.Rect(SCREEN_W // 2 - 80, SCREEN_H // 2 + 110, 160, 44)
    draw_rounded_rect(surf, (60, 20, 110), shop_rect, 22)
    pygame.draw.rect(surf, (120, 60, 200), shop_rect, 2, border_radius=22)
    draw_text(surf, "🛒  SHOP", 18, WHITE, SCREEN_W // 2, SCREEN_H // 2 + 132, bold=True)

    return retry_rect, shop_rect

# ─── Main ─────────────────────────────────────────────────────────────────────
def main():
    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    pygame.display.set_caption("Surf Run")
    clock = pygame.time.Clock()

    save_data = load_save()
    bg = Background()

    # Game states
    MENU = "menu"
    PLAYING = "playing"
    DEAD = "dead"
    SHOP = "shop"

    game_state = MENU
    player = None
    obstacles = []
    coins = []
    particles = []
    score = 0.0
    coins_run = 0
    speed = 5.0
    frame = 0
    spawn_timer = 0
    coin_timer = 0
    magnet_t = 0
    shield_t = 0
    boost_t = 0
    shop_message = ""
    shop_message_timer = 0
    prev_state = MENU

    def get_char_data():
        for ch in CHARACTERS:
            if ch["id"] == save_data["active_char"]:
                return ch
        return CHARACTERS[0]

    def start_game():
        nonlocal player, obstacles, coins, particles, score, coins_run
        nonlocal speed, frame, spawn_timer, coin_timer
        nonlocal magnet_t, shield_t, boost_t
        player = Player(get_char_data())
        obstacles = []
        coins = []
        particles = []
        score = 0.0
        coins_run = 0
        speed = 5.0
        frame = 0
        spawn_timer = 0
        coin_timer = 0
        magnet_t = 600 if save_data["powerups"].get("magnet") else 0
        shield_t = 600 if save_data["powerups"].get("shield") else 0
        boost_t  = 600 if save_data["powerups"].get("boost")  else 0

    running = True
    shop_buttons = []
    retry_rect = play_rect = shop_rect_menu = shop_rect_go = None

    while running:
        dt = clock.tick(FPS)
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if game_state == PLAYING and player:
                    if event.key in (pygame.K_LEFT, pygame.K_a):
                        player.move_lane(-1)
                    elif event.key in (pygame.K_RIGHT, pygame.K_d):
                        player.move_lane(1)
                    elif event.key in (pygame.K_UP, pygame.K_SPACE):
                        player.jump()
                    elif event.key in (pygame.K_DOWN, pygame.K_s):
                        player.slide()
                elif game_state == SHOP:
                    if event.key == pygame.K_ESCAPE:
                        game_state = prev_state

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx, my = event.pos

                if game_state == MENU:
                    if play_rect and play_rect.collidepoint(mx, my):
                        start_game()
                        game_state = PLAYING
                    elif shop_rect_menu and shop_rect_menu.collidepoint(mx, my):
                        prev_state = MENU
                        game_state = SHOP

                elif game_state == DEAD:
                    if retry_rect and retry_rect.collidepoint(mx, my):
                        start_game()
                        game_state = PLAYING
                    elif shop_rect_go and shop_rect_go.collidepoint(mx, my):
                        prev_state = DEAD
                        game_state = SHOP

                elif game_state == SHOP:
                    for btn in shop_buttons:
                        if btn["rect"].collidepoint(mx, my):
                            if btn["type"] == "close":
                                game_state = prev_state
                            elif btn["type"] == "char":
                                ch = btn["data"]
                                if save_data["active_char"] == ch["id"]:
                                    pass
                                elif ch["id"] in save_data["owned"]:
                                    save_data["active_char"] = ch["id"]
                                    write_save(save_data)
                                    shop_message = f"{ch['name']} selected!"
                                    shop_message_timer = 90
                                elif save_data["coins"] >= ch["price"]:
                                    save_data["coins"] -= ch["price"]
                                    save_data["owned"].append(ch["id"])
                                    save_data["active_char"] = ch["id"]
                                    write_save(save_data)
                                    shop_message = f"{ch['name']} unlocked!"
                                    shop_message_timer = 90
                                else:
                                    shop_message = "Not enough coins!"
                                    shop_message_timer = 90
                            elif btn["type"] == "powerup":
                                pu = btn["data"]
                                if save_data["powerups"].get(pu["id"]):
                                    shop_message = "Already owned!"
                                    shop_message_timer = 90
                                elif save_data["coins"] >= pu["price"]:
                                    save_data["coins"] -= pu["price"]
                                    save_data["powerups"][pu["id"]] = True
                                    write_save(save_data)
                                    shop_message = f"{pu['name']} purchased!"
                                    shop_message_timer = 90
                                else:
                                    shop_message = "Not enough coins!"
                                    shop_message_timer = 90
                            break

        # ── Update ────────────────────────────────────────────────────────────
        if game_state == PLAYING and player:
            frame += 1
            score += 0.2 if (boost_t > 0) else 0.1
            if score > save_data["best"]:
                save_data["best"] = int(score)
                write_save(save_data)
            speed = min(5.0 + (score // 200) * 0.5, 16.0)

            player.update()
            bg.update(speed)

            # Powerup timers
            if magnet_t > 0: magnet_t -= 1
            if shield_t > 0: shield_t -= 1
            if boost_t  > 0: boost_t  -= 1

            # Spawn
            spawn_rate = max(55, 110 - int(score // 100) * 5)
            spawn_timer += 1
            if spawn_timer >= spawn_rate:
                spawn_timer = 0
                lane = random.randint(0, 2)
                obstacles.append(Obstacle(lane))

            coin_timer += 1
            if coin_timer >= 70:
                coin_timer = 0
                lane = random.randint(0, 2)
                count = random.randint(3, 6)
                for ci in range(count):
                    coins.append(Coin(lane, -80 - ci * 38))

            # Update obstacles
            for o in obstacles:
                o.update(speed)
            obstacles = [o for o in obstacles if o.y < SCREEN_H + 100]

            # Update coins
            for c in coins:
                c.update(speed, player.x, player.y + player.h / 2, magnet_t > 0)
            coins = [c for c in coins if c.y < SCREEN_H + 50]

            # Update particles
            for p in particles:
                p.update()
            particles = [p for p in particles if p.life > 0]

            # Collisions - obstacles
            p_rect = player.get_rect()
            for o in obstacles[:]:
                if p_rect.colliderect(o.get_rect()):
                    if player.invincible > 0:
                        continue
                    if shield_t > 0:
                        shield_t = 0
                        for _ in range(8):
                            particles.append(Particle(o.x, o.y + o.h / 2, CYAN))
                        obstacles.remove(o)
                        player.invincible = 60
                        continue
                    # Die
                    for _ in range(12):
                        particles.append(Particle(player.x, player.y + player.h / 2, player.char["color"]))
                    save_data["coins"] += coins_run
                    write_save(save_data)
                    game_state = DEAD
                    break

            # Collisions - coins
            for c in coins[:]:
                if p_rect.colliderect(c.get_rect()):
                    coins_run += 1
                    for _ in range(5):
                        particles.append(Particle(c.x, c.y, GOLD))
                    coins.remove(c)

        elif game_state != PLAYING:
            bg.update(2.0)
            frame += 1
            for p in particles:
                p.update()
            particles = [p for p in particles if p.life > 0]

        if shop_message_timer > 0:
            shop_message_timer -= 1
            if shop_message_timer == 0:
                shop_message = ""

        # ── Draw ──────────────────────────────────────────────────────────────
        bg.draw(screen, frame)

        if game_state == PLAYING and player:
            for o in obstacles:
                o.draw(screen)
            for c in coins:
                c.draw(screen, frame)
            for p in particles:
                p.draw(screen)
            player.draw(screen, shield_t > 0, magnet_t > 0, boost_t > 0)
            draw_hud(screen, score, coins_run, save_data["best"],
                     magnet_t, shield_t, boost_t, frame)

        elif game_state == MENU:
            for p in particles:
                p.draw(screen)
            play_rect, shop_rect_menu = draw_menu(screen, save_data["best"], frame)

        elif game_state == DEAD:
            for p in particles:
                p.draw(screen)
            if player:
                player.draw(screen, False, False, False)
            retry_rect, shop_rect_go = draw_gameover(
                screen, score, coins_run, save_data["best"], save_data["coins"])

        elif game_state == SHOP:
            msg = shop_message if shop_message_timer > 0 else ""
            shop_buttons = draw_shop(screen, save_data, message=msg)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()