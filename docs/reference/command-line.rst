.. _whatcoloris_command:

``whatcoloris`` command
=======================

The :ref:`whatcoloris_command` can be run from the command-line, and provides a direct
connection to the :py:func:`WhatColorIsX.whatcoloris` function.
    
Usage
-----
::
    
    $ whatcoloris -h
    usage: whatcoloris-script.py [-h] [-b] [-f] [--images_to_try IMAGES_TO_TRY] x

    Returns colour of string based on Google image search.

    positional arguments:
      x                     string to find colour of

    optional arguments:
      -h, --help            show this help message and exit
      -b, --bright_hue      return a bright colour; hsl=(x,1.0,0.5)
      -f, --is_file         treat x as a file path to open locally
      --images_to_try IMAGES_TO_TRY
                            number of images to try processing before erroring
