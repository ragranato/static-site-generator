

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):        
        result = ''
        for key, value in self.props.items():
            result += f'{key}="{value}" '
        return result.rstrip()

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
            pass