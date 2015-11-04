WhatColorIsX
============

Python script which takes any string and returns a hex colour string, using Google
image search.

master:
"""""""

.. image:: https://img.shields.io/pypi/pyversions/WhatColorIsX.svg
    :target: https://pypi.python.org/pypi/WhatColorIsX
    :alt: Supported Python versions

.. image:: http://img.shields.io/pypi/v/WhatColorIsX.svg?style=flat
    :target: https://pypi.python.org/pypi/WhatColorIsX/
    :alt: Latest PyPI version

.. image:: https://travis-ci.org/tommilligan/WhatColorIsX.svg?branch=master
    :target: https://travis-ci.org/tommilligan/WhatColorIsX
    :alt: Travis CI build status
    
.. image:: https://coveralls.io/repos/tommilligan/WhatColorIsX/badge.svg?branch=master&service=github
    :target: https://coveralls.io/github/tommilligan/WhatColorIsX?branch=master
    :alt: Coveralls coverage status
    
dev:
""""

.. image:: https://travis-ci.org/tommilligan/WhatColorIsX.svg?branch=dev
    :target: https://travis-ci.org/tommilligan/WhatColorIsX
    :alt: Travis CI build status

.. image:: https://coveralls.io/repos/tommilligan/WhatColorIsX/badge.svg?branch=dev&service=github
    :target: https://coveralls.io/github/tommilligan/WhatColorIsX?branch=dev
    :alt: Coveralls coverage status


Installation
------------

::

    $ pip install WhatColorIsX

You may find you need to ``pip install Pillow`` as a dependency first, although
it will be attempted automatically.

Usage
-----

Input can be any string. Output is a 6-digit hex colour value (#[0-9a-f]{6}).

WhatColorIsX returns an accurate colour value by default. If bright_hue is set
to ``True``, it is guaranteed that a bright colour will be returned. If
bright_hue is not set, it is likely that some whites, greys or blacks will be
returned.

The `colour module`_ can be used to easily perform further alterations.

.. _colour module: https://github.com/vaab/colour

Import to your project
""""""""""""""""""""""
::

    from WhatColorIsX import whatcoloris
    
    brick_color = whatcoloris('brick')
    fish_color_bright = whatcoloris('fish', bright_hue=True)
    my_cat_colour = whatcoloris('my images/cat.jpg', is_file=True)

Run from the command line
"""""""""""""""""""""""""

When installed, the script can be accessed with the ``whatcoloris`` command. Usage::

    whatcoloris [-h] [-b] [-f] x

    positional arguments:
      x                 string to find colour of

    optional arguments:
      -h, --help        show this help message and exit
      -b, --bright_hue  return a bright colour; hsl=(x,1.0,0.5)
      -f, --is_file     treat x as a file path to open locally


::

    $ whatcoloris sky
    #769ab8
    $ whatcoloris -f images/dog.png
    #6c5a47

It can also be called directly::

    $ python WhatColorIsX.py grass -b
    #65ff00


Additional Scripts
------------------
These scripts will not be installed automatically, but can be downloaded
directly from GitHub if desired

xml
"""

``xmlInterface.py`` allows ``WhatColorIsX`` to interface with a correctly
formatted XML file. This allows multiple values to be queued for processing.
See the ``xml`` folder for the script, example input and output XML files,
and the command format used to run it. Raise the ``-h`` flag for detailed
information.

**input.xml**::

    <foo>
        <bar>
            <name>sun</name>
        </bar>
    </foo>

**command**::

    $ python xmlInterface.py input.xml output.xml bar name color

**output.xml**::

    <foo>
        <bar>
            <name>sun</name>
            <color>#873107</color>
        </bar>
    </foo>

