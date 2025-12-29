import unittest
from markdowntools import split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_text_nodes, markdown_to_blocks, extract_title
from textnode import TextNode, TextType

class TestParentNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is plain text ", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.TEXT)
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)

    def test_bold(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes[1].text_type, TextType.BOLD)

    def test_italic(self):
        node = TextNode("This is text with a _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes[1].text_type, TextType.ITALIC)

    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)

    def test_nested_markdown(self):
        node = TextNode("This is text with a `**nested markdown block`**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes[1].text_type, TextType.BOLD)

    def test_invalid_markdown(self):
        node = TextNode("This is text with _invalid** markdown", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "**", TextType.BOLD)
    
    def test_extract_markdown_images(self):
        matches = extract_markdown_images("This is text with an image ![Obi-Wan](https://i.imgur.com/fJRm4Vk.jpeg).")
        self.assertListEqual([("Obi-Wan", "https://i.imgur.com/fJRm4Vk.jpeg")], matches)

    def test_extract_markdown_images_mixed(self):
        matches = extract_markdown_images("This is text with an image ![Obi-Wan](https://i.imgur.com/fJRm4Vk.jpeg) and a link [to boot dev](https://www.boot.dev).")
        self.assertEqual([("Obi-Wan", "https://i.imgur.com/fJRm4Vk.jpeg")], matches)
    
    def test_extract_markdown_links(self):
        matches = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev).")
        self.assertListEqual([("to boot dev", "https://www.boot.dev")], matches)

    def test_extract_markdown_links_mixed(self):
        matches = extract_markdown_links("This is text with an ![Obi-Wan](https://i.imgur.com/fJRm4Vk.jpeg) and a link [to boot dev](https://www.boot.dev).")
        self.assertEqual([("to boot dev", "https://www.boot.dev")], matches)

    def test_extract_markdown_images_multiple(self):
        matches = extract_markdown_images("This is text with an image ![rick roll](https://i.imgur.com/aKaOqIh.gif) and a another image ![Obi-Wan](https://i.imgur.com/fJRm4Vk.jpeg).")
        self.assertEqual([("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("Obi-Wan", "https://i.imgur.com/fJRm4Vk.jpeg")], matches)

    def text_extract_markdown_links_multiple(self):
        matches = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev).")
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")], matches)

    # Tests for split nodes images / links
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and ", TextType.TEXT),
                TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
            ],
            new_nodes,
        )
    
    def test_split_images_mixed(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and a ![image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link [to boot dev](https://www.boot.dev) and a ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

    def test_split_links_mixed(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and a ![image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link ", TextType.TEXT),
                TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                TextNode(" and a ![image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_without_images(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_without_links(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_split_images_no_text(self):
        node = TextNode("", TextType.TEXT,)
        new_nodes = split_nodes_image([node])
        self.assertEqual([], new_nodes)

    def test_split_links_no_text(self):
        node = TextNode("", TextType.TEXT,)
        new_nodes = split_nodes_link([node])
        self.assertEqual([], new_nodes)

    def test_split_images_multiple_nodes(self):
        nodes = [
            TextNode("![image](https://i.imgur.com/zjjcJKZ.png)", TextType.TEXT),
            TextNode("This is just some text", TextType.TEXT),
        ]
        new_nodes = split_nodes_image(nodes)
        self.assertListEqual(
            [
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode("This is just some text", TextType.TEXT),
            ],
            new_nodes,
        )

        # Tests for text_to_text_nodes function
    def test_text_to_text_nodes_base(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_text_nodes(text)
        expected_nodes = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(nodes, expected_nodes)
    
    def test_text_to_text_nodes_multiples(self):
        text = "_This_ is **text** with an _italic_ **word** and a `code block` and `an` ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_text_nodes(text)
        expected_nodes = [
            TextNode("This", TextType.ITALIC),
            TextNode(" is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" ", TextType.TEXT),
            TextNode("word", TextType.BOLD),
            TextNode(" and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and ", TextType.TEXT),
            TextNode("an", TextType.CODE),
            TextNode(" ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(nodes, expected_nodes)

    def test_text_to_text_nodes_none(self):
        text = "This is text with an italic word and a code block and an obi wan image and a link"
        nodes = text_to_text_nodes(text)
        expected_nodes = [
            TextNode("This is text with an italic word and a code block and an obi wan image and a link", TextType.TEXT)
        ]
        self.assertEqual(nodes, expected_nodes)

    def test_text_to_text_nodes_nested(self):
        text = "_This_ is **_text_** with an _italic_ **word** and a `code block` and `an` ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        nodes = text_to_text_nodes(text)
        expected_nodes = [
            TextNode("This", TextType.ITALIC),
            TextNode(" is ", TextType.TEXT),
            TextNode("_text_", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" ", TextType.TEXT),
            TextNode("word", TextType.BOLD),
            TextNode(" and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and ", TextType.TEXT),
            TextNode("an", TextType.CODE),
            TextNode(" ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(nodes, expected_nodes)

    def test_text_to_text_nodes_invalid(self):
        text = "This is text _with **an italic word and a code block and an obi wan image and a link"
        with self.assertRaises(ValueError):
            text_to_text_nodes(text)

    # Tests for markdown_to_blocks function
    def test_markdown_to_blocks_base(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_extra_newlines(self):
        md = """
This is **bolded** paragraph



This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line



- This is a list
- with items



"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    
    def test_extract_heading_base(self):
        md = """
# This is the title
"""
        result = extract_title(md)
        self.assertEqual(result, "This is the title")

    def test_extract_heading_invalid(self):
        md = """
## This is the title
"""
        with self.assertRaises(Exception):
            extract_title(md)