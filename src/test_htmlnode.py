import unittest
from src.htmlnode import HTMLNode, LeafNode, ParentNode

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

if __name__ == "__main__":
    unittest.main()
