import unittest

from htmlnode import HTMLNode


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
        

if __name__ == "__main__":
    unittest.main()