import unittest
from block_to_html import markdown_to_html_node
from block_type import *
class TestBlockToBlockType(unittest.TestCase):
    
    def test_heading_block(self):
        block = "# A First Heading"
        expected = BlockType.HEADING
        self.assertEqual(block_to_block_type(block), expected)

  
    def test_code_block(self):
        block = "```\nprint('hello')\n```"
        expected = BlockType.CODE
        self.assertEqual(block_to_block_type(block), expected)
        
  
    def test_paragraph_block(self):
        block = "This is a simple paragraph.\nIt has multiple lines."
        expected = BlockType.PARAGRAPH
        self.assertEqual(block_to_block_type(block), expected)

    
    def test_ordered_list_block(self):
        block = "1. First item\n2. Second item"
        expected = BlockType.ORDERED_LIST
        self.assertEqual(block_to_block_type(block), expected)
        
   
    def test_invalid_ordered_list_sequence(self):
        block = "1. Item one\n3. Item two"
        expected = BlockType.PARAGRAPH
        self.assertEqual(block_to_block_type(block), expected)

    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph
    text in a p
    tag here

    This is another paragraph with _italic_ text and `code` here

    """
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )
    def test_codeblock(self):
        md = """
    ```
    This is text that _should_ remain
    the **same** even with inline stuff
    ```
    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )