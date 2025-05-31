from textnode import TextNode, TextType
from extractmarkdown import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    split_nodes = []
    for old_node in old_nodes:
        if type(old_node) != TextNode:
            raise Exception(f"Expected TextNode, got {type(old_node)}")
        count = old_node.text.count(delimiter)
        if count == 0:
            split_nodes.append(old_node)
            break
        if count % 2 > 0:
            raise Exception("Invalid Markdown")
        else:
            new_nodes = old_node.text.split(delimiter)
            for x in range(0,count+1):
                if x % 2 == 0:
                    split_nodes.append(TextNode(new_nodes[x],TextType.TEXT))
                else:
                    split_nodes.append(TextNode(new_nodes[x],text_type))
    return split_nodes

def split_nodes_image(old_nodes):
    split_nodes = []
    for node in old_nodes:
        temp_text = node.text
        images = extract_markdown_images(temp_text)
        for alt,url in images:
            delimiter = f"![{alt}]({url})"
            split_text = temp_text.split(delimiter)
            temp_text = split_text[1]
            if split_text[0] != "":
                split_nodes.append(TextNode(split_text[0], TextType.TEXT))
            split_nodes.append(TextNode(alt, TextType.IMAGE, url))
    return split_nodes
            

def split_nodes_link(old_nodes):
    split_nodes = []
    for node in old_nodes:
        temp_text = node.text
        links = extract_markdown_links(temp_text)
        for txt,url in links:
            delimiter = f"[{txt}]({url})"
            split_text = temp_text.split(delimiter)
            temp_text = split_text[1]
            if split_text[0] != "":
                split_nodes.append(TextNode(split_text[0], TextType.TEXT))
            split_nodes.append(TextNode(txt, TextType.LINK, url))
    return split_nodes