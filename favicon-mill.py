#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, re, glob
from gimpfu import *
from gimpenums import *

# Script body
def start_the_mill(file_path, size_list) :
    # transmit error messages to gimp console
    gimp.pdb.gimp_message_set_handler( ERROR_CONSOLE )

    full_path = os.path.expanduser(file_path)

    image = pdb.gimp_file_load(full_path, full_path)
    drawable = pdb.gimp_image_get_active_layer(image)
    original = image

    directory = os.path.expanduser("~/Desktop")

    sizes = [int(x) for x in size_list.split(',')]
    desc_sizes= sorted(sizes, key=int, reverse=True)

    for s in desc_sizes:
        call_favicon_resize(original, drawable, directory, s)

    return

def call_favicon_resize(image, drawable, target_dir, new_size) :
    pdb.python_fu_favicon_resize(image, drawable, target_dir, new_size)

    return

# Registration 
register(
    "python_fu_favicon_mill",
    "Take an image and churn out multiple favicons",
    "Take whatever image is loaded, and export a series of favicons, based on a list of dimensions, to ~/Desktop/favicon-X.png !!",
    "Jim Rice",
    "Jiiimbot Unincorporated",
    "May 2014",
    "<Toolbox>/Image/Favicon Mill",
    "*",
    [
        (PF_STRING, "file_path", "Absolute path to source file", "/home/user/example.png"),
        (PF_STRING, "size_list", "Comma-separated list of desired favicon sizes", "32,57,72,96,120,128,144,152,195,228")
    ],
    [],
    start_the_mill,
)

main()
