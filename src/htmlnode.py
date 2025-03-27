class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        if not self.props:
            return ""

        props_str = ""
        for prop, value in self.props.items():
            props_str += f' {prop}="{value}"'

        return props_str
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if not value:
            raise ValueError("LeafNode must have a value")
        super().__init__(tag=tag, value=value, props=props, children=None)

    def to_html(self):
        if not self.value:
            raise ValueError
        elif self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"