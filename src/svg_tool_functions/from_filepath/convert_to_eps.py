#!/usr/bin/python3

import os
from lxml import etree
import cairosvg
import base64


def convert_to_eps(svg_file, output_eps_file):
    """
    Converts an SVG file with referenced images (including SVGs and PNGs) to an EPS file.

    Args:
        svg_file (str): Path to the input SVG file.
        output_eps_file (str): Path where the output EPS file will be saved.
    """
    # Check if the SVG file exists
    if not os.path.exists(svg_file):
        raise FileNotFoundError(f"The SVG file {svg_file} does not exist.")

    # Load the SVG file in binary mode
    with open(svg_file, 'rb') as file:
        svg_content = file.read()

    # Parse the SVG content
    svg_tree = etree.fromstring(svg_content)

    # Replace image references with base64 data if necessary
    for image in svg_tree.findall('.//{http://www.w3.org/2000/svg}image'):
        href = image.get('{http://www.w3.org/1999/xlink}href')
        if href:
            # Check if the image path is relative and convert to an absolute path
            absolute_path = os.path.abspath(os.path.join(os.path.dirname(svg_file), href))
            if os.path.exists(absolute_path):
                # Read the image content based on its type
                with open(absolute_path, 'rb') as img_file:
                    img_data = img_file.read()
                
                # Determine the image type and encode appropriately
                if href.lower().endswith('.svg'):
                    img_data_str = img_data.decode('utf-8')  # Decode for SVG
                    encoded_image = base64.b64encode(img_data_str.encode('utf-8')).decode('utf-8')
                    # Create a data URI for the SVG image
                    image.set('{http://www.w3.org/1999/xlink}href', f'data:image/svg+xml;base64,{encoded_image}')
                elif href.lower().endswith(('.png', '.jpg', '.jpeg')):
                    encoded_image = base64.b64encode(img_data).decode('utf-8')
                    # Create a data URI for the PNG image
                    image.set('{http://www.w3.org/1999/xlink}href', f'data:image/png;base64,{encoded_image}')
                else:
                    print(f"Unsupported image format for {href}. Skipping.")

    # Create a modified temporary SVG file
    modified_svg_file = 'temp_modified.svg'
    with open(modified_svg_file, 'wb') as file:
        file.write(etree.tostring(svg_tree, xml_declaration=True, encoding='UTF-8'))

    # Convert the modified SVG to EPS using cairosvg
    cairosvg.svg2eps(url=modified_svg_file, write_to=output_eps_file)

    # Remove the temporary SVG file
    os.remove(modified_svg_file)

    print(f"Converted {svg_file} to {output_eps_file}")
    

