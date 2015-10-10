import WhatColorIsX
import xml.etree.ElementTree as ET
import argparse

def update_xml(xml_path, save_path, element_tag, name_tag, color_tag, bright_hue=False):
    tree = ET.parse(xml_path)
    root = tree.getroot()
    try:
        for element in root.findall(element_tag):
            ename = element.find(name_tag).text
            ehex = WhatColorIsX.what_color(ename, bright_hue=bright_hue) #Get color from google
            ecolor = ET.SubElement(element, color_tag)
            
            ecolor.text = ehex
            print ename, ehex
    finally:
        new_path = 'output.xml'
        tree.write(save_path)
        return 'XML saved to '+save_path

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Look up multiple string colors using xml')
    parser.add_argument('xml_path', help='input xml file')
    parser.add_argument('save_path', help='output xml file')
    parser.add_argument('parent_element', help='the element under which color will be saved')
    parser.add_argument('name_element', help='the value in each name_element will be Google searched')
    parser.add_argument('color_element', help='the element under which color will be saved')
    parser.add_argument('-b', '--bright_hue', action='store_true', help='return a bright colour; hsl=(x,1.0,0.5)')
    args = parser.parse_args()
    print update_xml(args.xml_path, args.save_path, args.parent_element, args.name_element, args.color_element, bright_hue=args.bright_hue)    
    