import os
import shutil
from static_to_public import copy_directory_contents, generate_pages_recursive

def main():
    if os.path.exists("public"):
        # Valid folder location, clean it out
        shutil.rmtree("public")
    
    copy_directory_contents("static", "public")
    generate_pages_recursive("content", "template.html", "public")

main()