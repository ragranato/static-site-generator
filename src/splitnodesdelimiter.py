from textnode import *
from htmlnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
      
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue  # Skip further processing

        text = node.text
        i = 0  # Initialize `i`

        while i < len(text):
            start = text.find(delimiter, i)
            if start == -1:
                # If no start delimiter, add remaining text as a normal text node
                new_nodes.append(TextNode(text[i:], TextType.TEXT))
                break

            # Add text before the first delimiter
            if start > i:
                new_nodes.append(TextNode(text[i:start], TextType.TEXT))

            end = text.find(delimiter, start + len(delimiter))
            if end == -1:
                raise ValueError("Unmatched delimiter found in text.")

            # Add the node text for the delimited text
            new_nodes.append(TextNode(text[start + len(delimiter):end], text_type))

            # Continue searching after the end delimiter
            i = end + len(delimiter)
            
    return new_nodes

                        



                

    
    
    