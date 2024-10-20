import subprocess
import os

def svg_to_plain_svg(input_svg_path, output_svg_path):
    """Converts an SVG file to Plain SVG using Inkscape."""
    """Converts all shapes in an SVG file to paths using Inkscape."""
    
    # Check if the input file exists
    if not os.path.exists(input_svg_path):
        raise FileNotFoundError(f"The file {input_svg_path} does not exist.")
    
    # Prepare the Inkscape command to convert shapes to paths
    command = [
        'inkscape',
        input_svg_path,
        '--export-type=svg',
        '--export-filename=' + output_svg_path,
        '--export-area-drawing',  # Export only the drawing area
        '--export-plain-svg',      # Option to export as plain SVG
        '--actions=object-to-path;select-all',         # Convert all objects to paths
    ]
    
    # Execute the command
    try:
        subprocess.run(command, check=True)
        print(f"Converted '{input_svg_path}' to paths and saved as '{output_svg_path}'.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

# Example usage
#svg_to_plain_svg('input.svg', 'output_plain.svg')

