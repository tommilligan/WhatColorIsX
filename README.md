# WhatColorIsX
Python script which takes any string and returns a hex colour string, using Google image search.

## Installation
```
pip install WhatColorIsX
```
You may find you need to ```pip install Pillow``` as a dependency first, although it will be attempted automatically.

## Usage
Input can be any string. Output is a valid hex colour value (3 or 6 digit).

WhatColorIsX returns an accurate colour value by default. If bright_hue is set to ```True```, it is guaranteed that a bright colour will be returned. If bright_hue is not set, it is likely that some whites, greys or blacks will be returned.

The [colour](https://github.com/vaab/colour) module can be used to easily perform further alterations.

#### Import to your project
```
from WhatColorIsX import whatcoloris

brick_color = whatcoloris('brick')
fish_color_bright = whatcoloris('fish', bright_hue=True)
```
#### Run from the command line
When installed, the script can be accessed with the ```whatcoloris``` command
```
whatcoloris sky
>>> #769ab8
```
It can also be called directly
```
python WhatColorIsX.py grass -b
>>> #6f0
```

## Additional Scripts
These scripts will not be installed by pip, but can be downloaded directly from the GitHub repo if desired

#### XML Interface
```xmlInterface.py``` allows ```WhatColorIsX``` to interface with a correctly formatted XML file. This allows multiple values to be queued for processing. See the ```xml``` folder for the script, example input and output XML files, and the command format used to run it. Raise the ```-h``` flag for detailed information.

**input.xml**
```
<foo>
    <bar>
        <name>sun</name>
    </bar>
</foo>
```
**command**
```
python xmlInterface.py input.xml output.xml bar name color
```
**output.xml**
```
<foo>
    <bar>
        <name>sun</name>
        <color>#873107</color>
    </bar>
</foo>
```
