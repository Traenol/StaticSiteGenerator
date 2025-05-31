import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_greatgrandchildren(self):
        greatgrandchild_node = LeafNode("b", "greatgrandchild")
        grandchild_node = ParentNode("div", [greatgrandchild_node])
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><div><b>greatgrandchild</b></div></span></div>",
        )
    
    def test_to_html_with_multiple_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node,child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span><span>child</span></div>")

    def test_to_html_with_multiple_grandchildren(self):
        greatgrandchild_node = LeafNode("b", "greatgrandchild")
        grandchild_node = ParentNode("div", [greatgrandchild_node])
        child_node = ParentNode("span", [grandchild_node,grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><div><b>greatgrandchild</b></div><div><b>greatgrandchild</b></div></span></div>",
        )

    def test_to_html_with_missing_parent_tag(self):
        greatgrandchild_node = LeafNode("b", "greatgrandchild")
        grandchild_node = ParentNode(None, [greatgrandchild_node])
        with self.assertRaises(ValueError):
            grandchild_node.to_html()

    def test_to_html_with_no_children(self):
        with self.assertRaises(ValueError):
            ParentNode("b", None).to_html()