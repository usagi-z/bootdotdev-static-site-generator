import unittest
from src.htmlnode import HTMLNode

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

if __name__ == "__main__":
    unittest.main()
