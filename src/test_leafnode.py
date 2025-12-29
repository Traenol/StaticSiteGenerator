import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        props = {"href": "https://www.google.com", "target": "_blank",}
        node = LeafNode("a", "Click me!", props)
        expected_result = '<a href="https://www.google.com" target="_blank">Click me!</a>'
        self.assertEqual(node.to_html(), expected_result)

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Just a plain text node ")
        expected_result = "Just a plain text node "
        self.assertEqual(node.to_html(), expected_result)


if __name__ == "__main__":
    unittest.main()