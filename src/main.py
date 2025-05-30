import os
import shutil
from extract_title import extract_title
from markdown_to_html import markdown_to_html_node
from text_to_textnodes import *
from textnode import *

def main():
    copy_while_clobbering('static', 'public')
    generate_page("content/index.md", "template.html", "public/index.html")


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        markdown = f.read()
    with open(template_path) as f:
        template = f.read()
    content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    output = template.replace("{{ Title }}", title).replace("{{ Content }}", content)
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(output)


def copy_while_clobbering(source_dir, dest_dir):
    if os.path.exists(dest_dir):
        for item in os.listdir(dest_dir):
            to_delete = os.path.join(dest_dir, item)
            print("Removing " + to_delete)
            if os.path.isfile(to_delete):
                os.remove(to_delete)
            else:
                shutil.rmtree(to_delete)
    else:
        os.mkdir(dest_dir)
    if os.path.exists(source_dir):
        for item in os.listdir(source_dir):
            src = os.path.join(source_dir, item)
            dest = os.path.join(dest_dir, item)
            if os.path.isfile(src):
                print("Copying file " + src + " to " + dest)
                shutil.copy(src, dest)
            elif os.path.isdir(src):
                if not os.path.exists(dest):
                    os.mkdir(dest)
                copy_while_clobbering(src, dest)


if __name__ == '__main__':
    main()
