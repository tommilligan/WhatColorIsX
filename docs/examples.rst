.. _examples:

Examples
========

Import to your project
----------------------

For almost all cases, call the :py:func:`~WhatColorIsX.whatcoloris` function:

.. code-block:: python

    from WhatColorIsX import whatcoloris
    
    brick_color = whatcoloris('brick')
    fish_color_bright = whatcoloris('fish', bright_hue=True)
    my_cat_colour = whatcoloris('my images/cat.jpg', is_file=True)
    pineapple_colour = whatcoloris('pineapple', images_to_try=100)
    
If you already have PIL images that you want to process, you can call
:py:func:`~WhatColorIsX.whatcoloris_image`:

.. code-block:: python

    from WhatColorIsX import whatcoloris_image
    from PIL import Image
    
    img = Image.open('my images/squirrel.jpg')
    squirrel_colour_bright = whatcoloris_image(img, bright_color=True)


Run from the command line
-------------------------

Use the :ref:`whatcoloris_command`::

    $ whatcoloris sky
    #769ab8
    $ whatcoloris -f images/dog.png
    #6c5a47

It can also be called directly::

    $ python WhatColorIsX.py grass -b
    #65ff00