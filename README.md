devict-autogimp
===============

Official cradle and final resting place of content for my devICT talk "Automating GIMP using Python"

Addressing questions that came up during the talk
-------------------------------------------------
Dominic Canare - can GTK be used to create GUI dialogs for your scripts?
    It would appear so.  From /usr/lib/gimp/2.0/python/gimpfu.py there are some choice imports
        ```python
            import pygtk
            pygtk.require('2.0')

            import gimpui
            import gtk
        ```
