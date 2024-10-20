#!/usr/bin/python3

import subprocess

def inkscape_convert_to(input_file, output_file):
    # Converte SVG para EPS usando Inkscape
    subprocess.run(['inkscape',input_file, '--export-filename', output_file])

# Exemplo de uso
#inkscape_convert_to('output.svg', 'output.svg.eps')

