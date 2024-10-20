import sys
sys.path.append('../src')

import svg_tool_functions as stf


input_text = "2x+y=5\ny+x=3"
dvars = {
    "x": "apple.svg",  
    "y": "orange.svg"
}


max_width, total_height = stf.from_text.chars_to_svg(   input_text, 
                                                        dvars, 
                                                        'output.svg',
                                                        width=40, 
                                                        font_size=40, 
                                                        h_spacing=0, 
                                                        v_spacing=60)

print(max_width, total_height)

stf.from_svgpath.svg_to_svg('output.svg', 'output.vector.svg')
stf.from_svgpath.svg_to_plain_svg('output.vector.svg','output.plain.svg')

stf.from_svgpath.binary_convert_to_eps('output.plain.svg', 'output.binary.eps')
#stf.from_svgpath.inkscape_convert_to('output.svg', 'output.inkscape.eps')
#stf.from_svgpath.rsvg_convert_to_eps('output.svg', 'output.rsvg.eps')
