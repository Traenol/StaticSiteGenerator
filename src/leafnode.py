from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self)->str:
        if self.value == None:
            raise ValueError("Leaf nodes require a value")
        html = ""
        if self.tag:
            html += f"<{self.tag}"
            if self.props:
                html += self.props_to_html()
            if self.tag == "img":
                html += "/>"
            else:
                html += f">{self.value}</{self.tag}>"
            return html
        else:
            return self.value