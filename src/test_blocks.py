import unittest
import re
from blocks import BlockType, block_to_block_type

class TestBlockType(unittest.TestCase):
    def test_block_to_block_type_paragraph(self):
        md = """
This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line
"""
        self.assertEqual(block_to_block_type(md), BlockType.PARAGRAPH)

    def test_block_to_block_type_heading(self):
        md = "#### This is a Heading"
        self.assertEqual(block_to_block_type(md), BlockType.HEADING)

    def test_block_to_block_type_invalid_heading(self):
        md = "####### This is not a heading"
        self.assertEqual(block_to_block_type(md), BlockType.PARAGRAPH)

    def test_block_to_block_type_code(self):
        md = """
```
This is a code block
This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line
```
"""
        self.assertEqual(block_to_block_type(md), BlockType.CODE)

    def test_block_to_block_type_quote(self):
        md = """>This is a Quote block
>This is another paragraph with _italic_ text and `code` here
>This is the same paragraph on a new line"""
        self.assertEqual(block_to_block_type(md), BlockType.QUOTE)
    
    def test_block_to_block_type_ordered_list(self):
        md = """1. This is an
2. ordered list
3. with items"""
        self.assertEqual(block_to_block_type(md), BlockType.ORDERED_LIST)

    def test_block_to_block_type_long_ordered_list(self):
        md = """1. This is an
2. ordered list
3. with items
4. that just keeps going
5. and going
6. and going
7. and going
8. and going
9. and going
10. just like that bunny"""
        self.assertEqual(block_to_block_type(md), BlockType.ORDERED_LIST)
    
    def test_block_to_block_type_invalid_ordered_list(self):
        md = """1. This is an
4. ordered list
3. with items"""
        self.assertEqual(block_to_block_type(md), BlockType.PARAGRAPH)

    def test_block_to_block_type_unordered_list(self):
        md = """- This is an
- unordered list
- with items"""
        self.assertEqual(block_to_block_type(md), BlockType.UNORDERED_LIST)