
import shutil
import sys
from textnode import TextNode, TextType
from extract_markdown import extract_title_markdown
import os
from block_to_html import markdown_to_html_node
import re

def main():
    if len(sys.argv)>1:
        base_path = sys.argv[1]
    else:
        base_path = '/'
    print(base_path)
    remove_dir('docs')
    copy_folder('static', 'docs')
    auto_generation('content', 'docs', base_path)

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

def auto_generation(source, destination, basepath):
    for elem in os.listdir(source):
        src_path = os.path.join(source, elem)
        dst_path = os.path.join(destination, elem)
        if os.path.isfile(src_path):
            dst_path = dst_path.replace('content/', 'public/')
            dst_path = dst_path.replace('.md', '.html')
            generate_page(f'{src_path}','template.html',f'{dst_path}',basepath )
        elif os.path.isdir(src_path):
            src_path = os.path.join(source, elem)
            dst_path = os.path.join(destination, elem)
            auto_generation(src_path, dst_path, basepath)
       
            

def generate_page(from_path, template_path, dest_path,basepath):
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
    import re

    if basepath == '/':
        template = template.replace('href="/', 'href="/')
        template = template.replace('src="/',  'src="/')
    else:
        
        template = re.sub(r'href="/', f'href="{basepath}/', template)
        template = re.sub(r'src="/', f'src="{basepath}/', template)
      
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    output_file = open(dest_path, 'w')
    output_file.write(template)
    output_file.close()



main()