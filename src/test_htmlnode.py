import unittest

from htmlnode import HTMLNode, LeafNode,ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_with_props(self):
        node = HTMLNode('p', None, None, {'class': 'highlight'})
        result = node.props_to_html()
        expected = ' class="highlight"'
        self.assertEqual(result, expected)
        
    
    def test_props_to_html_multiple_props(self):
        node = HTMLNode('a', None, None, {'href': 'https://google.com', 'target': '_blank'})
        result = node.props_to_html()
        expected = ' href="https://google.com" target="_blank"'
        self.assertEqual(result, expected)

    def test_props_to_html_empty_props(self):
        node = HTMLNode('div', None, None, )
        result = node.props_to_html()
        expected = ""
        self.assertEqual(result, expected)

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Just raw text")
        self.assertEqual(node.to_html(), "Just raw text")
    
    def test_leaf_to_html_no_value_raises_error(self):
        with self.assertRaises(ValueError):
            node = LeafNode("p", None)
            node.to_html()

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_many_children(self):
        child_node = LeafNode("span", "child")
        child2_node = LeafNode("span", "child2")
        child3_node = LeafNode("p", "child3")
        parent_node = ParentNode("div", [child_node, child2_node, child3_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span><span>child2</span><p>child3</p></div>")

    def test_to_html_with_no_children_raises_error(self):
        with self.assertRaises(ValueError):
            parent_node = ParentNode("div", None)  
            parent_node.to_html()

    def test_to_html_with_empty_children(self):
        with self.assertRaises(ValueError):
            parent_node = ParentNode("div", [])  
            parent_node.to_html()        

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()