
AVALANCHE OF TERRIBLE NOTES FOR MY DEVICT TALK - AUTOMATING GIMP WITH PYTHON
============================================================================

## Scratchpad

2 approaches to using Python to automate GIMP
* Script-Fu - Scheme-based extension language implemented using TinyScheme
* Python-Fu - You guessed it - 
* GIMP-Python - set of Python modules acting as a wrapper to libgimp for authoring GIMP plug-ins.  Similar to Script-Fu, but you can use the full set of Python extension modules from the plug-in.  At least one of them is written in C, but it all appears to be included on GIMP for Linux and PC.  You'll just need to make sure you have Python installed and configured correctly.  On Linux, it's probably already installed :)

Other approaches to automating GIMP
* You could also script with Perl or Tcl - but I have no idea about that stuff.  Not as much info after GIMP-Python gained in popularity.
  * I like learning Perl *every time* I need to use it.  But I don't *need* to use it here.  So I won't!
  * I don't know what Tcl is, and I'm not emotionally prepared to Google it yet.

* There are more GUI - centric solutions.  Strictly batch-like, good for if you don't need to have programmatic control.
  * There exists David's Batch Processor ... or it looks like that's dead... oh, it's alive!  It's been a rollercoaster of emotion for me!
    * Downside to DBP is that the Linux version requires g++ and gimp dev packages for your exact GIMP version.  Windows installers do exist, but are not supported by original dev
  * BIMP - a little newer, started support with GIMP 2.6

For truely programmatic control, and bypassing view/usage of the GUI, Script-Fu and/or GIMP-Python seems like the way to go.

## Outline

## PLUGS

## Links
