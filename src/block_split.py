

def markdown_to_blocks(markdown):
    pre_blocks = markdown.split("\n\n")
    blocks = []
    for block in pre_blocks:
        stripped_block = block.strip() 
        if stripped_block: 
            blocks.append(stripped_block)
        stripped_block = block.strip()
    
    return blocks

