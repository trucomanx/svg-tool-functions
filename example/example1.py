#!/usr/bin/python3

from visual_linear_systems.integuer_equation import generate_integer_system
from visual_linear_systems.svg_grid          import build_svg_grid
from visual_linear_systems.system_formatter  import transfor_system_to_format_1

seed=2

vars_dict = {"x": 2, "y": 1, "z": 3}



dvars = {
    "x": "../svgs/apple.svg",
    "y": "../svgs/orange.svg",
    "z": "../svgs/pera.svg",
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
    "?": "../svgs/box.svg",
    "void": "../svgs/void.svg"
}

res = generate_integer_system(vars_dict, -2, 2, seed=seed)

seqs = transfor_system_to_format_1( res, 
                                    coef_mode="expanded", 
                                    add_unknowns=False)

build_svg_grid( dvars,
                seqs,
                "data_unknowns.svg",
                elem_width=100,
                line_spacing=40  )
                
build_svg_grid( dvars,
                [["x","=","?","void","y","=","?","void","z","=","?"]],
                "data_system.svg",
                elem_width=100,
                line_spacing=40  )
