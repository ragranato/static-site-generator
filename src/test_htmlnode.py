import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(tag='p', value="This is a tag node", children=None)
        node2 = HTMLNode(tag='p', value="This is a tag node", children=None)
        self.assertNotEqual(node, node2)

    def test_eq2_tag(self):
        node = HTMLNode(tag='p', value="This is a tag node", children=None)
        node2 = HTMLNode(tag='h1', value="This is a tag node", children=None)
        self.assertNotEqual(node, node2)

    def test_eq3_url_none(self):
        node = HTMLNode(tag='p', value="This is a tag node", children=None)        
        self.assertIsInstance(node, HTMLNode)

class TestLeafNode(unittest.TestCase):
    def test_novalue(self):
        node = LeafNode(tag='p', value=None)
        self.assertRaises(ValueError)
    def test_isinstance(self):
        node = LeafNode(tag='p', value='this is a paragraph')
        self.assertIsInstance(node, LeafNode)

class TestParentNode(unittest.TestCase):
    def test_no_children(self):
        node = ParentNode(tag='p', children=None)
        self.assertRaises(ValueError)
    def test_isinstance(self):
        node = ParentNode(tag='p', children=[LeafNode('p', value='hello world')])
        self.assertIsInstance(node, ParentNode)
    def test_no_tag(self):
        node = ParentNode(tag=None, children=[LeafNode('p', value='hello world')])
        self.assertRaises(ValueError)
    def test_tag(self):
        node = ParentNode(tag='div', children=[LeafNode('p', value='hello world')])
        self.assertEqual(node.tag, 'div')
    def test_isinstance_children(self):
        node = ParentNode(tag='p', children=[LeafNode('p', value='hello world')])
        self.assertIsInstance(node.children, list)

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_isinstance(self):
        text_node = TextNode(text='testing', text_type=TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertIsInstance(html_node, LeafNode)
    def test_Exception(self):        
        invalid_node = TextNode("testing", "not_a_valid_type")
        with self.assertRaises(AttributeError):
            text_node_to_html_node(invalid_node)
if __name__ == "__main__":
    unittest.main()