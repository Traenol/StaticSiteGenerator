import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_single(self):
        node = HTMLNode("a", "Google", None, {"target": "_blank",})
        self.assertEqual(node.props_to_html(), 'target="_blank"')

    def test_props_to_html_multiple(self):
        node = HTMLNode("a", "Google", None, {"href": "https://www.google.com","target": "_blank",})
        self.assertEqual(node.props_to_html(), 'href="https://www.google.com" target="_blank"')
    
    def test_to_html(self):
        node = HTMLNode("a", "Google", None, {"href": "https://www.google.com","target": "_blank",})
        with self.assertRaises(NotImplementedError):
            node.to_html()
    