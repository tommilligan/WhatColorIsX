# WhatColorIsX
Python script which takes any string and returns a hex colour string, using Google image search.

## Installation
```pip install WhatColorIsX```

## Usage

#### Import to your project
```
from WhatColorIsX import what_color

sun_color = what_color('sun')
fish_color_bright = what_color('fish', bright_hue=True)
```
#### Run from the command line
```
python WhatColorIsX.py sky
>>> #769ab8
```
```
python WhatColorIsX.py grass -b
>>> #6f0
```

## XML Interface
```xmlInterface.py``` allows ```WhatColorIsX.py``` to interface with a correctly formatted XML file. This allows multiple values to be queued for processing. See the ```example``` folder for example input and output XML files.