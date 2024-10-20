
'''
import os


def convert_svg_to_eps(input_file, output_file):
    # Converte SVG para EPS usando rsvg-convert
    os.system(f'rsvg-convert -f eps -o {output_file} {input_file}')

# Exemplo de uso
convert_svg_to_eps('output.svg', 'output.svg.eps')
'''


import subprocess

def convert_svg_to_eps(input_file, output_file):
    # Converte SVG para EPS usando Inkscape
    subprocess.run(['inkscape',input_file, '--export-filename', output_file])

# Exemplo de uso
convert_svg_to_eps('output.svg', 'output.svg.eps')





