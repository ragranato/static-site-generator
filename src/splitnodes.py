from textnode import *
from htmlnode import *
import re

def split_node_image(nodes):
    new_nodes = []
      
    for node in old_nodes:
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
                break
            end_index = text.find(end_char, start_index + 1)
            if end_index == -1:
                break
            if len(text[:start_index]) != 0:
                new_nodes.append(TextNode(text[:start_index], TextType.TEXT))
                
            alt = ''
            match_alt = re.search(r"\[(.*?)\]", text[start_index+2:end_index])
            if match_alt:
                alt = match_alt.group(1)            
            url = ''
            match_url = re.search(r"\((.*?)\)", text[start_index+1:end_index])
            if match_url:
                url = match_url.group(1)

            new_nodes.append(TextNode(alt, TextType.IMAGE, url=url))
            text = text[end_index+1:]
            # start_index = end_index + 1
    return new_nodes

def split_node_link(nodes):
    pass