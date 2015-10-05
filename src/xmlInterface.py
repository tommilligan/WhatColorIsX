import WhatColorIsX
import xml.etree.ElementTree as ET
import os
from colour import Color

def update_xml(xml_path, element_tag, name_tag, color_tag):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    try:
        for element in root.findall(element_tag):
            ename = element.find(name_tag).text
            ehex = WhatColorIsX.what_color(ename) #Get color from google
            
            #Optional color alteration
            eColor = Color(ehex)
            altColor = Color(hue=eColor.hue, saturation=1.0, luminance=0.5)
            ehex = altColor.hex
            
            ecolor = element.find(color_tag)
            ecolor.text = ehex
            print ename, ehex
            #raise MemoryError #debug first col only
    finally:
        new_path = 'elements.xml'
        tree.write(new_path)
        return 'XML saved to '+new_path

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        print update_xml(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        print 'usage: xmlinterface.py xml_path element_tag name_tag color_tag'
        print 'updates the xml file at xml_path for element_tag with color_tag as determined by a Google image search for name_tag.'