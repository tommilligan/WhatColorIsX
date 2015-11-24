from setuptools import setup
import os


version = '2.0.1'


# Call this to get README
def readme():
    with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as f:
        return f.read()


setup(name='WhatColorIsX',
      version=version,
      description='Get color of a string via Google image search API',
      long_description=readme(),
      url='https://github.com/tommilligan/WhatColorIsX',
      author='Tom Milligan',
      author_email='code@tommilligan.net',
      license='GPL',
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
      ],
      keywords='colour color google image text search find get string',
      py_modules=['WhatColorIsX'],
      install_requires=[
        'colour',
        'Pillow'
      ],
      entry_points={
        'console_scripts': [
            'whatcoloris = WhatColorIsX:main'
        ]
      },
      test_suite='nose.collector',
      tests_require=['nose']
)