from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("Tag is required")
        if not self.children:
            raise ValueError("Parents need children")
        html = ""
        if self.props:
            html = self.props_to_html()
        html = f"<{self.tag}{html}>"
        for child in self.children:
            html += child.to_html()
        html += f"</{self.tag}>"
        return html