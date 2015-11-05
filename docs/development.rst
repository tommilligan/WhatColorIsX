Development
===========

Installation
------------

WhatColorIsX can be installed for development as normal:

    * clone the GitHub repo
    * run ``python setup.py develop``
    * install dev dependencies using ``pip install -r requirements_dev.txt``.

Guidelines
----------

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

Pull Requests on GitHub are always welcome!