import re
from enum import Enum
from htmlnode import HTMLNode
from markdowntools import markdown_to_blocks

class BlockType(Enum):
    PARAGRAPH = 0
    HEADING = 1
    CODE = 2
    QUOTE = 3
    UNORDERED_LIST = 4
    ORDERED_LIST = 5

def block_to_block_type(markdown: str)->BlockType:
    split_md = markdown.strip().split("\n")
    if split_md[0] == "```" and split_md[-1] == "```":
        return BlockType.CODE
    elif re.match(r"^[#]{1,6} ",split_md[0]):
        return BlockType.HEADING
    elif lines_start_with(split_md, ">"):
        return BlockType.QUOTE
    elif lines_start_with(split_md, "- "):
        return BlockType.UNORDERED_LIST
    elif is_ordered_list(split_md):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH

def lines_start_with(lines: list[str], prefix: str)->bool:
    for line in lines:
        if not line.startswith(prefix):
            return False
    return True

def is_ordered_list(list_to_check: list[str])->bool:
    for n, line in enumerate(list_to_check, start=1):
        if not line.startswith(f"{n}. "):
            return False
    return True
