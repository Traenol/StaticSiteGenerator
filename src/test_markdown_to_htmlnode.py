import unittest
from markdown_to_htmlnode import markdown_to_html_node

class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        #print(repr(html))
        #print(r"<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>")
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_heading(self):
        md = """
###### This is a heading
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h6>This is a heading</h6></div>"
        )

    def test_heading_with_inline_markdown(self):
        md = """
# This _is_ a heading with **inline** markdown.
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>This <i>is</i> a heading with <b>inline</b> markdown.</h1></div>"
        )

    def test_blockquote(self):
        md = """
> Words can be like X-rays, if you use them properly—they’ll go through
> anything. You read and you’re pierced.
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>Words can be like X-rays, if you use them properly—they’ll go through anything. You read and you’re pierced.</blockquote></div>"
        )

    def test_blockquote_with_inline_markdown(self):
        md = """
> Words can be like **X-rays**, if you use them properly—they’ll go through
> anything. You read and you’re _pierced_.
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>Words can be like <b>X-rays</b>, if you use them properly—they’ll go through anything. You read and you’re <i>pierced</i>.</blockquote></div>"
        )
    
    def test_blockquote_with_empty_line(self):
        md = """
> "I am in fact a Hobbit in all but size."
>
> -- J.R.R. Tolkien
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><blockquote>"I am in fact a Hobbit in all but size." -- J.R.R. Tolkien</blockquote></div>'
        )

    def test_unordered_list(self):
        md = """
- This is an
- unordered list
- with items
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is an</li><li>unordered list</li><li>with items</li></ul></div>"
        )

    def test_unordered_list_with_inline_markdown(self):
        md = """
- This is an
- **unordered** list
- with _items_
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is an</li><li><b>unordered</b> list</li><li>with <i>items</i></li></ul></div>"
        )

    def test_ordered_list(self):
        md = """
1. This is an
2. ordered list
3. with items
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>This is an</li><li>ordered list</li><li>with items</li></ol></div>"
        )
    
    def test_ordered_list_with_inline_markdown(self):
        md = """
1. This is an
2. **ordered** list
3. with _items_
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>This is an</li><li><b>ordered</b> list</li><li>with <i>items</i></li></ol></div>"
        )