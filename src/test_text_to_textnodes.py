import unittest

from split_nodes import split_nodes_image, split_nodes_link
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType

class TestTextToTextNodes(unittest.TestCase):
    def test_1(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        result = text_to_textnodes(text)
        nodes = [
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
        self.assertListEqual(nodes, result)
    def test_2(self):
        text = "This is a **_bold_** text with underscores"
        result = text_to_textnodes(text)
        nodes = [
            TextNode("This is a ", TextType.TEXT),
            TextNode("_bold_", TextType.BOLD),
            TextNode(" text with underscores", TextType.TEXT),
        ]
        self.assertListEqual(nodes, result)
    def test_3(self):
        with self.assertRaises(Exception):
            text = "This is a `**_code_**` text with underscores and earmuffs"
            text_to_textnodes(text)

