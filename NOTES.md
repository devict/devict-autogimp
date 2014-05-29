
AVALANCHE OF TERRIBLE NOTES FOR MY DEVICT TALK - AUTOMATING GIMP WITH PYTHON
============================================================================

## Scratchpad

2 approaches to using Python to automate GIMP
* Script-Fu - Scheme-based extension language implemented using TinyScheme
* Python-Fu - You guessed it - 
* GIMP-Python - set of Python modules acting as a wrapper to libgimp for authoring GIMP plug-ins.  Similar to Script-Fu, but you can use the full set of Python extension modules from the plug-in.  At least one of them is written in C, but it all appears to be included on GIMP for Linux and PC.  You'll just need to make sure you have Python installed and configured correctly.  On Linux, it's probably already installed :)

Other approaches to automating GIMP
* You could also script with Perl, C# or Tcl - but I have no idea about that stuff.  Not as much info after GIMP-Python gained in popularity.
  * I like learning Perl *every time* I need to use it.  But I don't *need* to use it here.  So I won't!
  * I really really don't want to have to compile for different OSs.  When script/Python is enough, why bother?
  * I don't know what Tcl is, and I'm not emotionally prepared to Google it yet.
  * If you're a good person, you've already got Python installed anyhow.

* There are more GUI - centric solutions.  Strictly batch-like, good for if you don't need to have programmatic control.
  * There exists David's Batch Processor ... or it looks like that's dead... oh, it's alive!  It's been a rollercoaster of emotion for me!
    * Downside to DBP is that the Linux version requires g++ and gimp dev packages for your exact GIMP version.  Windows installers do exist, but are not supported by original dev
  * BIMP - a little newer, started support with GIMP 2.6

For truely programmatic control, and bypassing view/usage of the GUI, Script-Fu and/or GIMP-Python seems like the way to go.

-------------------------------

Verify you can get to the Python-Fu console in Gimp - Filters->Python-Fu->Console
```
GIMP 2.8.10 Python Console
Python 2.7.6 (default, Mar 22 2014, 22:59:56) 
[GCC 4.8.2]
>>>
```
-------------------------------

To view GIMP functions at your disposal, go to "Help->Procedure Browser" ... should be consistent with function names accross Script-Fu, Gimp-Perl or other Gimp scripts.  For Python-Fu scripts, however, you'll need to replace hyphens "-" with underscore

A few gotchas while playing with gimp.pdb.file_png_save 
  * Omit the first (run-mode) parameter in your scripts, it's implicitly handled in pygimp
  * It does not like it when you offer "~/" as part of a path param.  Use os.path.expanduser(~/Desktop) to create path to user desktop which will by usable by pygimp scripts 

-------------------------------

Everything in Gimp, each funtion in a menu,  or field in a dialog, brush name, pattern name etc has its equivalent in the procedure browser

"gimp." allows user to call on GIMP's functionality.  "pdb." opens doors to all procedures exposed by Gimp via the "Procedure Database" ... same content as "Help->Procedure Browser" ... remember to use underscore, as hyphen means subtraction in Python, and as such is not allowed in function names.
  * As you will likely tire of prepending "gimp.pdb." to everything, try assigning an alias like 
  ```
  >>>g = gimp.pdb
  ```
    * might make more sense to limit this shortcut to scripts, as you lose TAB autocomplete or function listing from the console if alias is used.

-------------------------------

## Scripting
### Where to save your script
Typically store them locally, available only to your user profile "~/.gimp-x.x/plug-ins/"
  * On Linux, make sure your script has execute permissions 
  ```
  >chmod u+x example1.py
  ```
### Plugin Registration
Without registering, GIMP will not load the plugin, as it will not know where to put it or how to run it.

Skeleton of basic GIMP Python script:
```python
#!/usr/bin/env python

# This tells Python to load the Gimp module 
from gimpfu import *

# This is the function that will perform actual actions
def my_script_function() :
    print "Hello from my script!"
    return

# This is the plugin registration function
# I have written each of its parameters on a different line 
register(
    "my_first_script",    
    "My first Python-Fu",   
    "This script does nothing and is extremely good at it",
    "Michel Ardan", 
    "Michel Ardan Company", 
    "April 2010",
    "<Image>/MyScripts/My First Python-Fu", 
    "*", 
    [], 
    [],
    my_script_function,
    )

main()
```
NOTE: You *only* need to restart GIMP if you change the registration function.  Other changes can be tested without restarting GIMP.
  * TODO - SCREENSHOT OF THIS EXAMPLE

In register function example, in order

1. plugin's main function name - as found by GIMP's Procedure Browser
  1. can be called by other plugins using this name, even in languages other than Python.
1. Plugin's documentation name, also appears in browser, should briefly describe your plugin
1. Plugin's Help, more detailed description
1. Author's name
1. Any Copyright info
1. Date released
1. Path in the Menu where your plugin should be found
1. Image types supported by your plugin
1. Input parameters - TODO: email author about this missing definition
1. results sent back by your plugin

Specifically, regarding the Menu path - if you don't specify it correctly, you won't be able to find a menu for your plugin.
  * You could put it in the Filters menu by changing it to 

  ```
  "<Image>"/Filters/MyScripts/My First Python-Fu
  ```
  * Other options instead of <Image> include Toolbox, Layers, Channels, Vectors, Colormap, Load, Save, Brushes, Gradients, Palettes, Patterns and Buffers
  * Possible Image types are * for all, RBG, RGBA, GRAY, or INDEXED
  * to support both RBG and RGBA, you can write "RGB*"
  * Even if you provide [], empty list of parameters, GIMP automatically adds 3 parameters
    * 2nd is current image, third is current drawable object/layer
    * first is "run mode" - either "RUN-NONINTERACTIVE" or "RUN-INTERACTIVE" ... we'll focus on the former
    * if you define a Toolbox menu entry, only run-mode param is required, meaning your plugin will not require an image, but will perhaps generate an image

Modified first plugin example - allowing user to input values:
```python
#!/usr/bin/env python


# This tells Python to load the Gimp module 
from gimpfu import *

# This is the function that will perform actual actions
def my_script_function(image, drawable, text_value, int_value) :
    print "Hello from my script!"
    print "You sent me this text: "+text_value
    print "You sent me this number: %d"%int_value
    return

# This is the plugin registration function
register(
    "my_first_script",    
    "My first Python-Fu",   
    "This script does nothing and is extremely good at it",
    "Michel Ardan", 
    "Michel Ardan Company", 
    "April 2010",
    "<Image>/MyScripts/My First Python-Fu", 
    "*", 
    [
      (PF_STRING, 'some_text', 'Some text input for our plugin', 'Write something'),
      (PF_INT, 'some_integer', 'Some number input for our plugin', 2010)
    ], 
    [],
    my_script_function,
    )

main()
```


-------------------------------

VOCAB

Drawable - A Channel or Layer
Images - containers for layers, other objects like channels, paths, selections...

## Outline

## PLUGS

## Links
http://www.gimp.org/docs/python/index.html
http://www.w3.org/TR/PNG-Chunks.html
