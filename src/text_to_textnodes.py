from splitnodes import *
from splitnodesdelimiter import *

def text_to_textnodes(text):    
    delimiters = [('**', TextType.BOLD), ('*', TextType.ITALIC), ('`', TextType.CODE), ]
    
    text_node = TextNode(text, TextType.TEXT)

    image_nodes = split_nodes_image([text_node])
    print("After image split:", image_nodes)

    image_link_nodes = split_nodes_link(image_nodes)
    print("After link split:", image_link_nodes)
    
    for delimiter, text_type in delimiters:
        image_link_nodes = split_nodes_delimiter(image_link_nodes, delimiter, text_type)              
               
        
    return image_link_nodes
