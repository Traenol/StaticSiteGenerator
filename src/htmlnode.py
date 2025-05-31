class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        html = ""
        for prop in self.props:
            html += prop + "=\"" + self.props[prop] + "\" "
        return html.strip(" ")
    
    def __repr__(self):
        nodetext =  "HTMLNode: \n"
        nodetext += f"tag: {self.tag}\n"
        nodetext += f"value: {self.value}\n"
        nodetext += f"children: {self.children}\n"
        nodetext += f"props: {self.props}\n"
        return nodetext