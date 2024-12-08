from enum import Enum, auto

class TextType(Enum):
    NORMAL = auto()
    BOLD = auto()
    ITALIC = auto()
    CODE = auto()
    LINKS = auto()
    IMAGES = auto()

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    def __eq__(self, node):
        if self.text == node.text and self.text_type == node.text_type and self.url == node.url:
            return True
        return False
    def __repr__(self):
        return f"TexNode({self.text}, {self.text_type}, {self.url})"

