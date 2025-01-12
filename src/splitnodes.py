from textnode import *
from htmlnode import *
from extract_markdown import *
import re

def split_nodes_image(nodes):
    new_nodes = []
      
    for node in nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue  # Skip further processing

        text = node.text
        start_index = 0
        start_char = '!'
        end_char = ')'
        while True:
            start_index = text.find(start_char, start_index)
            if start_index == -1:
                new_nodes.append(TextNode(text, TextType.TEXT))
                break
            end_index = text.find(end_char, start_index + 1)
            if end_index == -1:
                new_nodes.append(TextNode(text, TextType.TEXT))
                break
            if len(text[:start_index]) != 0:
                new_nodes.append(TextNode(text[:start_index], TextType.TEXT))
                
            image_extract = extract_markdown_images(text[start_index:end_index])
            if image_extract:
                new_nodes.append(TextNode(image_extract[0], TextType.IMAGE, url=image_extract[1]))
            
            text = text[end_index+1:]
            # start_index = end_index + 1
            

    return new_nodes

def split_node_link(nodes):
    pass