from markdowntools import markdown_to_blocks, text_to_text_nodes
from blocks import BlockType, block_to_block_type
from nodetools import text_node_to_html_node, TextNode, TextType
from htmlnode import HTMLNode
from parentnode import ParentNode
from leafnode import LeafNode

def markdown_to_html_node(markdown: str)->HTMLNode:
    child_nodes = []
    md_blocks = markdown_to_blocks(markdown)
    for md_block in md_blocks:
        block_type = block_to_block_type(md_block)
        match block_type:
            case BlockType.CODE:
                cleaned_md = ""
                for line in md_block.strip().splitlines()[1:-1]:
                    cleaned_md += line + "\n"
                code_text = TextNode(cleaned_md, TextType.CODE)
                code_leaf = text_node_to_html_node(code_text)
                child_nodes.append(ParentNode("pre", [code_leaf]))
            case BlockType.PARAGRAPH:
                children = markdown_to_children(md_block)
                child_nodes.append(ParentNode("p", children))
            case BlockType.QUOTE:
                children = markdown_to_children(md_block, "> ")
                child_nodes.append(ParentNode("blockquote", children))
            case BlockType.UNORDERED_LIST:
                children = list_item_to_children(md_block)
                child_nodes.append(ParentNode("ul", children))
            case BlockType.ORDERED_LIST:
                children = list_item_to_children(md_block)
                child_nodes.append(ParentNode("ol", children))
            case BlockType.HEADING:
                lines = md_block.split(" ", 1)
                heading_number = len(lines[0].strip())
                leafs = text_to_children(lines[1].rstrip())
                child_nodes.append(ParentNode(f"h{heading_number}", leafs))
    return ParentNode("div", child_nodes)

def text_to_children(text: str)->list[HTMLNode]:
    text_nodes = text_to_text_nodes(text)
    leafs = []
    for node in text_nodes:
        leafs.append(text_node_to_html_node(node))
    return leafs

def markdown_to_children(markdown: str, remove_from_start="")->list[HTMLNode]:
    cleaned_md = ""
    for line in markdown.splitlines():
        if line:
            if not remove_from_start:
                cleaned_md += line + " "
            else:
                try:
                    cleaned_md += line.split(remove_from_start, 1)[1] + " "
                except:
                    print(f"Nothing to remove from line: {line}")
    return text_to_children(cleaned_md.rstrip())

def list_item_to_children(markdown: str)->list[HTMLNode]:
    children = []
    for line in markdown.splitlines():
        if line[0] == "-":
            children.append(ParentNode("li", text_to_children(line.split("- ",1)[1])))
        else:
            children.append(ParentNode("li", text_to_children(line.split(". ",1)[1])))
    return children
