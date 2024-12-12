from textnode import *
from htmlnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            text = node.text            
            start = text.find(delimiter)
            if start == -1:
                new_nodes.append(node)
                
            else:
                end = text.find(delimiter, start + len(delimiter))
           
                if end == -1:
                    raise Exception("Invalid markdown syntax")
                if len(text[start+len(delimiter):end]) == 0:
                    raise Exception("Invalid markdown syntax")
                if start > 0:
                    new_nodes.append(TextNode(text[:start], TextType.TEXT))  
                new_nodes.append(TextNode(text[start+len(delimiter):end], text_type))
                remaining = text[end + len(delimiter):]
                if remaining:
                    new_nodes.append(TextNode(remaining, TextType.TEXT))
    return new_nodes
                    
print(split_nodes_delimiter([TextNode("`code` hello `code` world", TextType.TEXT)], "`", TextType.CODE) )              
                

    
    
    