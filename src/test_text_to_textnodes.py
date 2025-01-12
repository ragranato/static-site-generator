import unittest

from text_to_textnodes import *


class TestTextToTextnodes(unittest.TestCase):
    def test_eq(self):
        node_list = text_to_textnodes("This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)")
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(node_list, expected)
    # def test_eq2_tag(self):
    #     image_list = split_nodes_image([TextNode("This is a test of the coding network...", TextType.TEXT)])
    #     expected = [
    #         TextNode("This is a test of the coding network...", TextType.TEXT),            
    #     ]
    #     self.assertEqual(image_list, expected)


if __name__ == "__main__":
    unittest.main()