.. _examples:

Examples
========

Import to your project
----------------------

For almost all cases, call the :py:func:`~WhatColorIsX.new` factory function,
then get the colour value from the :py:meth:`~WhatColorIsX.whatcolorisx.color` method:

.. code-block:: python

    import WhatColorIsX
    
    brick = WhatColorIsX.new('brick')
    brick_color = brick.color()
    fish = WhatColorIsX.new('fish')
    fish_color_bright = fish.color(bright_hue=True)
    
If you already have PIL images that you want to process, you can use the same syntax:

.. code-block:: python

    from WhatColorIsX import whatcoloris_image
    from PIL import Image
    
    img = Image.open('images/cat.jpg')
    cat = WhatColorIsX.new(img)
    cat_color = cat.color()

Run from the command line
-------------------------

Use the :ref:`whatcoloris_command`::

    $ whatcoloris sky
    #769ab8
    $ whatcoloris images/dog.png
    #6c5a47
    $ whatcoloris grass -b
    #65ff00

Visual Demo
-----------

Using `this python script`_, a folder of image files can be composited along
with their calculated colours. The main function of WhatColorIsX is to do this
*without* a source image, using only a string.

.. _this python script: https://gist.github.com/tommilligan/951a63b55be7dc9b8c02

See an example output `here`_.

.. _here: http://tommilligan.github.io/#WhatColorIsX
