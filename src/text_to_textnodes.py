from splitnodes import *
from splitnodesdelimiter import *

def text_to_textnodes(text):
    new_nodes = []
    delimiters = [('**', TextType.BOLD), ('*', TextType.ITALIC), ('`', TextType.CODE), ]
    
    text_node = TextNode(text, TextType.TEXT)
    
    image_link_nodes = split_nodes_link(split_nodes_image([text_node]))

    for d in delimiters:
        temp_list = image_link_nodes
        node_list = []
        for node in image_link_nodes:
            text_temp = split_nodes_delimiter([node], d[0], d[1])
            node_list += text_temp        
        new_nodes += node_list
    return new_nodes

print(text_to_textnodes('This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)'))