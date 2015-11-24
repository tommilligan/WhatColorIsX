.. py:module:: WhatColorIsX
.. py:currentmodule:: WhatColorIsX

:py:mod:`~WhatColorIsX` Module
==============================

The :py:mod:`~WhatColorIsX` module provides functions for determining the colour of
a string or image.
    
Functions
---------

.. autofunction:: WhatColorIsX.whatcoloris

Exceptions
----------

.. autoexception:: WhatColorIsX.InvalidSearchResults

Helper functions
----------------

These were not written to be called directly, but you may find them useful
(e.g. if you want a ``PIL.Image.Image`` object as an input or output)

.. autofunction:: WhatColorIsX.whatcoloris_image
.. autofunction:: WhatColorIsX.search_image
.. autofunction:: WhatColorIsX.average_image_color
.. autofunction:: WhatColorIsX.common_image_color
