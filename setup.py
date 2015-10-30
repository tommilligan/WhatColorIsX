from setuptools import setup

setup(name='WhatColorIsX',
      version='0.1.1',
      description='Get color of a string via Google iamge search API',
      long_description='Using the Google image search API, this allows a string to be converted into a (usually) related hex color value.',
      url='https://github.com/tommilligan/WhatColorIsX',
      author='Tom Milligan',
      author_email='code@tommilligan.net',
      license='GPL',
      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Natural Language :: English',
        'Programming Language :: Python'
      ],
      keywords='colour color google image text search',
      py_modules=['WhatColorIsX'],
      install_requires=[
          'colour',
          'simplejson',
          'Pillow'
      ],
      entry_points={
        'console_scripts': [
            'whatcoloris = WhatColorIsX:main'
        ]
      }
)