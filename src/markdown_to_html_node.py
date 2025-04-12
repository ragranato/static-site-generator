from textnode import *
from htmlnode import *
from blocktype import *
import markdown_to_blocks

def text_to_children(text):
    pass

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    parent_html = ParentNode('div')
    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.CODE:
            code_block = TextNode(block, block_type)
            block_html = text_node_to_html_node(code_block)
            children.append(block_html)
        else:
            block_html = text_to_children(block)
            children.append(block_html)

    parent_html.children = children
    return parent_html