import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            match delimiter:
                case "**":  # Bold
                    if node.text.count(delimiter) % 2 > 0:
                        raise ValueError(f"Invalid Markdown - mismatched {delimiter}")
                    else:
                        split_text = node.text.split(delimiter)
                        for i in range(len(split_text)):
                            if i % 2 != 0:
                                new_nodes.append(TextNode(split_text[i], TextType.BOLD))
                            else:
                                new_nodes.append(TextNode(split_text[i], TextType.TEXT))
                case "_":   # Italic
                    if node.text.count(delimiter) % 2 > 0:
                        raise ValueError(f"Invalid Markdown - mismatched {delimiter}")
                    else:
                        split_text = node.text.split(delimiter)
                        for i in range(len(split_text)):
                            if i % 2 != 0:
                                new_nodes.append(TextNode(split_text[i], TextType.ITALIC))
                            else:
                                new_nodes.append(TextNode(split_text[i], TextType.TEXT))
                case "`":   # Code
                    if node.text.count(delimiter) % 2 > 0:
                        raise ValueError(f"Invalid Markdown - mismatched {delimiter}")
                    else:
                        split_text = node.text.split(delimiter)
                        for i in range(len(split_text)):
                            if i % 2 != 0:
                                new_nodes.append(TextNode(split_text[i], TextType.CODE))
                            else:
                                new_nodes.append(TextNode(split_text[i], TextType.TEXT))
                case _:     # Unknown
                    raise ValueError(f"Delimiter '{delimiter}' is not valid")
    return new_nodes

def split_nodes_image(old_nodes):
    nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            nodes.append(node)
            continue
        split = re.split(r"(!\[[^\[\]]*\]\([^\(\)]*\))", node.text)
        i = 0
        while i <= len(split) - 1:
            if split[i]:
                if split[i].startswith("!["):
                    extracted = extract_markdown_images(split[i])
                    for image in extracted:
                        nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
                else:
                    nodes.append(TextNode(split[i], TextType.TEXT))
            i += 1
    return nodes

def split_nodes_link(old_nodes):
    nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            nodes.append(node)
            continue
        split = re.split(r"(?<!!)(\[[^\[\]]*\]\([^\(\)]*\))", node.text)
        i = 0
        while i <= len(split) - 1:
            if split[i]:
                if split[i].startswith("["):
                    extracted = extract_markdown_links(split[i])
                    for link in extracted:
                        nodes.append(TextNode(link[0], TextType.LINK, link[1]))
                else:
                    nodes.append(TextNode(split[i], TextType.TEXT))
            i += 1
    return nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    formatted = []
    for match in matches:
        formatted.append((match[0], match[1]))
    return formatted

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    formatted = []
    for match in matches:
        formatted.append((match[0], match[1]))
    return formatted

def text_to_text_nodes(text: str)->list[TextNode]:
    nodes = split_nodes_delimiter([TextNode(text, TextType.TEXT)],"**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

def markdown_to_blocks(markdown: str)->list[str]:
    blocks = markdown.split("\n\n")
    clean_blocks = []
    for block in blocks:
        if block:
            block = block.rstrip("\n").lstrip("\n")
            clean_blocks.append(block)
    return clean_blocks

def extract_title(markdown: str)->str:
    title = ""
    lines = markdown.split(" ", 1)
    if len(lines[0].strip()) == 1:
        title = lines[1].strip()
    else:
        raise Exception(f"Invalid heading markdown: {markdown}")
    return title