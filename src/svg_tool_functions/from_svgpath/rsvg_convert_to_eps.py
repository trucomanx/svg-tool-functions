

import os

def rsvg_convert_to_eps(input_file, output_file):
    # Converte SVG para EPS usando rsvg-convert
    os.system(f'rsvg-convert -f eps -o {output_file} {input_file}')

# Exemplo de uso
# rsvg_convert_to_eps('output.svg', 'output.svg.eps')







