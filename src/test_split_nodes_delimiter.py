import unittest

from src.split_nodes_delimiter import split_nodes_delimiter
from src.textnode import TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_1(self):
        node = TextNode("a`b`c", TextType.TEXT)
        result_nodes = [
            TextNode('a', TextType.TEXT),
            TextNode('b', TextType.CODE),
            TextNode('c', TextType.TEXT),
        ]
        self.assertEqual(split_nodes_delimiter([node], '`', TextType.CODE), result_nodes)
    def test_2(self):
        node = TextNode("a`b`", TextType.TEXT)
        result_nodes = [
            TextNode('a', TextType.TEXT),
            TextNode('b', TextType.CODE),
        ]
        self.assertEqual(split_nodes_delimiter([node], '`', TextType.CODE), result_nodes)
    def test_3(self):
        node = TextNode("a`b", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], '`', TextType.CODE)
    def test_4(self):
        node1 = TextNode("a`b`c", TextType.TEXT)
        node2 = TextNode("d`e`f", TextType.TEXT)
        result_nodes = [
            TextNode('a', TextType.TEXT),
            TextNode('b', TextType.CODE),
            TextNode('c', TextType.TEXT),
            TextNode('d', TextType.TEXT),
            TextNode('e', TextType.CODE),
            TextNode('f', TextType.TEXT),
        ]
        self.assertEqual(split_nodes_delimiter([node1, node2], '`', TextType.CODE),
                         result_nodes)
    def test_5(self):
        node1 = TextNode("a**b**c", TextType.TEXT)
        node2 = TextNode("d**e**f", TextType.TEXT)
        result_nodes = [
            TextNode('a', TextType.TEXT),
            TextNode('b', TextType.BOLD),
            TextNode('c', TextType.TEXT),
            TextNode('d', TextType.TEXT),
            TextNode('e', TextType.BOLD),
            TextNode('f', TextType.TEXT),
        ]
        self.assertEqual(split_nodes_delimiter([node1, node2], '**', TextType.BOLD),
                         result_nodes)
    def test_6(self):
        node = TextNode("", TextType.TEXT)
        self.assertEqual(split_nodes_delimiter([node], '**', TextType.BOLD), [])

if __name__ == "__main__":
    unittest.main()
