import os
import shutil
import sys
from static_to_public import copy_directory_contents, generate_pages_recursive

def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"
    print(basepath)
    if os.path.exists("docs"):
        # Valid folder location, clean it out
        shutil.rmtree("docs")
    
    copy_directory_contents("static", "docs")
    generate_pages_recursive(basepath, "content", "template.html", "docs")

main()