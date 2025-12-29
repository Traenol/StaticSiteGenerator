import os
import shutil
from markdown_to_htmlnode import markdown_to_html_node
from markdowntools import extract_title
from blocks import block_to_block_type, BlockType

def copy_directory_contents(src, dest):
    # Check if destination folder exists
    if os.path.exists(dest):
        # Valid folder location, clean it out
        shutil.rmtree(dest)
    
    # Create the folder in place
    print(f"Creating Folder {dest}")
    os.mkdir(dest)

    # Iterate over files and directories to copy

    for item in os.listdir(src):
        src_item_path = src + "/" + item
        dest_item_path = dest + "/" + item
        if os.path.isfile(src_item_path):
            print(f"Copying {src_item_path} to {dest_item_path}")
            shutil.copy(src_item_path, dest_item_path)
        elif os.path.isdir(src_item_path):
            copy_directory_contents(src_item_path, dest_item_path)

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # read the markdown file from from_path
    try:
        with open(from_path, mode="r") as file:
            markdown = file.read()
    except Exception:
        return f"Error: unable to read the file: {from_path}"
    
    # read the template from template_path
    try:
        with open(template_path, mode="r") as file:
            template = file.read()
    except Exception:
        return f"Error: unable to read the file: {template_path}"
    
    html = markdown_to_html_node(markdown).to_html()
    title = ""
    for line in markdown.splitlines():
        if block_to_block_type(line) == BlockType.HEADING:
            title = extract_title(line)
            break
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    
    # write finished html to dest_path
    try:
        if not os.path.exists(dest_path.rsplit("/",1)[0]):
            os.mkdir(dest_path.rsplit("/",1)[0])
        with open(dest_path, mode="w") as file:
            file.write(template)
    except Exception:
        return f"Error: unable to write the file: {dest_path}"

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        print(f"Creating Directory: {dest_dir_path}")
        os.mkdir(dest_dir_path)
    for item in os.listdir(dir_path_content):
        if str(item).endswith(".md"):
            file_name = str(item).replace(".md", ".html")
            generate_page(dir_path_content + "/" + item, template_path, dest_dir_path + "/" + file_name)
        if os.path.isdir(dir_path_content + '/' + item):
            generate_pages_recursive(dir_path_content + "/" + item, template_path, dest_dir_path + "/" + item)
