from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError("Leaf Nodes require a value")
        html = ""
        if self.tag == None:
            return self.value
        else:
            html += f"<{self.tag}"
            if self.props != None:
                html += " " + self.props_to_html()
            html += f">{self.value}</{self.tag}>"
        return html