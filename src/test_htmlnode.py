import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_empty_props(self):
        #create a node with no props
        node = HTMLNode()
        #check that props_to_html returns an empty string
        self.assertEqual(node.props_to_html(), "")

        #test with empty dict
        node2 = HTMLNode(props={})
        self.assertEqual(node2.props_to_html(), "")

    def test_props_to_html_multiple_props(self):
        #create a node with multiple props
        node = HTMLNode(props={
            "href": "https://www.google.com",
            "target": "_blank",
            "class" : "link"
        })

        #pass node into props_to_html function
        result = node.props_to_html()

        self.assertIn(' href="https://www.google.com"', result)
        self.assertIn(' target="_blank"', result)
        self.assertIn(' class="link"', result)

        #verify the total length matches what we expect (spaces + all attributes)
        expected_length = len(' href="https://www.google.com"') + \
                          len(' target="_blank"') + \
                          len(' class="link"')
        self.assertEqual(len(result), expected_length)

    def test_props_to_html_single_prop(self):
        #create a node with a single prop
        node = HTMLNode(props={
            "class" : "link"
        })

        result = node.props_to_html()
        self.assertIn(' class="link"', result)
        expected_length = len(' class="link"')
        self.assertEqual(len(result), expected_length)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_p(self):
        node = LeafNode("b", "Hello, world!")
        self.assertEqual(node.to_html(), "<b>Hello, world!</b>")

    def test_leaf_to_html_p(self):
        node = LeafNode("span", "Hello, world!")
        self.assertEqual(node.to_html(), "<span>Hello, world!</span>")

if __name__ == "__main__":
    unittest.main()