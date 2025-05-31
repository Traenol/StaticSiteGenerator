import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        actual = LeafNode("p", "This is a paragraph of text.").to_html()
        expected = "<p>This is a paragraph of text.</p>"
        self.assertEqual(expected, actual)

    def test_leaf_to_html_a(self):
        actual = LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
        expected = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()