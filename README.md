# WhatColorIsX
Python script which takes any string and returns a hex colour string, using Google image search.

## Installation
```
pip install WhatColorIsX
```
You may find you need to install Pillow as a dependency first.
```
pip install Pillow
```

## Usage
Input can be any string. Output is a valid hex colour value (3 or 6 digit).

WhatColorIsX returns an accurate colour value by default. If bright_hue is set to ```True```, it is guaranteed that a bright colour will be returned. If bright_hue is not set, it is likely that some whites, greys or blacks will be returned.

The [colour](https://github.com/vaab/colour) module can be used to easily perform further alterations.

#### Import to your project
```
from WhatColorIsX import what_color

brick_color = what_color('brick')
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

## Additional Scripts
#### XML Interface
```xmlInterface.py``` allows ```WhatColorIsX``` to interface with a correctly formatted XML file. This allows multiple values to be queued for processing. See the ```xml``` folder for the script, example input and output XML files, and the command format used to run it. Raise the ```-h``` flag for detailed information.
```
<foo>
    <bar>
        <name>sun</name>
    </bar>
</foo>
```
```
python xmlInterface.py input.xml output.xml bar name color
```
```
<foo>
    <bar>
        <name>sun</name>
        <color>#873107</color>
    </bar>
</foo>
```
