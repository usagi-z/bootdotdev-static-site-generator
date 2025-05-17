from src.textnode import TextNode, TextType


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def __repr__(self):
       return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    def to_html(self):
        raise NotImplementedError
    def props_to_html(self):
        if self.props != None:
            format_pair = lambda p: p[0] + "=" + '"' + p[1] + '"'
            pairs = self.props.items()
            pairs = map(format_pair, pairs)
            return " " + " ".join(list(pairs))
        else:
            return ""

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
       super().__init__(tag=tag, value=value, children=None, props=props)
    def to_html(self):
        if self.value == None:
            raise ValueError
        elif self.tag == None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)
    def to_html(self):
        if self.tag == None:
            raise ValueError("no tag")
        elif self.children == None:
            raise ValueError("no children")
        else:
            children = ''.join(map(lambda c: c.to_html(), self.children))
            return f"<{self.tag}{self.props_to_html()}>{children}</{self.tag}>"



def text_node_to_html_node(text_node: TextNode):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode('b', text_node.text)
        case TextType.ITALIC:
            return LeafNode('i', text_node.text)
        case TextType.CODE:
            return LeafNode('code', text_node.text)
        case TextType.LINK:
            return LeafNode('a', text_node.text, { "href": text_node.url})
        case TextType.IMAGE:
            return LeafNode('img', '', {
                "src": text_node.url,
                "alt": text_node.text
            })
        case _:
            raise Exception("invalid TextType")

