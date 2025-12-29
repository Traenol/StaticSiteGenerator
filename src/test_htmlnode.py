import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        props = {"href": "https://www.google.com", "target": "_blank",}
        node = HTMLNode("a", None, None, props)
        expected_result = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_result)
    
    def test_wrong_props_type(self):
        props = ["href", "https://www.google.com", "target", "_blank",]
        node = HTMLNode("a", None, None, props)
        with self.assertRaises(TypeError):
            node.props_to_html()

    def test_repr(self):
        node = HTMLNode("a", None, None, None)
        expected_result = "Tag: a\nValue: None\nIf this is expected, make sure there are children.\nChildren: None\nIf this is expected, make sure there is a value.\n"
        self.assertEqual(node.__repr__(), expected_result)


if __name__ == "__main__":
    unittest.main()