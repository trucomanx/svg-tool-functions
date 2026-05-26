#!/usr/bin/python3

import os
import json

from visual_linear_systems.pipeline import generate_visual_linear_system

out_dir="output"

seed=4

vars_keys = ["x", "y", "z"]
var_min=1
var_max=3

coef_min=-2
coef_max=2
coef_mode="expanded"

svg_dir = "../svgs"
dvars = {
    "x": os.path.join(svg_dir,"apple.svg"),
    "y": os.path.join(svg_dir,"orange.svg"),
    "z": os.path.join(svg_dir,"pera.svg"),
    "+": os.path.join(svg_dir,"plus.svg"),
    "-": os.path.join(svg_dir,"minus.svg"),
    "=": os.path.join(svg_dir,"equal.svg"),
    "0": os.path.join(svg_dir,"0.svg"),
    "1": os.path.join(svg_dir,"1.svg"),
    "2": os.path.join(svg_dir,"2.svg"),
    "3": os.path.join(svg_dir,"3.svg"),
    "4": os.path.join(svg_dir,"4.svg"),
    "5": os.path.join(svg_dir,"5.svg"),
    "6": os.path.join(svg_dir,"6.svg"),
    "7": os.path.join(svg_dir,"7.svg"),
    "8": os.path.join(svg_dir,"8.svg"),
    "9": os.path.join(svg_dir,"9.svg"),
    "?": os.path.join(svg_dir,"box.svg"),
    "void": os.path.join(svg_dir,"void.svg")
}

res = generate_visual_linear_system(out_dir,
                                    vars_keys,
                                    dvars,
                                    var_min,
                                    var_max,
                                    coef_min,
                                    coef_max,
                                    coef_mode,
                                    seed
                                    )

print(json.dumps(res, indent=2))
