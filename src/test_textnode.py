import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq2_url_eq(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.widget.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "www.widget.com")
        self.assertEqual(node, node2)

    def test_eq3_url_none(self):
        node = TextNode("This is a text node", TextType.BOLD, "www.widget.com")
        node2 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertNotEqual(node, node2)
    
    def test_eq4_text_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is also a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()