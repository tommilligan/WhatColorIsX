.. py:module:: WhatColorIsX
.. py:currentmodule:: WhatColorIsX

:py:mod:`~WhatColorIsX` Module
==============================

The :py:mod:`~WhatColorIsX` module provides an object of the same name (lowercase), which can
determining the colour of:

    * A string
    * A local file
    * A ``PIL.Image.Image``
    
The :py:class:`~WhatColorIsX.whatcolorisx` Class
------------------------------------------------

.. autoclass:: WhatColorIsX.whatcolorisx

Methods
^^^^^^^

.. automethod:: whatcolorisx.color

Helper methods
""""""""""""""

.. automethod:: whatcolorisx.average_color
.. automethod:: whatcolorisx.common_color

Attributes
^^^^^^^^^^

.. py:attribute:: whatcolorisx.input

    The initial input to the :py:class:`~WhatColorIsX.whatcolorisx` object.

.. py:attribute:: whatcolorisx.img

    The ``PIL.Image.Image`` image generated from :py:attr:`~WhatColorIsX.whatcolorisx.input`.

Exceptions
----------

.. autoexception:: WhatColorIsX.InvalidSearchResults

