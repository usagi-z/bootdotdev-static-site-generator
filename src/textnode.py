from enum import Enum
from typing import override


class TextType(Enum):
    NORMAL_TEXT = "normal"
    BOLD_TEXT = "bold"
    ITALIC_TEXT = "italic"
    CODE_TEXT = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    def __eq__(self, other):
        return (self.text_type == other.text_type and
                self.text == other.text and
                self.url == other.url)
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
