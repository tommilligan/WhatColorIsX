.. _whatcoloris_command:

``whatcoloris`` command
=======================

The :ref:`whatcoloris_command` can be run from the command-line, and provides quick
use of the :py:func:`WhatColorIsX.whatcolorisx.color` method.
    
Usage
-----
::
    
    $ whatcoloris -h
    usage: whatcoloris [-h] [-b] [-m {average_color,common_color}]
                       [--images_to_try IMAGES_TO_TRY]
                       x

    Returns colour of string based on Google image search.

    positional arguments:
      x                     string/file to find colour of

    optional arguments:
      -h, --help            show this help message and exit
      -b, --bright_hue      return a bright colour; hsl=(x,1.0,0.5)
      -m {average_color,common_color}, --method {average_color,common_color}
                            Helper method to use for colour picking. Defaults to
                            average
      --images_to_try IMAGES_TO_TRY
                            number of images to try processing before erroring
