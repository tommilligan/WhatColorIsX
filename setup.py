from setuptools import setup

setup(name='WhatColorIsX',
      version='0.1.0',
      description='Get color of a string via Google iamge search API',
      long_description='Using the Google image search API, this allows a string to be converted into a (usually) related hex color value.',
      url='https://github.com/tommilligan/WhatColorIsX',
      author='Tom Milligan',
      author_email='tom.milligan477@gmail.com',
      license='GPL',
      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7'
      ],
      keywords='colour color google image text search',
      packages=['.'],
      install_requires=[
          'colour',
          'simplejson',
          'pillow'
      ]
)