from enum import Enum
from typing import override


class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

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
