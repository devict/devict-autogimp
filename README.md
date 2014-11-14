# devict-autogimp

*Official cradle and final resting place of content for my devICT talk "Automating GIMP using Python"*

## Credits and links
**[Frédéric Jaume](http://www.exp-media.com/)** - *I basically ended up duplicating his blog posts when I got started, and summarized them as I continued to find them in my Google searches!  He said that was OK, and I promised to link him and his helpful guides!!*
 * Python-Fu Extending Gimp with Python - [Part 1](http://www.exp-media.com/content/extending-gimp-python-python-fu-plugins-part-1), [Part 2](http://www.exp-media.com/content/extending-gimp-python-python-fu-plugins-part-2), [Part 3](http://www.exp-media.com/content/extending-gimp-python-python-fu-plugins-part-3), [Part 4](http://www.exp-media.com/content/extending-gimp-python-python-fu-plugins-part-4)

**Select Links from Frédéric's guides**

* [Official Gimp Python documentation](http://www.gimp.org/docs/python/index.html)
* [Python.org tutorial](http://docs.python.org/tutorial/index.html)
* [Python.org reference](http://docs.python.org/reference/index.html)
* [Gimp Basic Batch guide](http://www.gimp.org/tutorials/Basic_Batch/)


# TODO - Link dump from the guides I favorited and organized as such after my talk

## Addressing questions that came up during the talk

**Dominic Canare - can GTK be used to create GUI dialogs for your scripts?**

*    It would appear so.  From /usr/lib/gimp/2.0/python/gimpfu.py there are some choice imports
```python
import pygtk
pygtk.require('2.0')

import gimpui
import gtk
```
**Dominic Canare - again - can you modify raster images etc... basically draw programmatically**

*    Pretty much any gimp procedure can be done via plugin, AFAIK.  Here's a possible example?

http://coderazzi.net/python/gimp/pythonfu.html

**Eddy? - Does it use its own Python, or the system Python Library?**

*    It is specifically using the packed-in Python for the Gimp version you're running.  You can verify what version it is by running the Python console from Filters -> Python-fu -> console.  So if you want to use a different (newer) version of Python to do some really heavy lifting, I'd suppose you could "tee up" your work using the Gimp-packed Python, then pass along work to whatever script you like, in whatever language you like?  If I'm wrong, file an issue and I'll eat crow.  Name it "JIM SHOULD EAT CROW."
