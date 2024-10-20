import os
import base64
from lxml import etree
import svgwrite

# Define a função para converter diferentes unidades para pixels
def convert_to_pixels(value, unit):
    unit_conversions = {
        'px': 1,
        'in': 96,  # 1 inch = 96 pixels
        'mm': 3.7795275591,  # 1 mm = 3.7795275591 pixels
        'cm': 37.795275591,  # 1 cm = 37.795275591 pixels
        'pt': 1.3333333333,  # 1 pt = 1.3333333333 pixels
        'pc': 16  # 1 pica = 16 pixels
    }
    
    # Se não houver unidade, assuma pixels
    if unit == '':
        unit = 'px'
    
    if unit in unit_conversions:
        return float(value) * unit_conversions[unit]
    else:
        raise ValueError(f"Unidade desconhecida: {unit}")

def parse_dimension(dimension):
    """Parse a dimension string like '100px', '50mm' and return a value in pixels."""
    import re
    match = re.match(r"([\d.]+)([a-zA-Z%]*)", dimension)
    if match:
        value, unit = match.groups()
        unit = unit if unit else 'px'  # Assume pixels if no unit is provided
        return convert_to_pixels(float(value), unit)
    else:
        raise ValueError(f"Dimensão inválida: {dimension}")

def get_svg_dimensions_from_content(svg_content):
    """Extract the width and height from the given SVG content string, converting to pixels."""
    svg_tree = etree.fromstring(svg_content.encode('utf-8'))
    
    # Obter a largura e altura do SVG, lidar com unidades
    width = svg_tree.get('width', '1px')
    height = svg_tree.get('height', '1px')
    
    print(width,height)

    # Parse e converta largura e altura para pixels
    width_in_pixels = parse_dimension(width)
    height_in_pixels = parse_dimension(height)
    
    print(width_in_pixels,height_in_pixels)

    return width_in_pixels, height_in_pixels

def get_svg_content(file_path):
    """Read and return the content of an SVG file."""
    with open(file_path, 'r') as file:
        return file.read()

def convert_svg_to_eps(input_svg_path, output_eps_path):
    """Convert an SVG file to EPS, embedding SVG or PNG images."""
    
    # Parse the SVG
    with open(input_svg_path, 'r') as svg_file:
        svg_content = svg_file.read()

    # Parse the SVG content to modify it
    svg_tree = etree.fromstring(svg_content.encode('utf-8'))
    
    # Find all <image> elements in the SVG
    for image in svg_tree.findall('.//{http://www.w3.org/2000/svg}image'):
        href = image.get('{http://www.w3.org/1999/xlink}href')

        if href:
            # Determine file extension
            _, ext = os.path.splitext(href)
            ext = ext.lower()

            if ext == '.svg':
                print("")
                print(href)
                # Get the SVG content and embed it
                embedded_svg_content = get_svg_content(href)
                embedded_width, embedded_height = get_svg_dimensions_from_content(embedded_svg_content)
                
                
                # Extract original <image> attributes for positioning and sizing
                x = parse_dimension(image.get('x', '0'))
                y = parse_dimension(image.get('y', '0'))
                width = parse_dimension(image.get('width'))
                height = parse_dimension(image.get('height'))
                print("x",x,"y",y,"width",width,"height",height)

                # Calculate scaling factors
                scale_x = width / embedded_width
                scale_y = height / embedded_height
                print("scale_x",scale_x,"scale_y",scale_x)

                # Wrap the embedded SVG content in a <g> element with translation and scaling
                g = etree.Element('g')
                g.set('transform', f'translate({x},{y}) scale({scale_x},{scale_y})')

                # Add the embedded SVG content to the <g> element, adjusting namespaces if necessary
                for element in etree.fromstring(embedded_svg_content.encode('utf-8')):
                    g.append(element)

                # Replace the original <image> element with the <g> containing the embedded SVG
                image.getparent().replace(image, g)

            elif ext in ['.png', '.jpg', '.jpeg']:
                # If it's a PNG or JPEG, embed it as a base64 string
                with open(href, 'rb') as img_file:
                    img_data = base64.b64encode(img_file.read()).decode('utf-8')
                    image.set('{http://www.w3.org/1999/xlink}href', f"data:image/{ext[1: ]};base64,{img_data}")

    # Create a new SVG file to hold the modified content
    new_svg_content = etree.tostring(svg_tree, pretty_print=True).decode('utf-8')

    # Write the modified SVG content to a new file
    temp_svg_path = 'temp_modified.svg'
    with open(temp_svg_path, 'w') as temp_svg_file:
        temp_svg_file.write(new_svg_content)

    # Now convert the modified SVG to EPS using your preferred method.
    # Example: Using CairoSVG (you'll need to install it)
    import cairosvg
    cairosvg.svg2eps(url=temp_svg_path, write_to=output_eps_path)

# Example usage:
convert_svg_to_eps('output.svg', 'output.svg.eps')

