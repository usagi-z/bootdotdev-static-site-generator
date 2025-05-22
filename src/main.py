from split_nodes import split_nodes_image
from textnode import *

def main():
    node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT
    )
    new_nodes = split_nodes_image([node])
    t = [
        TextNode("This is text with an ", TextType.TEXT),
        TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
        TextNode(" and another ", TextType.TEXT),
        TextNode(
            "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
        ),
    ]
    # print(t)
    print(new_nodes)


if __name__ == '__main__':
    main()
