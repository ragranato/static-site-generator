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
        
        while len(text) != 0:            
            image_extract = extract_markdown_images(text)
            if image_extract:
                for item in image_extract:
                    alt_text, url = item
                    match_section = f"![{alt_text}]({url})"
                    sections = text.split(match_section, 1)
                    if sections[0]:
                        new_nodes.append(TextNode(sections[0], TextType.TEXT))
                        new_nodes.append(TextNode(alt_text, TextType.IMAGE, url=url))
                        text = sections[1]
                if len(text) != 0:
                    new_nodes.append(TextNode(text, TextType.TEXT))
            else:
                new_nodes.append(node)
                break
    return new_nodes

def split_nodes_link(nodes):
    new_nodes = []
      
    for node in nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue  # Skip further processing

        text = node.text
        
        while len(text) != 0:            
            link_extract = extract_markdown_links(text)
            if link_extract:
                for item in link_extract:
                    link_text, url = item
                    match_section = f"[{link_text}]({url})"
                    sections = text.split(match_section, 1)
                    if sections[0]:
                        new_nodes.append(TextNode(sections[0], TextType.TEXT))
                        new_nodes.append(TextNode(link_text, TextType.LINK, url=url))
                        text = sections[1]
                if len(text) != 0:
                    new_nodes.append(TextNode(text, TextType.TEXT))
            else:
                new_nodes.append(node)
                break
    return new_nodes