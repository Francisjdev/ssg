from textnode import TextType, TextNode
import re
from extract_markdown import extract_markdown_images, extract_markdown_links
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []  
    for node in old_nodes:
        if node.text_type == TextType.TEXT:  
            if delimiter in node.text:  
                if node.text.count(delimiter) % 2 != 0:
                    raise Exception("Unmatched delimiter")
                results = node.text.split(delimiter)
                for idx in range(len(results)):
                    if idx % 2 == 0:
                        node = TextNode(results[idx], TextType.TEXT)
                    else:
                        node = TextNode(results[idx], text_type)  
                    new_nodes.append(node) 
            else:
                new_nodes.append(node)  
        else:
            new_nodes.append(node) 
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node) 
            continue
            
        current_text = node.text
        images = extract_markdown_images(current_text)
        
        if not images:  
            new_nodes.append(node)  
            continue
            
        for image in images:  
            sections = current_text.split(f"![{image[0]}]({image[1]})", 1)
            new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            current_text = sections[1]
            
        if current_text:  
            new_nodes.append(TextNode(current_text, TextType.TEXT))
            
    return new_nodes 
def split_nodes_link(old_nodes):
    new_nodes=[]
    
    for node in old_nodes:
            if node.text_type != TextType.TEXT:
                new_nodes.append(node) 
                continue

            current_text=node.text
            links = extract_markdown_links(current_text)
            if not links:  
                new_nodes.append(node)  
                continue
            for link in links:
                
                sections = current_text.split(f"[{link[0]}]({link[1]})",1)
                new_nodes.append(TextNode(sections[0],TextType.TEXT))
                new_nodes.append(TextNode(link[0],TextType.LINK,link[1]))
                current_text = sections[1]
            if current_text:
                    new_nodes.append(TextNode(current_text, TextType.TEXT))
    return new_nodes       
    
def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]

    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
  
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    
    nodes = split_nodes_image(nodes)
    
    nodes = split_nodes_link(nodes)
    
    return nodes

