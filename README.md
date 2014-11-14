devict-autogimp
===============

Official cradle and final resting place of content for my devICT talk "Automating GIMP using Python"

Credits and links
-----------------



Addressing questions that came up during the talk
-------------------------------------------------
#Dominic Canare - can GTK be used to create GUI dialogs for your scripts?
    It would appear so.  From /usr/lib/gimp/2.0/python/gimpfu.py there are some choice imports
```python
import pygtk
pygtk.require('2.0')

import gimpui
import gtk
```
#Dominic Canare - again - can you modify raster images etc... basically draw programmatically 
Pretty much any gimp procedure can be done via plugin, AFAIK.  Here's a possible example?

http://coderazzi.net/python/gimp/pythonfu.html

#Eddy? - Does it use its own Python, or the system Python Library?
It is specifically using the packed-in Python for the Gimp version you're running.  You can verify what version it is by running the Python console from Filters -> Python-fu -> console.  So if you want to use a different (newer) version of Python to do some really heavy lifting, I'd suppose you could "tee up" your work using the Gimp-packed Python, then pass along work to whatever script you like, in whatever language you like?  If I'm wrong, file an issue and I'll eat crow.  Name it "JIM SHOULD EAT CROW."
