import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_not_eq_types(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertNotEqual(node, node2)
    def test_not_eq_url(self):
        node = TextNode("This is a text node", TextType.LINK, "https://foo.com")
        node2 = TextNode("This is a text node", TextType.LINK, "https://example.com")
        self.assertNotEqual(node, node2)
    def test_not_eq_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is another text node", TextType.TEXT)
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
