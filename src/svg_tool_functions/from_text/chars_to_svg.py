#!/usr/bin/python3

from svg_tool_functions.from_svgpath import get_dimensions

import svgwrite

def chars_to_svg(input_text, dvars, out_path,width=30, font_size=30, h_spacing=10, v_spacing=50,font_family='Arial'):
    """
    Generates an SVG file containing images and text based on the input text.

    Args:
        input_text (str): The input string containing text and variable characters.
        dvars (dict): A dictionary mapping variable characters to their corresponding SVG image paths.
        out_path (str): Output path.
        width (int, optional): The width of the SVG images. Defaults to 30.
        font_size (int, optional): The font size for the text. Defaults to 30.
        h_spacing (int, optional): Horizontal spacing between characters/images. Defaults to 10.
        v_spacing (int, optional): Vertical spacing between lines of text. Defaults to 50.
        font_family (str, optional): The font family for text. Defaults to 'Arial'.

    Returns:
        tuple: A tuple containing the maximum width and total height of the generated SVG.

    This function works by:
    1. Splitting the input text into lines and calculating the total width and height required for the SVG.
    2. Iterating through each character in the input text:
        - If the character is a variable present in `dvars`, it retrieves the corresponding SVG dimensions and inserts the image into the SVG.
        - If the character is not a variable, it inserts the character as text.
    3. The final SVG is saved as out_path.
    """
    # Cria o arquivo SVG
    lines = input_text.split("\n")
    number_of_lines = len(lines)  # Número de linhas
    max_width = 0  # Para calcular a largura total
    max_height = font_size
    # Calcula a largura total com base nas variáveis
    for line in lines:
        line_width = 0
        for char in line:
            if char in dvars:
                # Obtém as dimensões da imagem correspondente
                svg_width, svg_height = get_dimensions(dvars[char])
                aspect_ratio = svg_height / svg_width
                height = int(width * aspect_ratio)
                max_height = max(height,max_height)
                
                line_width += width + h_spacing  # Largura da imagem e espaçamento
            else:
                line_width += font_size*0.61 + h_spacing  # Apenas espaçamento para caracteres que não são variáveis
        max_width = max(max_width, line_width)  # Atualiza a largura máxima

    # Calcula a altura total
    total_height = max_height+(number_of_lines-1) * v_spacing #+ 0.5*font_size

    # Define o tamanho da área de desenho do SVG
    dwg = svgwrite.Drawing(out_path, profile='tiny', size=(max_width, total_height))

    x_offset, y_offset = 0, 0

    # Posições iniciais para os objetos
    x_pos, y_pos = x_offset, y_offset 

    # Substitui as variáveis no input_text por imagens
    for n,line in enumerate(lines):
        # Itera sobre os caracteres do texto da equação
        for char in line:
            if char in dvars:
                # Obtém as dimensões da imagem correspondente
                svg_width, svg_height = get_dimensions(dvars[char])
                aspect_ratio = svg_height / svg_width
                height = int(width * aspect_ratio)  # Ajusta a altura com base na largura fornecida
                # Insere a imagem correspondente
                if n==0:
                    dwg.add(dwg.image(dvars[char], insert=(x_pos, y_pos+max_height-height), size=(width, height)))
                else:
                    dwg.add(dwg.image(dvars[char], insert=(x_pos, y_pos+v_spacing-height), size=(width, height)))
                x_pos += width + h_spacing  # Move a posição para a direita após inserir a imagem
            else:
                # Insere o caractere como texto (números ou operadores)
                if n==0:
                    dwg.add(dwg.text(char, insert=(x_pos, y_pos + max_height), font_size=str(font_size) + "px", font_family=font_family))
                else:
                    dwg.add(dwg.text(char, insert=(x_pos, y_pos + v_spacing), font_size=str(font_size) + "px", font_family=font_family))
                x_pos += font_size*0.61 + h_spacing  # Move a posição para a direita após inserir o texto
        
        # Avança para a próxima linha
        if n==0:
            y_pos += max_height
        else:
            y_pos += v_spacing
        x_pos = x_offset  # Reinicia a posição x para a próxima linha

    # Salva o SVG
    dwg.save()
    return (max_width, total_height)
