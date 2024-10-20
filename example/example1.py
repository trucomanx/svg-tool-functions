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



stf.from_filepath.convert_to_eps('output.svg', 'output.eps')    
