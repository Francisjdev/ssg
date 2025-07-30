
import shutil
from textnode import TextNode, TextType
from extract_markdown import extract_title_markdown
import os
from block_to_html import markdown_to_html_node

def main():
    remove_dir('public')
    copy_folder('static', 'public')
    auto_generation('content', 'public')
   # generate_page('content/index.md', 'template.html', 'public/index.html')
   # generate_page('content/blog/glorfindel/index.md', 'template.html', 'public/blog/`glorfindel/index.html')
   # generate_page('content/blog/tom/index.md', 'template.html', 'public/blog/tom/index.html')
   # generate_page('content/blog/majesty/index.md', 'template.html', 'public/blog/majesty/index.html')
   # generate_page('content/contact/index.md', 'template.html', 'public/contact/index.html')

def remove_dir(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.mkdir(path)
def copy_folder(source,destination):
    for elem in os.listdir(source):
        src_path = os.path.join(source, elem)
        dst_path = os.path.join(destination, elem)
        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)
        elif os.path.isdir(src_path):
            os.mkdir(dst_path) 
            copy_folder(src_path, dst_path)

def auto_generation(source, destination):
    for elem in os.listdir(source):
        src_path = os.path.join(source, elem)
        dst_path = os.path.join(destination, elem)
        if os.path.isfile(src_path):
            dst_path = dst_path.replace('content/', 'public/')
            dst_path = dst_path.replace('.md', '.html')
            generate_page(f'{src_path}','template.html',f'{dst_path}' )
        elif os.path.isdir(src_path):
            src_path = os.path.join(source, elem)
            dst_path = os.path.join(destination, elem)
            auto_generation(src_path, dst_path)
       
            

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    file = open(from_path)
    template_file = open(template_path)
    md = file.read()
    template = template_file.read()
    file.close()
    template_file.close()
    html = markdown_to_html_node(md).to_html()
    title = extract_title_markdown(md)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
# Inside your function:
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    output_file = open(dest_path, 'w')
    output_file.write(template)
    output_file.close()



main()