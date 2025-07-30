import re

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
    return matches

def extract_title_markdown(text):
    lines = text.splitlines()
    for line in lines:
        if line.startswith("# "):
            h1 = line.lstrip("# ")
            h1 = h1.strip()
            return h1
    raise Exception ('no title found')

