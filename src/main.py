import os
import shutil
from text_to_textnodes import *
from textnode import *

def main():
    copy_while_clobbering('static', 'foo')

def copy_while_clobbering(source_dir, dest_dir):
    if os.path.exists(dest_dir):
        for item in os.listdir(dest_dir):
            to_delete = os.path.join(dest_dir, item)
            print("Removing " + to_delete)
            # shutil.rmtree(to_delete)
    else:
        os.mkdir(dest_dir)
    if os.path.exists(source_dir):
        for item in os.listdir(source_dir):
            src = os.path.join(source_dir, item)
            dest = os.path.join(dest_dir, item)
            if os.path.isfile(src):
                print("Copying file " + src + " to " + dest)
                # shutil.copy(src, dest)
            elif os.path.isdir(src):
                if not os.path.exists(dest):
                    os.mkdir(dest)
                copy_while_clobbering(src, dest)


if __name__ == '__main__':
    main()
