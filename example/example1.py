#!/usr/bin/python3

from visual_linear_systems.integuer_equation import generate_integer_system
from visual_linear_systems.integuer_equation import generate_integer_vars
from visual_linear_systems.svg_grid          import build_svg_grid
from visual_linear_systems.system_formatter  import transfor_system_to_format_1

def generate_visual_linear_system(  out_dir,
                                    vars_keys,
                                    dvars,
                                    var_min=1,
                                    var_max=3,
                                    coef_min=-2,
                                    coef_max=2,
                                    seed=4
                                    ):

    vars_dict = generate_integer_vars(  vars_keys, 
                                        var_min, 
                                        var_max, 
                                        seed=seed)

    res = generate_integer_system(  vars_dict, 
                                    coef_min, 
                                    coef_max, 
                                    seed=seed)

    seqs = transfor_system_to_format_1( res, 
                                        coef_mode="expanded", 
                                        add_unknowns=False)

    build_svg_grid( dvars,
                    seqs,
                    "data_unknowns.svg",
                    elem_width=100,
                    line_spacing=40  )

    seq = []
    for i, var in enumerate(vars_keys):
        seq.extend([var, "=", "?"])
        if i < len(vars_keys) - 1:
            seq.append("void")
     
    build_svg_grid( dvars,
                    [seq],
                    "data_system.svg",
                    elem_width=100,
                    line_spacing=40  )

    print(vars_dict)
    return {"vars_dict": vars_dict}

################################################################################


out_dir="output"

seed=4

vars_keys = ["x", "y", "z"]
var_min=1
var_max=3

coef_min=-2
coef_max=2


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

generate_visual_linear_system(  vars_keys,
                                dvars,
                                var_min,
                                var_max,
                                coef_min,
                                coef_max,
                                seed
                                )
