from extract_links import extract_markdown_images, extract_markdown_links
from textnode import TextNode, TextType

def split_nodes_image(old_nodes):
    def split_node_image(node):
        if node.text_type != TextType.TEXT:
            return [node]
        text = node.text
        imgs = extract_markdown_images(text)
        r = list()

        for alt, url in imgs:
            sections = text.split(f"![{alt}]({url})", 1)
            if len(sections) == 2:
                t = sections[0]
                if t != "":
                    r.append(TextNode(t, TextType.TEXT))
                text = sections[1]
            r.append(TextNode(alt, TextType.IMAGE, url))
        if text != "":
            r.append(TextNode(text, TextType.TEXT))
        return r

    r = list()
    for sublist in map(split_node_image, old_nodes):
        r.extend(sublist)
    return r

def split_nodes_link(old_nodes):
    def split_node_link(node):
        if node.text_type != TextType.TEXT:
            return [node]
        text = node.text
        links = extract_markdown_links(text)
        r = list()

        for link_text, url in links:
            sections = text.split(f"[{link_text}]({url})", 1)
            if len(sections) == 2:
                t = sections[0]
                if t != "":
                    r.append(TextNode(t, TextType.TEXT))
                text = sections[1]
            r.append(TextNode(link_text, TextType.LINK, url))
        if text != "":
            r.append(TextNode(text, TextType.TEXT))
        return r

    r = list()
    for sublist in map(split_node_link, old_nodes):
        r.extend(sublist)
    return r

