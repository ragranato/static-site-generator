from textnode import *

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):            
        if self.props:
            result = ''
            for key, value in self.props.items():
                result += f'{key}="{value}" '
            return result.rstrip()
        else:
            return ''

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value,  props=None):
        super().__init__(tag, value, props)
    
    def to_html(self):
        if not self.value:
            raise ValueError
        elif not self.tag:
            return f"{self.value}"
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError('No tag found')
        elif not self.children:
            raise ValueError('ParentNodes must have children')
        else:
            children = ''
            for child in self.children:                
                children = children + child.to_html()
            
            return f"<{self.tag}>{children}</{self.tag}>"

def text_node_to_html_node(text_node):    
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(value=text_node.text)
        case TextType.BOLD:
            return LeafNode(tag='b', value=text_node.text)
        case TextType.ITALIC:
            return LeafNode(tag='i', value=text_node.text)
        case TextType.CODE:
            return LeafNode(tag='code', value=text_node.text)
        case TextType.LINK:
            return LeafNode(tag='a', value=text_node.text, props= {'href': text_node.url})
        case TextType.IMAGE:
            return LeafNode(tag='img', value='', props={'src':text_node.url, 'alt':text_node.text})
        case _:
            raise AttributeError('Invalid Text_Type')

# text = TextNode('testing', TextType.IMAGE, 'www.widget.com')
# print(text_node_to_html_node(text))