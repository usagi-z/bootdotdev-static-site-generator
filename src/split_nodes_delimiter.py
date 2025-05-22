from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    def split_node_delimiter(node):
        if node.text_type != TextType.TEXT:
            return [node]
        r = []
        fragments = node.text.split(delimiter)
        if len(fragments) % 2 == 0:
            raise Exception(f"Invalid syntax: unmatched {delimiter}")
        for i, fragment in enumerate(fragments):
            if i % 2 == 0:
                tt = TextType.TEXT
            else:
                tt = text_type
            if fragment != "":
                r.append(TextNode(fragment, tt))
        return r

    r = list()
    for sublist in map(split_node_delimiter, old_nodes):
        r.extend(sublist)
    return r

