WhatColorIsX
============

Python script which takes any string and returns a hex colour string, using Google
image search.

master: .. image:: https://travis-ci.org/tommilligan/WhatColorIsX.svg?branch=master
    :target: https://travis-ci.org/tommilligan/WhatColorIsX
dev: .. image:: https://travis-ci.org/tommilligan/WhatColorIsX.svg?branch=dev
    :target: https://travis-ci.org/tommilligan/WhatColorIsX

Installation
------------

::

    pip install WhatColorIsX

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
^^^^^^^^^^^^^^^^^^^^^^
::

    from WhatColorIsX import whatcoloris
    
    brick_color = whatcoloris('brick')
    fish_color_bright = whatcoloris('fish', bright_hue=True)

Run from the command line
^^^^^^^^^^^^^^^^^^^^^^^^^

When installed, the script can be accessed with the ``whatcoloris`` command

::

    whatcoloris sky
    >>> #769ab8
    ```
    It can also be called directly
    ```
    python WhatColorIsX.py grass -b
    >>> #65ff00


Additional Scripts
------------------
These scripts will not be installed automatically, but can be downloaded
directly from GitHub if desired

xml
^^^

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

    python xmlInterface.py input.xml output.xml bar name color

**output.xml**::

    <foo>
        <bar>
            <name>sun</name>
            <color>#873107</color>
        </bar>
    </foo>

