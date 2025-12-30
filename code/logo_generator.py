#!/usr/bin/env python3
"""
Parametric flat logo generator (FENG, 180° rotatable concept-friendly)
Outputs SVG (vector) and optionally PNG preview.

Dependencies:
  pip install svgwrite
Optional PNG export:
  pip install cairosvg
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import List, Tuple, Optional
import argparse

import svgwrite


Point = Tuple[float, float]


@dataclass(frozen=True)
class LogoParams:
    # Overall geometry
    height: float = 200.0               # Canvas height (px)
    stroke: float = 20.0                # Stroke width (px)
    margin: float = 28.0                # Outer padding (px)

    # Letter widths (key constraint)
    letter_w: float = 280.0             # F, E, G width
    n_ratio: float = 0.5                # N width = letter_w * n_ratio

    # Spacing between letters (prefer multiples of stroke for "font-like" rhythm)
    gap_ratio: float = 1.8              # gap = gap_ratio * stroke

    # Flat/modern look
    stroke_color: str = "#000000"
    cap: str = "round"                  # round / square / butt
    join: str = "round"                 # round / bevel / miter

    # Internal layout (relative, keeps proportions stable)
    y_top_ratio: float = 0.20           # y positions for F/E bars
    y_mid_ratio: float = 0.50
    y_bot_ratio: float = 0.80

    # F bar lengths as ratio of letter width (top/mid/bot)
    f_top: float = 1.00
    f_mid: float = 0.88
    f_bot: float = 0.46

    # E bar lengths (top/bot short; mid long)
    e_short: float = 0.38               # top & bottom
    e_mid: float = 1.00                 # middle is full width

    # G construction (two-stroke: outer + inner counter)
    g_outer_inset_ratio: float = 0.10   # padding inside G box
    g_hook_len_ratio: float = 0.32      # "hook" length suggesting G
    g_counter_ratio: float = 0.52       # inner square size relative to (usable) height


def _path_d(points: List[Point]) -> str:
    """M x y L ... path string."""
    if len(points) < 2:
        raise ValueError("Need at least 2 points for a path.")
    d = [f"M {points[0][0]:.3f} {points[0][1]:.3f}"]
    for x, y in points[1:]:
        d.append(f"L {x:.3f} {y:.3f}")
    return " ".join(d)


def add_stroke(
    dwg: svgwrite.Drawing,
    points: List[Point],
    params: LogoParams,
    translate: Point = (0.0, 0.0),
) -> None:
    tx, ty = translate
    pts = [(x + tx, y + ty) for x, y in points]
    dwg.add(
        dwg.path(
            d=_path_d(pts),
            fill="none",
            stroke=params.stroke_color,
            stroke_width=params.stroke,
            stroke_linecap=params.cap,
            stroke_linejoin=params.join,
        )
    )


def add_rect_stroke(
    dwg: svgwrite.Drawing,
    x: float,
    y: float,
    w: float,
    h: float,
    params: LogoParams,
) -> None:
    """Rectangle as a stroke path (for consistent joins/caps)."""
    add_stroke(
        dwg,
        [(x, y), (x + w, y), (x + w, y + h), (x, y + h), (x, y)],
        params,
    )


def letter_F(dwg: svgwrite.Drawing, params: LogoParams, origin: Point, w: float, h: float) -> None:
    ox, oy = origin
    y1 = oy + params.y_top_ratio * h
    y2 = oy + params.y_mid_ratio * h
    y3 = oy + params.y_bot_ratio * h

    # Left aligned bars
    add_stroke(dwg, [(ox, y1), (ox + params.f_top * w, y1)], params)
    add_stroke(dwg, [(ox, y2), (ox + params.f_mid * w, y2)], params)
    add_stroke(dwg, [(ox, y3), (ox + params.f_bot * w, y3)], params)


def letter_E(dwg: svgwrite.Drawing, params: LogoParams, origin: Point, w: float, h: float) -> None:
    ox, oy = origin
    y1 = oy + params.y_top_ratio * h
    y2 = oy + params.y_mid_ratio * h
    y3 = oy + params.y_bot_ratio * h

    # Vertical spine
    add_stroke(dwg, [(ox, oy + params.y_top_ratio * h), (ox, oy + params.y_bot_ratio * h)], params)

    # Horizontals
    add_stroke(dwg, [(ox, y1), (ox + params.e_short * w, y1)], params)
    add_stroke(dwg, [(ox, y2), (ox + params.e_mid * w, y2)], params)
    add_stroke(dwg, [(ox, y3), (ox + params.e_short * w, y3)], params)


def letter_N_arch(dwg: svgwrite.Drawing, params: LogoParams, origin: Point, w: float, h: float) -> None:
    """
    Square arch/portal: like a Π shape (top + two verticals, bottom open).
    This is the "N" abstraction you described (and becomes part of I/K when rotated).
    """
    ox, oy = origin
    y_top = oy + params.y_top_ratio * h
    y_bot = oy + params.y_bot_ratio * h

    # Left vertical
    add_stroke(dwg, [(ox, y_bot), (ox, y_top)], params)
    # Top bar
    add_stroke(dwg, [(ox, y_top), (ox + w, y_top)], params)
    # Right vertical
    add_stroke(dwg, [(ox + w, y_top), (ox + w, y_bot)], params)


def letter_G_flat(dwg: svgwrite.Drawing, params: LogoParams, origin: Point, w: float, h: float) -> None:
    """
    Flat "lying G" built as two components:
      1) Outer stroke: a squared C/G-like path with a 'hook'
      2) Inner counter: a square outline

    This mirrors your sketch where the right side looks like a C-shape plus a square.
    """
    ox, oy = origin
    y_top = oy + params.y_top_ratio * h
    y_bot = oy + params.y_bot_ratio * h

    # Define an inner usable box to keep stroke away from edges a bit
    inset = params.g_outer_inset_ratio * w
    xL = ox + inset
    xR = ox + w - inset
    yT = y_top
    yB = y_bot

    # Outer "lying G": start top-left -> top-right -> down (short) -> left (hook) -> down -> bottom-right
    # Tuned for modern, readable silhouette with minimal complexity.
    drop = 0.42 * (yB - yT)                         # how far the right side drops before the hook
    hook_len = params.g_hook_len_ratio * (xR - xL)   # hook length back to the left
    hook_y = yT + drop

    outer = [
        (xL, yT),
        (xR, yT),
        (xR, hook_y),
        (xR - hook_len, hook_y),
        (xR - hook_len, yB),
        (xR, yB),
    ]
    add_stroke(dwg, outer, params)

    # Inner counter square (like your right-most square piece)
    usable_h = (yB - yT)
    counter = params.g_counter_ratio * usable_h
    # Place it toward the far right to feel like a "counter" of G
    cx = xR - counter
    cy = yT + 0.10 * usable_h
    add_rect_stroke(dwg, cx, cy, counter, counter, params)


def build_logo(params: LogoParams, out_svg: str, export_png: bool = False) -> None:
    wF = params.letter_w
    wE = params.letter_w
    wN = params.letter_w * params.n_ratio
    wG = params.letter_w

    gap = params.gap_ratio * params.stroke
    h = params.height
    # Letter box height inside margins
    box_h = h - 2 * params.margin

    total_w = (
        2 * params.margin
        + wF + gap
        + wE + gap
        + wN + gap
        + wG
    )

    dwg = svgwrite.Drawing(out_svg, size=(total_w, h))
    # Optional: set viewBox for responsive scaling in HTML/CSS
    dwg.viewbox(0, 0, total_w, h)

    # Origins (top-left of letter boxes)
    x = params.margin
    y = params.margin

    # Draw letters
    letter_F(dwg, params, (x, y), wF, box_h)
    x += wF + gap

    letter_E(dwg, params, (x, y), wE, box_h)
    x += wE + gap

    letter_N_arch(dwg, params, (x, y), wN, box_h)
    x += wN + gap

    letter_G_flat(dwg, params, (x, y), wG, box_h)

    dwg.save()
    print(f"Saved SVG: {out_svg}")

    if export_png:
        try:
            import cairosvg  # type: ignore
            out_png = out_svg.rsplit(".", 1)[0] + ".png"
            cairosvg.svg2png(url=out_svg, write_to=out_png, output_width=int(total_w * 2))
            print(f"Saved PNG: {out_png}")
        except Exception as e:
            print("PNG export skipped (install cairosvg?):", e)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Generate a flat parametric FENG logo (SVG + optional PNG).")
    p.add_argument("--out", default="logo.svg", help="Output SVG file path.")
    p.add_argument("--png", action="store_true", help="Also export PNG preview (requires cairosvg).")

    # Key knobs (enough to iterate quickly without editing code)
    p.add_argument("--height", type=float, default=200.0, help="Canvas height in px.")
    p.add_argument("--stroke", type=float, default=20.0, help="Stroke width in px.")
    p.add_argument("--letterw", type=float, default=280.0, help="Width of F/E/G modules in px.")
    p.add_argument("--nratio", type=float, default=0.5, help="N width ratio relative to letterw.")
    p.add_argument("--gapratio", type=float, default=1.8, help="Gap ratio relative to stroke.")
    return p.parse_args()


def main() -> None:
    a = parse_args()
    params = LogoParams(
        height=a.height,
        stroke=a.stroke,
        letter_w=a.letterw,
        n_ratio=a.nratio,
        gap_ratio=a.gapratio,
    )
    build_logo(params, out_svg=a.out, export_png=a.png)


if __name__ == "__main__":
    main()
