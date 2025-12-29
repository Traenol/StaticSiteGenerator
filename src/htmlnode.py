class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self)->str:
        raise NotImplemented() # pyright: ignore[reportOptionalCall]
    
    def props_to_html(self):
        html = ""
        if type(self.props) is not dict:
            raise TypeError("props must be a dictionary")
        for prop in self.props:
            html += f' {prop}="{self.props[prop]}"'
        return html
        
    def __repr__(self):
        temp = ""
        temp += f"Tag: {self.tag}\n"
        temp += f"Value: {self.value}\n"
        if self.value is None:
            temp += "If this is expected, make sure there are children.\n"
        if self.children is not None:
            for child in self.children:
                temp += f"Child: {child}\n"
        else:
            temp += "Children: None\nIf this is expected, make sure there is a value.\n"
        if self.props is not None:
            temp += self.props_to_html() + "\n"
        return temp