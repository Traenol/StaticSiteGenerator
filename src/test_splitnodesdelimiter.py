import unittest
from splitnodesdelimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNodesDelmimiter(unittest.TestCase):
    def test_no_delimiter(self):
        node = TextNode("This is text with no markdown", TextType.TEXT)
        actual = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [TextNode("This is text with no markdown", TextType.TEXT)]
        self.assertEqual(expected, actual)

    def test_invalid_markdown(self):
        node = TextNode("This is text with **invalid** Markdown**!", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter(node)

    def test_bold(self):
        node = TextNode("This is text with a **bold** statement", TextType.TEXT)
        actual = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" statement", TextType.TEXT),
            ]
        self.assertEqual(expected, actual)

    def test_italic(self):
        node = TextNode("This is text with _emphasis_!", TextType.TEXT)
        actual = split_nodes_delimiter([node], "_", TextType.ITALIC)
        expected = expected = [
            TextNode("This is text with ", TextType.TEXT),
            TextNode("emphasis", TextType.ITALIC),
            TextNode("!", TextType.TEXT),
            ]
        self.assertEqual(expected, actual)

    def test_code(self):
        node = TextNode("This is `code` inline", TextType.TEXT)
        actual = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" inline", TextType.TEXT),
            ]
        self.assertEqual(expected, actual)

    def test_nested(self):
        node = TextNode("This is text with **_bold and italicized_** text.", TextType.TEXT)
        actual = split_nodes_delimiter([node], "_", TextType.ITALIC)
        expected = expected = [
            TextNode("This is text with **", TextType.TEXT),
            TextNode("bold and italicized", TextType.ITALIC),
            TextNode("** text.", TextType.TEXT),
            ]
        self.assertEqual(expected, actual)

    def test_multiple(self):
        node = TextNode("This is text with **bold** and _italicized_ text.", TextType.TEXT)
        actual = split_nodes_delimiter([node], "**", TextType.BOLD)
        expected = expected = [
            TextNode("This is text with ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" and _italicized_ text.", TextType.TEXT),
            ]
        self.assertEqual(expected, actual)