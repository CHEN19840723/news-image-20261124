#!/usr/bin/env python3
"""Draw the 24 November 2026 front page (1024x1024 PNG).

Fresh build for make.fun news-image-20261124. Every fact on the page was
checked against a real source on Tuesday morning, 24 November 2026; see
BUILD_NOTES.md for the sources. Draws a newspaper front page with PIL
only — no network, no photographs, no copied artwork.
"""

from PIL import Image, ImageDraw, ImageFont

CANVAS = (1024, 1024)
NEWS = (250, 246, 238)      # newsprint
INK = (22, 22, 22)
SCARLET = (172, 30, 32)
NAVY = (18, 33, 61)
STEEL = (84, 96, 116)
MIST = (226, 231, 238)
RULE = (196, 188, 172)
WHITE = (255, 255, 255)

FONT_DIR = "/usr/share/fonts/truetype/noto/"


def load(name, size):
    return ImageFont.truetype(FONT_DIR + name, size)


SERIF_XB = lambda s: load("NotoSerif-Black.ttf", s)
SERIF_B = lambda s: load("NotoSerif-Bold.ttf", s)
SANS_XB = lambda s: load("NotoSans-Black.ttf", s)
SANS_B = lambda s: load("NotoSans-Bold.ttf", s)
SANS = lambda s: load("NotoSans-Regular.ttf", s)


def split_lines(draw, text, fnt, width):
    """Greedy wrap: pack as many words per line as fit."""
    out = []
    current = ""
    for word in text.split():
        trial = (current + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            current = trial
        else:
            if current:
                out.append(current)
            current = word
    if current:
        out.append(current)
    return out


def para(draw, xy, text, fnt, width, leading, color=INK):
    """Draw a wrapped paragraph; return the y just below it."""
    x, y = xy
    for line in split_lines(draw, text, fnt, width):
        draw.text((x, y), line, font=fnt, fill=color)
        y += leading
    return y


def headline_block(draw, x, y, width, kicker, head, head_size, body,
                   body_size, kicker_color=SCARLET):
    """A kicker, a wrapped headline and a wrapped body paragraph."""
    draw.text((x, y), kicker, font=SANS_XB(20), fill=kicker_color)
    y += 30
    y = para(draw, (x, y), head, SERIF_XB(head_size), width,
             head_size + 8)
    y += 6
    y = para(draw, (x, y), body, SANS(body_size), width, body_size + 8)
    return y


def radar(draw, cx, cy, r):
    """Concentric radar rings with a sweep and one blip."""
    for i in (3, 2, 1):
        rr = r * i // 3
        draw.ellipse((cx - rr, cy - rr, cx + rr, cy + rr),
                     outline=STEEL, width=2)
    draw.line((cx - r, cy, cx + r, cy), fill=STEEL, width=1)
    draw.line((cx, cy - r, cx, cy + r), fill=STEEL, width=1)
    draw.line((cx, cy, cx + int(r * 0.7), cy - int(r * 0.7)),
              fill=SCARLET, width=3)
    draw.ellipse((cx + int(r * 0.45) - 6, cy - int(r * 0.45) - 6,
                  cx + int(r * 0.45) + 6, cy - int(r * 0.45) + 6),
                 fill=SCARLET)
    draw.ellipse((cx - 4, cy - 4, cx + 4, cy + 4), fill=NAVY)


def paint():
    img = Image.new("RGB", CANVAS, NEWS)
    d = ImageDraw.Draw(img)

    # --- masthead ------------------------------------------------------
    d.rectangle((0, 0, 1024, 116), fill=NAVY)
    d.text((36, 26), "THE WORLD TODAY", font=SERIF_XB(58), fill=WHITE)
    d.text((700, 30), "TUESDAY", font=SANS_XB(30), fill=WHITE)
    d.text((700, 68), "24 NOVEMBER 2026", font=SANS_B(24),
           fill=(196, 205, 224))
    d.rectangle((0, 116, 1024, 124), fill=SCARLET)

    # --- lead story ----------------------------------------------------
    y = 148
    d.text((36, y), "LEAD  ·  EUROPE", font=SANS_XB(20), fill=SCARLET)
    y += 32
    y = para(d, (36, y), "NATO sends AWACS jets to Poland after missiles land",
             SERIF_XB(42), 640, 50)
    y += 10
    lead_body = ("The alliance will deploy an early-warning aircraft after "
                 "three Russian Kh-101 missiles landed in Poland on Friday, "
                 "a Polish deputy defence minister said on Monday. A "
                 "Russian drone also briefly entered Polish airspace.")
    y = para(d, (36, y), lead_body, SANS(23), 640, 31)
    radar(d, 852, 268, 92)
    d.text((760, 372), "AWACS to the eastern flank",
           font=SANS_B(17), fill=STEEL)

    # --- divider -------------------------------------------------------
    d.line((36, 448, 988, 448), fill=RULE, width=2)

    # --- two columns ---------------------------------------------------
    left = headline_block(
        d, 36, 470, 452,
        "WAR SPREADS  ·  LIBYA",
        "Ukraine sinks Russian warship in Libya",
        30,
        "Naval drones hit the corvette Merkury at Benghazi on Sunday, "
        "Kyiv says — the war spills beyond Europe. A Russian cargo ship "
        "was also struck in the Gulf of Finland.",
        21)
    headline_block(
        d, 536, 470, 452,
        "BUSINESS  ·  UNITED STATES",
        "Trump brings back Nvidia chief Huang",
        30,
        "The president says he struck a deal with Nvidia's board to "
        "reinstate Jensen Huang as CEO — a \u201cnational treasure\u201d and "
        "no security risk. Huang stepped down on 12 November.",
        21)

    # --- divider -------------------------------------------------------
    d.line((36, 724, 988, 724), fill=RULE, width=2)

    # --- Seoul strip ---------------------------------------------------
    d.rectangle((36, 742, 988, 856), fill=MIST)
    d.rectangle((36, 742, 46, 856), fill=SCARLET)
    d.text((66, 758), "ASIA  ·  TUESDAY", font=SANS_XB(19), fill=SCARLET)
    para(d, (66, 784), "Seoul alert as Russian jet enters its airspace",
         SERIF_XB(29), 890, 36)
    d.text((66, 824),
           "South Korea briefly warned Ulleung island at 07:52; the alert "
           "was lifted after three minutes.",
           font=SANS(19), fill=INK)

    # --- ticker --------------------------------------------------------
    d.rectangle((0, 884, 1024, 972), fill=NAVY)
    ticker = ("COP31 blame game begins  •  Indonesia factory fire: 24 dead, "
              "~30 missing  •  Wellington Test drawn: NZ 239/5 holds India  •  "
              "Alcaraz beats Zverev 6–2, 7–6(7) to win ATP Finals  •  Chess "
              "title match opens today in Geneva: Gukesh v Sindarov  •  EU "
              "proposes 22nd Russia sanctions package")
    para(d, (28, 896), ticker, SANS_B(19), 968, 27, color=WHITE)

    # --- footer --------------------------------------------------------
    d.text((36, 986),
           "Stories verified against Reuters, BusinessWorld, ESPNcricinfo, "
           "ATP Tour and FIDE  ·  Tuesday, 24 November 2026",
           font=SANS(15), fill=STEEL)
    return img


if __name__ == "__main__":
    paint().save("entry.png", optimize=True)
    print("wrote entry.png")
