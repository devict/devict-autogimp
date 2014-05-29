#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, re, glob
from gimpfu import *
from gimpenums import *

# Script body
def start_the_mill(image, drawable) :
    # transmit error messages to gimp console
    gimp.pdb.gimp_message_set_handler( ERROR_CONSOLE )

    newWidth = 28 
    newHeight = 28

    original = image
    filename = "derp-28.png"
    directory = os.path.expanduser("~/Desktop")
    gimp.pdb.gimp_image_scale( original, newWidth, newHeight )
    gimp.pdb.file_png_save( original, drawable, directory+"/"+filename, filename, 0, 9, 0, 0, 0, 1, 1 )

    return

# Registration 
register(
    "python_fu_favicon_derp_28",
    "Demo some image resizing and export via GUI",
    "Take whatever image is loaded, chop it to 28x28 and export it to ~/Desktop/derp-28.png !!",
    "Jim Rice",
    "Jiiimbot Unincorporated",
    "May 2014",
    "<Image>/Derp/derp 28",
    "*",
    [],
    [],
    start_the_mill,
)

main()
