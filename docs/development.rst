Development
===========

.. image:: https://readthedocs.org/projects/whatcolorisx/badge/?version=dev
    :target: http://whatcolorisx.readthedocs.org/en/stable/?badge=stable
    :alt: ReadTheDocs Documentation Status

.. image:: https://travis-ci.org/tommilligan/WhatColorIsX.svg?branch=dev
    :target: https://travis-ci.org/tommilligan/WhatColorIsX
    :alt: Travis CI build status

.. image:: https://coveralls.io/repos/tommilligan/WhatColorIsX/badge.svg?branch=dev&service=github
    :target: https://coveralls.io/github/tommilligan/WhatColorIsX?branch=dev
    :alt: Coveralls coverage status

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