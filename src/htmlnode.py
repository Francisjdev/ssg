class HTMLNode:
    def __init__(self,tag=None,value=None,children=None,props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        text = ""
        if self.props == None:
            return ""  
        else:
            for key in self.props:
                text += f' {key}="{self.props[key]}"'  
        return text

    def __repr__(self):
        return f"HTML node ({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value,props=None):
        super().__init__(tag, value, children = None, props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return f"{self.value}"
        else:
            attributes = self.props_to_html()  
            return f'<{self.tag}{attributes}>{self.value}</{self.tag}>'

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag,None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError
        if not self.children: 
            raise ValueError("children missing")
        else:
            attributes = self.props_to_html()
            children_html = ""
            for child in self.children:
                children_html += child.to_html()  
            return f'<{self.tag}{attributes}>{children_html}</{self.tag}>'






