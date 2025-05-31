
import re
from split_blocks import markdown_to_blocks
from blocks import BlockType, block_to_block_type
from htmlnode import LeafNode, ParentNode, text_node_to_html_node
from text_to_textnodes import text_to_textnodes

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = list()
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                text_nodes = text_to_textnodes(block)
                html_nodes = map(text_node_to_html_node, text_nodes)
                p = ParentNode('p', children=list(html_nodes))
                children.append(p)
            case BlockType.HEADING:
                heading_level, heading_text = destruct_heading(block)
                heading_nodes = map(text_node_to_html_node, text_to_textnodes(heading_text))
                h = ParentNode('h' + str(heading_level), children=heading_nodes)
                children.append(h)
            case BlockType.CODE:
                code = extract_code(block)
                code_node = LeafNode('code', code)
                pre_node = ParentNode('pre', children=[code_node])
                children.append(pre_node)
            case BlockType.QUOTE:
                children.append(LeafNode('blockquote', extract_quote(block)))
            case BlockType.UNORDERED_LIST:
                items = extract_unordered_list_items(block)
                htmlize_item = lambda item: list(map(text_node_to_html_node, text_to_textnodes(item)))
                items = map(htmlize_item, items)
                wrap_in_li = lambda item_children: ParentNode('li', children=item_children)
                item_nodes = list(map(wrap_in_li, items))
                children.append(ParentNode('ul', children=item_nodes))
            case BlockType.ORDERED_LIST:
                items = extract_ordered_list_items(block)
                htmlize_item = lambda item: list(map(text_node_to_html_node, text_to_textnodes(item)))
                items = map(htmlize_item, items)
                wrap_in_li = lambda item_children: ParentNode('li', item_children)
                item_nodes = list(map(wrap_in_li, items))
                children.append(ParentNode('ol', children=item_nodes))
    return ParentNode('div', children=children)

def destruct_heading(block):
    # TODO can headings span multiple lines?
    # for now, assume it can't
    m = re.match(r"^(#{1,6}) (.*)", block)
    return len(m.group(1)), m.group(2)

def extract_code(block):
    return block.removeprefix("```\n").removesuffix("```")

def extract_quote(block: str):
    remove_quote_mark = lambda line: line.removeprefix('> ')
    return "\n".join(map(remove_quote_mark, block.splitlines()))

def extract_unordered_list_items(block: str):
    remove_list_mark = lambda line: line.removeprefix('- ')
    return list(map(remove_list_mark, block.splitlines()))

def extract_ordered_list_items(block: str):
    def remove_list_mark(line):
        return re.search(r"^\d+\. (.*)", line).group(1)
    return list(map(remove_list_mark, block.splitlines()))
