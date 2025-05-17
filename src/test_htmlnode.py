import unittest
from src.htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node
from src.textnode import TextNode, TextType

class TestHTMLNode(unittest.TestCase):
    def test_props1(self):
        node = HTMLNode(None, None, None, props={ "href": "https://www.google.com",
                                                  "target": "_blank"
                                                }
                       )
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')
    def test_props2(self):
        node = HTMLNode(None, None, None, props=
                        { "class": "fit-picture",
                          "src": "/shared-assets/images/examples/grapefruit-slice.jpg",
                          "alt": "Grapefruit slice atop a pile of other slices"
                        }
                       )
        html = ' class="fit-picture" src="/shared-assets/images/examples/grapefruit-slice.jpg" alt="Grapefruit slice atop a pile of other slices"'
        self.assertEqual(node.props_to_html(), html)
    def test_props3(self):
        node = HTMLNode(None, None, None, props=None)
        html = ''
        self.assertEqual(node.props_to_html(), html)


    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Click me!")
        self.assertEqual(node.to_html(), "Click me!")

    def test_parent_to_html_1(self):
        node = ParentNode('p',
                          [
                              LeafNode('b', 'Bold text'),
                              LeafNode(None, 'Normal text'),
                              LeafNode('i', 'italic text'),
                              LeafNode(None, 'Normal text'),
                          ])
        rendering = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), rendering)
    def test_parent_to_html_2(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")
    def test_parent_to_html_3(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_text_1(self):
        node = TextNode('This is a text node', TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    def test_text_2(self):
        node = TextNode('This is a bold text node', TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'b')
        self.assertEqual(html_node.value, "This is a bold text node")
    def test_text_3(self):
        node = TextNode('This is a link node', TextType.LINK, "https://example.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'a')
        self.assertEqual(html_node.value, "This is a link node")
        self.assertEqual(html_node.props["href"], "https://example.com")
    def test_text_4(self):
        node = TextNode('This is a image node', TextType.IMAGE, "https://example.com/i.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props["src"], "https://example.com/i.jpg")
        self.assertEqual(html_node.props["alt"], 'This is a image node')


if __name__ == "__main__":
    unittest.main()
