import os
import shutil
import sys
from extract_title import extract_title
from markdown_to_html import markdown_to_html_node
from text_to_textnodes import *
from textnode import *

def main():
    if len(sys.argv) == 1:
        basepath = "/"
    else:
        basepath = sys.argv[1]
    out_dir = 'docs'
    copy_while_clobbering('static', out_dir)
    generate_pages_recursive("content", "template.html", out_dir, basepath)

def is_markdown_file(path):
    if not os.path.isfile(path):
      return False
    _, ext = os.path.splitext(path)
    return ext == '.md'

def switch_extension_to_html(path):
    head, ext = os.path.splitext(path)
    return head + ".html"

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    def walk_dirs(current_path):
        in_path = os.path.join(dir_path_content, current_path)
        if os.path.exists(in_path):
            for item in os.listdir(in_path):
                path = os.path.join(in_path, item)
                if is_markdown_file(path):
                    out_path = os.path.join(dest_dir_path, current_path, switch_extension_to_html(item))
                    generate_page(path, template_path, out_path, basepath)
                elif os.path.isdir(path):
                    walk_dirs(os.path.join(current_path, item))
    walk_dirs("")

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        markdown = f.read()
    with open(template_path) as f:
        template = f.read()
    content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    output = template.replace("{{ Title }}", title).replace("{{ Content }}", content)
    output = output.replace('href="/', f'href="{basepath}').replace('src="/', f"src=\"{basepath}")
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
