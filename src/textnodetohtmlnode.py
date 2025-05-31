from textnode import TextType
from leafnode import LeafNode

def text_node_to_html_node(text_node):
    if not text_node.text_type in TextType:
        raise Exception("Invalid text type")
    tag = None
    value = None
    props = None
    match text_node.text_type:
        case TextType.TEXT:
            value = text_node.text
        case TextType.BOLD:
            tag = "b"
            value = text_node.text
        case TextType.ITALIC:
            tag = "i"
            value = text_node.text
        case TextType.CODE:
            tag = "code"
            value = text_node.text
        case TextType.IMAGE:
            if text_node.url == None:
                raise ValueError("Image tags must specify the url")
            tag = "img"
            props = {
                "src": text_node.url,
                "alt": text_node.text
            }
        case TextType.LINK:
            if text_node.url == None:
                raise ValueError("Link tags must specify the url")
            if text_node.text == None or text_node.text == "":
                raise ValueError("Link tags must specify the text")
            tag = "a"
            value = text_node.text
            props = {
                "href": text_node.url,
            }
    return LeafNode(tag, value, props)