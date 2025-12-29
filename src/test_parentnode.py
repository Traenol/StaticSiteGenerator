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

    def test_parent_with_many_children(self):
        child_node1 = LeafNode("b", "child 1")
        child_node2 = LeafNode("b", "child 2")
        child_node3 = LeafNode("b", "child 3")
        child_node4 = LeafNode("b", "child 4")
        child_node5 = LeafNode("b", "child 5")
        parent_node = ParentNode("div", [child_node1,child_node2,child_node3,child_node4,child_node5])
        self.assertEqual(
            parent_node.to_html(),
            "<div><b>child 1</b><b>child 2</b><b>child 3</b><b>child 4</b><b>child 5</b></div>",
        )
