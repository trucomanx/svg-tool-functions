#!/usr/bin/python3

import xml.etree.ElementTree as ET
from copy import deepcopy
import re

def parse_svg_length(value):
    match = re.match(r"([0-9.+-eE]+)", value)
    if not match:
        raise ValueError(f"Valor SVG inválido: {value}")
    return float(match.group(1))


def get_svg_geometry(root):

    viewbox = root.get("viewBox")

    if viewbox:
        minx, miny, w, h = map(float, viewbox.split())
        return minx, miny, w, h

    width = root.get("width")
    height = root.get("height")

    if width and height:
        w = parse_svg_length(width)
        h = parse_svg_length(height)
        return 0, 0, w, h

    raise ValueError("SVG sem width/height ou viewBox")


def build_svg_grid(
        dvars,
        seqs,
        output_file,
        elem_width=100,
        line_spacing=20
    ):

    svg_ns = "http://www.w3.org/2000/svg"
    ET.register_namespace("", svg_ns)

    loaded = {}

    max_elem_height = 0

    # =========================
    # CARREGA SVGS
    # =========================

    for key, path in dvars.items():

        tree = ET.parse(path)
        root = tree.getroot()

        minx, miny, w, h = get_svg_geometry(root)

        scale = elem_width / w

        final_h = h * scale

        max_elem_height = max(max_elem_height, final_h)

        loaded[key] = {
            "root": root,
            "minx": minx,
            "miny": miny,
            "scale": scale,
            "final_h": final_h
        }

    # =========================
    # TAMANHO TOTAL
    # =========================

    max_cols = max(len(line) for line in seqs)

    total_width = max_cols * elem_width

    total_height = (
        len(seqs) * max_elem_height
        + (len(seqs) - 1) * line_spacing
    )

    out_root = ET.Element(
        "svg",
        width=str(total_width),
        height=str(total_height),
        viewBox=f"0 0 {total_width} {total_height}"
    )

    # =========================
    # DESENHA LINHAS
    # =========================

    for row_idx, seq in enumerate(seqs):

        row_width = len(seq) * elem_width

        # alinhamento à direita
        start_x = total_width - row_width

        y_base = row_idx * (max_elem_height + line_spacing)

        x_cursor = start_x

        for key in seq:

            item = loaded[key]

            y_offset = (
                y_base
                + (max_elem_height - item["final_h"]) / 2
            )

            g = ET.Element(
                "g",
                transform=(
                    f"translate({x_cursor},{y_offset}) "
                    f"scale({item['scale']}) "
                    f"translate({-item['minx']},{-item['miny']})"
                )
            )

            for child in item["root"]:
                g.append(deepcopy(child))

            out_root.append(g)

            x_cursor += elem_width

    ET.ElementTree(out_root).write(output_file)


if __name__ == "__main__":

    dvars = {
        "x": "../svgs/apple.svg",
        "y": "../svgs/orange.svg",
        "+": "../svgs/plus.svg",
        "-": "../svgs/minus.svg",
        "=": "../svgs/equal.svg",
        "0": "../svgs/0.svg",
        "1": "../svgs/1.svg",
        "2": "../svgs/2.svg",
        "3": "../svgs/3.svg",
        "4": "../svgs/4.svg",
        "5": "../svgs/5.svg",
        "6": "../svgs/6.svg",
        "7": "../svgs/7.svg",
        "8": "../svgs/8.svg",
        "9": "../svgs/9.svg",
        "?": "../svgs/unknown.svg"
    }

    seqs = [

        ["x", "+", "x", "+", "y", "=", "1", "0"],
        ["x", "-", "y", "=", "3"],
        ["x", "=", "?"],
        ["y", "=", "?"]
    ]

    build_svg_grid(
        dvars,
        seqs,
        "output.svg",
        elem_width=100,
        line_spacing=40
    )
