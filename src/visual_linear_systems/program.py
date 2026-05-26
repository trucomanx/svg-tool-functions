import os
import sys
import argparse

import visual_linear_systems.about as about
from visual_linear_systems.modules.wabout import show_about

# ----------------------------------------------------------
# Utility Functions
# ----------------------------------------------------------
def generic_function1(output_dir):
    print("Some code here")
    print(f"Output directory: {output_dir}")


# ----------------------------------------------------------
# Main CLI
# ----------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        prog=about.__program_name__,
        description=about.__description__
    )

    parser.add_argument(
        "--about",
        action="store_true",
        help="Show 'about' information and exit"
    )

    parser.add_argument(
        "--output-dir",
        type=str,
        help="The output directory"
    )

    args = parser.parse_args()

    # ---------------- Actions ----------------


    if args.about:
        show_about()
        return

    # -------------------------------------------------
    # Main Program Logic
    # -------------------------------------------------

    generic_function1(args.output_dir)


if __name__ == "__main__":
    main()

