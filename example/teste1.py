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


def generate_svg(dvars, seq, output_file, elem_width=100):

    svg_ns = "http://www.w3.org/2000/svg"
    ET.register_namespace("", svg_ns)

    loaded = {}

    max_height = 0

    # carrega svgs
    for key, path in dvars.items():

        tree = ET.parse(path)
        root = tree.getroot()

        minx, miny, w, h = get_svg_geometry(root)

        scale = elem_width / w

        final_h = h * scale

        max_height = max(max_height, final_h)

        loaded[key] = {
            "root": root,
            "minx": minx,
            "miny": miny,
            "w": w,
            "h": h,
            "scale": scale,
            "final_h": final_h
        }

    total_width = len(seq) * elem_width

    out_root = ET.Element(
        "svg",
        width=str(total_width),
        height=str(max_height),
        viewBox=f"0 0 {total_width} {max_height}"
    )

    x_cursor = 0

    for key in seq:

        item = loaded[key]

        scale = item["scale"]

        # centraliza verticalmente
        y_offset = (max_height - item["final_h"]) / 2

        g = ET.Element(
            "g",
            transform=(
                f"translate({x_cursor},{y_offset}) "
                f"scale({scale}) "
                f"translate({-item['minx']},{-item['miny']})"
            )
        )

        for child in item["root"]:
            g.append(deepcopy(child))

        out_root.append(g)

        x_cursor += elem_width

    ET.ElementTree(out_root).write(output_file)


# exemplo
dvars = {
    "x": "svgs/apple.svg",
    "y": "svgs/orange.svg",
    "+": "svgs/plus.svg",
    "=": "svgs/equal.svg",
    "1": "svgs/1.svg",
    "2": "svgs/2.svg"
}

seq = ["x", "+", "x", "+", "x", "+", "y", "=", "1", "2"]

generate_svg(dvars, seq, "output.svg", elem_width=100)
