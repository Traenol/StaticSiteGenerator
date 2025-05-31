from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("Parent Nodes require a tag")
        if self.children == None:
            raise ValueError("Parent Nodes need children to care for!")
        
        html = f"<{self.tag}"
        if self.props != None:
            html += " " + self.props_to_html()
        html += f">"
        for child in self.children:
            html += child.to_html()
        html += f"</{self.tag}>"
        return html