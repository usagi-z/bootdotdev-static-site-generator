import unittest

from markdown_to_html import markdown_to_html_node


class TestMarkdownToHtml(unittest.TestCase):
    def test_1(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
        node = markdown_to_html_node(md)
        self.assertEqual(node.to_html(),
                         "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>"
                         )
    def test_2(self):
        md = """
###### this is a level 6 heading

## this is a level 2 heading

# this is a level 1 heading
"""
        node = markdown_to_html_node(md)
        self.assertEqual(node.to_html(),
                         "<div><h6>this is a level 6 heading</h6><h2>this is a level 2 heading</h2><h1>this is a level 1 heading</h1></div>"
                         )
    def test_3(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""
        node = markdown_to_html_node(md)
        self.assertEqual(node.to_html(),
                         "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
                         )
    def test_4(self):
        md = """
>this is
>a quote
"""
        node = markdown_to_html_node(md)
        self.assertEqual(node.to_html(),
                         "<div><blockquote>this is\na quote</blockquote></div>"
                         )
    def test_5(self):
        md = """
- foo
- bar
- baz
"""
        node = markdown_to_html_node(md)
        self.assertEqual(node.to_html(),
                         "<div><ul><li>foo</li><li>bar</li><li>baz</li></ul></div>"
                         )
    def test_6(self):
        md = """
1. foo
2. bar
3. baz
"""
        node = markdown_to_html_node(md)
        self.assertEqual(node.to_html(),
                         "<div><ol><li>foo</li><li>bar</li><li>baz</li></ol></div>"
                         )

if __name__ == "__main__":
    unittest.main()
