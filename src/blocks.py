from enum import Enum
from itertools import pairwise, tee
import re


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    if re.match(r"^#{1,6} ", block):
        return BlockType.HEADING
    elif re.search(r"^```\n", block) and re.search(r"\n```$", block):
        return BlockType.CODE
    elif is_quote_block(block):
        return BlockType.QUOTE
    elif is_ordered_list(block):
        return BlockType.ORDERED_LIST
    elif is_unordered_list(block):
        return BlockType.UNORDERED_LIST
    else:
        return BlockType.PARAGRAPH

def is_unordered_list(block):
    has_right_start = lambda line: line.startswith("- ")
    return all(map(has_right_start, block.split("\n")))

def is_quote_block(block):
    has_right_start = lambda line: line.startswith('>')
    return all(map(has_right_start, block.split("\n")))

def is_ordered_list(block):
    lines = block.splitlines()

    def extract_number(line):
        digits = re.findall(r"^(\d+)\. ", line)
        if len(digits) == 1:
            try:
                return int(digits[0])
            except ValueError:
                return None

    numbers = map(extract_number, lines)
    numbers1, numbers2, numbers3 = tee(numbers, 3)

    if next(numbers1) != 1:
        return False

    if any(map(lambda x: x == None, numbers2)):
        return False

    def is_one_greater(x, y):
        return x + 1 == y
    pairs = pairwise(numbers3)
    return all(map(lambda x: is_one_greater(x[0], x[1]), pairs))
