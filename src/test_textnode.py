import unittest

from textnode import text_node_to_html_node, TextNode, TextType



class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_ineq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)
    def test_not_eq_different_text_type(self):
        node1 = TextNode("Hello", TextType.TEXT, None)
        node2 = TextNode("Hello", TextType.BOLD, None)
        self.assertNotEqual(node1, node2)
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    def test_image(self):
        node = TextNode("This is a duck image", TextType.IMAGE, "https://example.com/image.jpg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")  # Images have empty value
        self.assertEqual(html_node.props, {"src": "https://example.com/image.jpg", "alt": "This is a duck image"})
    def test_invalid_text_type(self):
        with self.assertRaises(Exception):
            node = TextNode("This is a text node", "INVALID_TYPE")
            text_node_to_html_node(node)
if __name__ == "__main__":
    unittest.main()