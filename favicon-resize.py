#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, re, glob
from gimpfu import *
from gimpenums import *

# Script body
def resize_it(image, drawable, target_dir, new_size) :
    # transmit error messages to gimp console
    gimp.pdb.gimp_message_set_handler( ERROR_CONSOLE )

    newWidth = new_size 
    newHeight = new_size 

    original = image
    filename = "favicon-" + str(newWidth) + ".png" 
    directory = os.path.expanduser(target_dir)
    gimp.pdb.gimp_image_scale( original, newWidth, newHeight )
    gimp.pdb.file_png_save( original, drawable, directory+"/"+filename, filename, 0, 9, 0, 0, 0, 1, 1 )

    return

# Registration 
register(
    "python_fu_favicon_resize",
    "resize favicons",
    "Take PNG and resize it to square dimensions. Use it correctly!!",
    "Jim Rice",
    "Jiiimbot Unincorporated",
    "May 2014",
    "<Image>/Image/Favicon Resize",
    "*",
    [
        (PF_STRING, "target_directory", "Target Directory", "~/Desktop"),
        (PF_INT, "new_size", "New Size", "120")
    ],
    [],
    resize_it,
)

main()
