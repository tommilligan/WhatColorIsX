WhatColorIsX
============

.. image:: https://img.shields.io/pypi/pyversions/WhatColorIsX.svg
    :target: https://pypi.python.org/pypi/WhatColorIsX
    :alt: Supported Python versions

.. image:: http://img.shields.io/pypi/v/WhatColorIsX.svg?style=flat
    :target: https://pypi.python.org/pypi/WhatColorIsX/
    :alt: Latest PyPI version

.. image:: https://readthedocs.org/projects/whatcolorisx/badge/?version=stable
    :target: http://whatcolorisx.readthedocs.org/en/stable/?badge=stable
    :alt: ReadTheDocs Documentation Status
    
.. image:: https://travis-ci.org/tommilligan/WhatColorIsX.svg?branch=master
    :target: https://travis-ci.org/tommilligan/WhatColorIsX
    :alt: Travis CI build status
    
.. image:: https://coveralls.io/repos/tommilligan/WhatColorIsX/badge.svg?branch=master&service=github
    :target: https://coveralls.io/github/tommilligan/WhatColorIsX?branch=master
    :alt: Coveralls coverage status

Python script which takes any string and returns a hex colour string, using Google
image search.

Installation
------------

::

    $ pip install WhatColorIsX

You may find you need to ``pip install Pillow`` as a dependency first, although
it will be attempted automatically.

Docs
----

Full documentation is hosted at http://whatcolorisx.readthedocs.org

Usage
-----

Input can be any string. Output is a 6-digit hex colour value (#[0-9a-f]{6}).

WhatColorIsX returns an accurate colour value by default. If bright_hue is set
to ``True``, it is guaranteed that a bright colour will be returned. If
bright_hue is not set, it is likely that some whites, greys or blacks will be
returned.

Files can have their colour detected by raising the ``-f`` flag and providing the
path to the image file (see example below).

The number of images google searched for before giving up and erroring can be
specified with ``--images_to_try`` and an integer. Default is 10.

The `colour module`_ can be used to easily perform further alterations.

.. _colour module: https://github.com/vaab/colour

Import to your project
^^^^^^^^^^^^^^^^^^^^^^
::

    from WhatColorIsX import whatcoloris
    
    brick_color = whatcoloris('brick')
    fish_color_bright = whatcoloris('fish', bright_hue=True)
    my_cat_colour = whatcoloris('my images/cat.jpg', is_file=True)
    pineapple_colour = whatcoloris('pineapple', images_to_try=100)

Run from the command line
^^^^^^^^^^^^^^^^^^^^^^^^^

When installed, the script can be accessed with the ``whatcoloris`` command. Usage::

    whatcoloris [-h] [-b] [-f] x

    positional arguments:
      x                 string to find colour of

    optional arguments:
      -h, --help        show this help message and exit
      -b, --bright_hue  return a bright colour; hsl=(x,1.0,0.5)
      -f, --is_file     treat x as a file path to open locally
      --images_to_try IMAGES_TO_TRY
                        number of images to try processing before erroring



::

    $ whatcoloris sky
    #769ab8
    $ whatcoloris -f images/dog.png
    #6c5a47

It can also be called directly::

    $ python WhatColorIsX.py grass -b
    #65ff00

Errors
------

If the search does not find a suitable image to process, the
``WhatColorIsX.InvalidSearchResults`` exception will be raised. Examples that
cause this error include::

    from WhatColorIsX import whatcoloris
    
    no_search_string = whatcoloris('')
    no_images_returned = whatcoloris('foo', images_to_try=0)

Development
-----------

.. image:: https://readthedocs.org/projects/whatcolorisx/badge/?version=dev
    :target: http://whatcolorisx.readthedocs.org/en/stable/?badge=stable
    :alt: ReadTheDocs Documentation Status

.. image:: https://travis-ci.org/tommilligan/WhatColorIsX.svg?branch=dev
    :target: https://travis-ci.org/tommilligan/WhatColorIsX
    :alt: Travis CI build status

.. image:: https://coveralls.io/repos/tommilligan/WhatColorIsX/badge.svg?branch=dev&service=github
    :target: https://coveralls.io/github/tommilligan/WhatColorIsX?branch=dev
    :alt: Coveralls coverage status
    
WhatColorIsX can be installed for development as normal:

    * clone the GitHub repo
    * run ``python setup.py develop``
    * install dev dependencies using ``pip install -r requirements_dev.txt``.

Please ensure any new code you write:

    * is documented
        * has docstrings in the source code
        * is added to the ``docs`` (prefably using autodoc)
        * ``sphinx-build -b html . ./_build`` to check html output

    * is covered by tests
        * write tests and add them to ``tests``
        * run tests using ``nosetests`` or
          ``coverage run source=WhatColorIsX.py setup.py test``
        * check coverage using ``coverage report``

Pull Requests are always welcome!
    
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

    $ python xmlInterface.py input.xml output.xml bar name color

**output.xml**::

    <foo>
        <bar>
            <name>sun</name>
            <color>#873107</color>
        </bar>
    </foo>

