from enum import Enum


class BlockType(Enum):
    PARAGRAPH="paragraph"
    HEADING ="heading"
    CODE="code"
    QUOTE="quote"
    UNORDERED_LIST="unordered_list"
    ORDERED_LIST="ordered_list"

def block_to_block_type(markdown):
    if markdown.startswith(('# ', "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if markdown.startswith("```") and markdown.endswith("```"):
        return BlockType.CODE
    lines = markdown.splitlines()
    if all(line.startswith(">") for line in lines):
        return BlockType.QUOTE
    if all(line.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST 
    is_ordered_list = True
    counter = 1
    for i, line in enumerate(lines):
        idx = line.find(".")
        is_valid_ordered_list_line = (
            idx != -1 and 
            idx + 1 < len(line) and 
            line[:idx].isdigit() and 
            line[idx+1] == " "
        )
        
        if not is_valid_ordered_list_line:
            is_ordered_list = False
            break 
        
        try:
            line_num = int(line[:idx])
        except ValueError: 
            is_ordered_list = False
            break
            
        if line_num != counter:
            is_ordered_list = False
            break 
        counter += 1
            
    if is_ordered_list and lines: 
        return BlockType.ORDERED_LIST
    elif not lines and is_ordered_list: 
        return BlockType.PARAGRAPH 
    
    return BlockType.PARAGRAPH 