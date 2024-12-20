import unittest

from extract_markdown import *


class TestExtractImage(unittest.TestCase):
    def test_eq(self):
        image_list = extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")
        expected = [('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')]
        self.assertEqual(image_list, expected)
    def test_eq2_tag(self):
        image_list = extract_markdown_images("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)")
        expected = [('lollipop', 'https://i.imgur.com/aKqIh.gif'), ('obi juan', 'https://i.imgur.com/fJRm4Vk.jpeg')]
        self.assertNotEqual(image_list, expected)

class TestExtractLink(unittest.TestCase):
    def test_eq(self):
        link_list = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
        expected = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(link_list, expected)
    def test_eq2_tag(self):
        link_list = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)")
        expected = [('lollipop', 'https://i.imgur.com/aKqIh.gif'), ('obi juan', 'https://i.imgur.com/fJRm4Vk.jpeg')]
        self.assertNotEqual(link_list, expected)

if __name__ == "__main__":
    unittest.main()