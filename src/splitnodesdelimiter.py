from textnode import TextNode, TextType

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