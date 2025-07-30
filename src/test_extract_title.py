import unittest
from extract_markdown import extract_title_markdown

class TestExtractTitle(unittest.TestCase):


    def test_extract_title_basic(self):
        markdown = "# Hello World"
        result = extract_title_markdown(markdown)
        self.assertEqual(result, "Hello World")

    def test_extract_title_no_header(self):
        markdown = "## Only h2\nSome text"
        with self.assertRaises(Exception):
            extract_title_markdown(markdown)

    def test_extract_title_with_whitespace(self):
        markdown = "#   Hello World   "
        result = extract_title_markdown(markdown)
        self.assertEqual(result, "Hello World")

    def test_extract_title_not_first_line(self):
        markdown = "Some intro\n# My Title\nMore content"
        result = extract_title_markdown(markdown)
        self.assertEqual(result, "My Title")