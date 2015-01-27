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


# ~~TODO~~ - Link dump from the guides I favorited and organized as such after my talk

* [Gimp Scripting: Python objects in practice](http://gimpbook.com/scripting/slides30/pyobjectcode.html)
* [audreyr's cheat sheet to favicon sizes/types](https://github.com/audreyr/favicon-cheat-sheet)
* [Making multi-resolution favicons in GIMP - Clara Tse](http://kirinyan.net/making-multi-resolution-favicons-in-gimp/)
* [Python Programming/Functions - en.wikibooks.org](http://en.wikibooks.org/wiki/Python_Programming/Functions)
* [Gimp Script: Save as PNG - defron.org](http://blog.defron.org/2013/01/gimp-script-save-as-png.html)
* [PNG Specification - libpng.org](http://www.libpng.org/pub/png/spec/iso/)
* [PNG Specification - w3.org](http://www.w3.org/TR/PNG-Chunks.html)
* [GIMP Resize Script example in Python-fu - zwell.net](http://zwell.net/content/pygimp.html)
* [Python os.path - docs.python.org](https://docs.python.org/2/library/os.path.html)
* [Other os.path guide that answered a few questions for me - effbot.org](http://effbot.org/librarybook/os-path.htm)
* [Stack Overflow question whose answer served as a good, concise guide to creating a GIMP batch script](https://stackoverflow.com/questions/12662676/writing-a-gimp-python-script/12663785#12663785)
* [Script-fu tutorial in case you really really like Scheme - seul.org](http://www.seul.org/~grumbel/gimp/script-fu/script-fu-tut.html)
* [Gimp Python Documentation, very broad overview - gimp.org](http://www.gimp.org/docs/python/)
* [Gimp function reference, so you know what's possible to script! - gimp.cp-dev.com](http://gimp.cp-dev.com/manual/gimp-function-reference.html)
* [Stack Overflow question about using split to parse string of comma-separated values, as we did in the demo.](http://stackoverflow.com/questions/3477502/pythonic-method-to-parse-a-string-of-comma-separated-integers-into-a-list-of-i)
* [Sorting in Python](https://wiki.python.org/moin/HowTo/Sorting)
* [GIMP Library Reference Manual entry for image scale - developer.gimp.org](http://developer.gimp.org/api/2.0/libgimp/libgimp-gimpimage.html#gimp-image-scale)
* [GIMP Library Reference Manual, so you know what you can script! - developer.gimp.org](http://developer.gimp.org/api/2.0/libgimp/index.html)
* [GIMP Batch Mode - gimp.org](http://www.gimp.org/tutorials/Basic_Batch/)
* [Thread about chasing down what version of Python GIMP is using](http://gimpforums.com/thread-python-fu-no-show-mac)

## Addressing questions that came up during the talk

**Dominic Canare - can GTK be used to create GUI dialogs for your scripts?**

*    It would appear so.  From /usr/lib/gimp/2.0/python/gimpfu.py there are some choice imports
```python
import pygtk
pygtk.require('2.0')

import gimpui
import gtk
```
*    Maybe that wasn't what you're after?  What about this business??!?
   * [Section 3 of Writing a Plug-in from developer.gimp.org](http://developer.gimp.org/writing-a-plug-in/3/)
   * [Template script demonstrating all "included" GUI building options](http://gimpbook.com/scripting/gimp-script-templates/pyui.py)

**Dominic Canare - again - can you modify raster images etc... basically draw programmatically**

*    Pretty much any gimp procedure can be done via plugin, AFAIK.  Here's a possible example?

http://coderazzi.net/python/gimp/pythonfu.html

**Eddy? - Does it use its own Python, or the system Python Library?**

*    It is specifically using the packed-in Python for the Gimp version you're running.  You can verify what version it is by running the Python console from Filters -> Python-fu -> console.  So if you want to use a different (newer) version of Python to do some really heavy lifting, I'd suppose you could "tee up" your work using the Gimp-packed Python, then pass along work to whatever script you like, in whatever language you like?  If I'm wrong, file an issue and I'll eat crow.  Name it "JIM SHOULD EAT CROW."
