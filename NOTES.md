
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

-------------------------------

Everything in Gimp, each funtion in a menu,  or field in a dialog, brush name, pattern name etc has its equivalent in the procedure browser

-------------------------------

VOCAB

Drawable - A Channel or Layer
Images - containers for layers, other objects like channels, paths, selections...

## Outline

## PLUGS

## Links
http://www.gimp.org/docs/python/index.html
