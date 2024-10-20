#!/usr/bin/python3

import xml.etree.ElementTree as ET


def get_dimensions(svg_path):
    """
    Obtém as dimensões de um arquivo SVG.

    Parâmetros:
    svg_path (str): O caminho do arquivo SVG.

    Retorna:
    tuple: Uma tupla contendo a largura e altura do SVG.
    """
    tree = ET.parse(svg_path)
    root = tree.getroot()

    # Verifica se o SVG tem o atributo viewBox
    viewBox = root.attrib.get('viewBox')
    if viewBox:
        # Se viewBox estiver presente, utiliza suas dimensões
        viewBox_values = list(map(float, viewBox.split()))
        width = viewBox_values[2]  # Largura do viewBox
        height = viewBox_values[3]  # Altura do viewBox
    else:
        # Se viewBox não estiver presente, utiliza atributos width e height
        width = float(root.attrib.get('width', 0))
        height = float(root.attrib.get('height', 0))

    return width, height
