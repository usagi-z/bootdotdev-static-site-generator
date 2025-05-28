import unittest

from blocks import BlockType, block_to_block_type


class TestBlocks(unittest.TestCase):
    def test_block_to_block_type_1(self):
        block = "### foobar"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
    def test_block_to_block_type_2(self):
        block = "####### foobar"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    def test_block_to_block_type_3(self):
        block = "```\nfoobar\nfoobaz\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
    def test_block_to_block_type_4(self):
        block = "```foobar\nfoobaz"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    def test_block_to_block_type_5(self):
        block = "> foobar\n> foobaz\n> foobrob"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
    def test_block_to_block_type_6(self):
        block = "- foobar\n- foobaz\n- foobrob"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
    def test_block_to_block_type_7(self):
        block = "1. foobar\n2. foobaz\n3. foobrob"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
    def test_block_to_block_type_8(self):
        block = "1. foobar\n5. foobaz\n3. foobrob"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
    def test_block_to_block_type_9(self):
        block = "2. foobar\n3. foobaz\n4. foobrob"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)
