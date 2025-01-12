import unittest

from splitnodes import *


class TestSplitNodesImage(unittest.TestCase):
    def test_eq(self):
        image_list = split_nodes_image([TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", TextType.TEXT)])
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"
            ),
        ]
        self.assertEqual(image_list, expected)
    def test_eq2_tag(self):
        image_list = split_nodes_image([TextNode("This is a test of the coding network...", TextType.TEXT)])
        expected = [
            TextNode("This is a test of the coding network...", TextType.TEXT),            
        ]
        self.assertEqual(image_list, expected)
class TestExtractLink(unittest.TestCase):
    def test_eq(self):
        link_list = split_nodes_link([TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)])
        expected = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
            ),
        ]
        self.assertEqual(link_list, expected)
    def test_eq2_tag(self):
        link_list = split_nodes_link([TextNode("This is a test of the coding network...", TextType.TEXT)])
        expected = [
            TextNode("This is a test of the coding network...", TextType.TEXT)
        ]
        self.assertEqual(link_list, expected)

if __name__ == "__main__":
    unittest.main()