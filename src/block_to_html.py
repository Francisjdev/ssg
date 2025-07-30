from block_type import block_to_block_type, BlockType
from block_split import markdown_to_blocks
from htmlnode import HTMLNode, ParentNode,LeafNode
from nodesplit import text_to_textnodes
from textnode import *

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    block_nodes =[]
    for block in blocks:
        btype = block_to_block_type(block)
        if btype == BlockType.HEADING:
            space_idx = space_index_finder(block)
            heading_tag = block.count("#",0,space_idx)

            if heading_tag <=6:
                block_text = block[space_idx + 1:]
                text_nodes = text_to_textnodes(block_text)
                html_children = [text_node_to_html_node(tn) for tn in text_nodes]
                bnode = ParentNode(f"h{heading_tag}",html_children, None)
                block_nodes.append(bnode)
        if btype == BlockType.PARAGRAPH:
            lines = block.splitlines()
            block_text = " ".join(line.strip() for line in lines)
            text_nodes = text_to_textnodes(block_text)
            html_children = [text_node_to_html_node(tn) for tn in text_nodes]
            bnode = ParentNode("p", html_children, None)
            block_nodes.append(bnode)
        if btype == BlockType.CODE:
            lines = block.splitlines()
            code_content = "\n".join(line.strip() for line in lines[1:-1])+"\n"
            text_node = TextNode(code_content, TextType.TEXT, None)
            html_children= text_node_to_html_node(text_node)
            code_node = ParentNode("code", [html_children], None)
            pre_node = ParentNode("pre",[code_node], None)
            bnode = pre_node
            block_nodes.append(bnode)
        if btype == BlockType.QUOTE:
            space_idx = space_index_finder(block)
            block_text = block[space_idx + 1:]
            text_nodes = text_to_textnodes(block_text)
            html_children = [text_node_to_html_node(tn) for tn in text_nodes]
            bnode = ParentNode("blockquote", html_children, None)
            block_nodes.append(bnode)

        if btype == BlockType.UNORDERED_LIST:
            lines = block.splitlines()
            li_nodes = []
            for line in lines:
                space_idx = space_index_finder(line)
                block_text = line[space_idx + 1:]
                text_nodes = text_to_textnodes(block_text)
                html_children = [text_node_to_html_node(tn) for tn in text_nodes]
                li_node = ParentNode("li", html_children, None)
                li_nodes.append(li_node)
            ul_node = ParentNode("ul",li_nodes, None)
            block_nodes.append(ul_node)

        if btype == BlockType.ORDERED_LIST:
            lines = block.splitlines()
            li_nodes = []
            for line in lines:
                space_idx = space_index_finder(line)
                block_text = line[space_idx + 1:]
                text_nodes = text_to_textnodes(block_text)
                html_children = [text_node_to_html_node(tn) for tn in text_nodes]
                li_node = ParentNode("li", html_children, None)
                li_nodes.append(li_node)
            ol_node = ParentNode("ol",li_nodes, None)
            block_nodes.append(ol_node)
    div_node = ParentNode('div',block_nodes, None)
    return div_node




#helper functions
def space_index_finder(block):
    space_idx = block.find(" ")
    if space_idx == -1:
        raise Exception("markdown does not follow correct structure, check previous code to fix issue")
    return space_idx

