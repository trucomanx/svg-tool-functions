#!/usr/bin/python3

import os
import json

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
                                    coef_mode="expanded",
                                    seed=4,
                                    prename="linear_system",
                                    elem_width=100,
                                    line_spacing=40
                                    ):
    os.makedirs(out_dir, exist_ok=True)

    vars_dict = generate_integer_vars(  vars_keys, 
                                        var_min, 
                                        var_max, 
                                        seed=seed)

    res = generate_integer_system(  vars_dict, 
                                    coef_min, 
                                    coef_max, 
                                    seed=seed)

    seqs = transfor_system_to_format_1( res, 
                                        coef_mode, 
                                        add_unknowns=False)

    filename_linsys   = f"{prename}_{seed}.svg"
    filename_unknowns = f"{prename}_{seed}_unknowns.svg"
    filename_solution = f"{prename}_{seed}_solution.svg"
    
    path_linsys   = os.path.join(out_dir, filename_linsys)
    path_unknowns = os.path.join(out_dir, filename_unknowns)
    path_solution = os.path.join(out_dir, filename_solution)
    
    ####################
    # SAVE LINEAR SYSTEM
    ####################
    
    build_svg_grid( dvars,
                    seqs,
                    path_linsys,
                    elem_width,
                    line_spacing  )

    ###############
    # SAVE UNKNOWNS
    ###############
    
    seq = []
    for i, var in enumerate(vars_keys):
        seq.extend([var, "=", "?"])
        if i < len(vars_keys) - 1:
            seq.append("void")
     
    build_svg_grid( dvars,
                    [seq],
                    path_unknowns,
                    elem_width,
                    line_spacing )

    ###############
    # SAVE SOLUTION
    ###############
    
    seq = []
    for i, var in enumerate(vars_keys):
        seq.extend([var, "=", str(vars_dict[var])])
        if i < len(vars_keys) - 1:
            seq.append("void")
     
    build_svg_grid( dvars,
                    [seq],
                    path_solution,
                    elem_width,
                    line_spacing )


    return  {
            "vars_dict": vars_dict,
            "filename_linsys": filename_linsys,
            "filename_unknowns": filename_unknowns,
            "filename_solution": filename_solution
            }

################################################################################


out_dir="output"

seed=4

vars_keys = ["x", "y", "z"]
var_min=1
var_max=3

coef_min=-2
coef_max=2
coef_mode="expanded"

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
