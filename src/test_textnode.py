import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_no_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node.url, None)

    def test_text_type(self):
        node = TextNode("This is a text node with a text type", "bold")
        self.assertEqual(node.text_type, TextType.BOLD)

    def test_invalid_texttype(self):
        with self.assertRaises(ValueError):
            TextNode("This is a text node with an invalid text type", "French")

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()