#!/usr/bin/env/python

import argparse
import json
import codecs
import urllib.parse
import urllib.request
import io

from colour import Color
from PIL import Image


def average_image_color(img):
    """
    Takes image, returns average colour [`StackOverflow`_].
    
    .. _StackOverflow: http://stackoverflow.com/questions/29726148/finding-average-color-using-python
    
	:param i: A `PIL.Image.Image` object
    :returns: RGB value in a three-member tuple
    :rtype: tuple
    """
    img = img.convert('RGB')
    h = img.histogram()
    # split into red, green, blue
    r = h[0:256]
    g = h[256:256*2]
    b = h[256*2: 256*3]
    # perform the weighted average of each channel:
    # the *index* is the channel value, and the *value* is its weight
    return (
        sum( i*w for i, w in enumerate(r) ) / sum(r),
        sum( i*w for i, w in enumerate(g) ) / sum(g),
        sum( i*w for i, w in enumerate(b) ) / sum(b)
    )


def get_image(searchTerm):
    """
    Takes string, returns image [`StackOverflow`_].
    
    .. _StackOverflow: http://stackoverflow.com/questions/20716842/python-download-images-from-google-image-search
    
	:param searchTerm: The string to find image of
    :returns: A `PIL.Image.Image` object
    :rtype: `PIL.Image.Image`
    """
    startIndex = 0
    searchUrl = "http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=" + urllib.parse.quote_plus(searchTerm) + "&start=" + str(startIndex)
    f = urllib.request.urlopen(searchUrl)   
    reader = codecs.getreader("utf-8")
    deserialized_output = json.load(reader(f))
    # 4 image URLs returned - take first one that doesn't IOerror and is RGB(A) format
    for i in range(4):
        imageUrl = deserialized_output['responseData']['results'][i]['unescapedUrl']
        try:
            file = io.BytesIO(urllib.request.urlopen(imageUrl).read())
            img = Image.open(file)
        except IOError:
            continue
        if (img.mode == "RGB" or img.mode == "RGBA"):
            return img
    return False


def whatcoloris_image(img, bright_hue=False):
    """
    Takes a `PIL.Image.Image` object and returns it's average colour.
    
    If bright_hue is set to True, a bright hue will be returned.
    
    :param searchTerm: A `PIL.Image.Image` object to get colour of
    :param bool bright_hue: force a bright colour value (hsl = [0.0-1.0], 1.0, 0.5)
    :returns: the guessed colour of the input string in 6-digit hexadecimal format (#[0-9a-f]{6})
    :rtype: string
    """
    avg = average_image_color(img)
    color = Color(rgb=[float(avg[x])/255.0 for x in range(3)])
    if bright_hue is True:
        color = Color(hue=color.hue, saturation=1.0, luminance=0.5)
    return color.hex_l

    
def whatcoloris(search_string, bright_hue=False, is_file=False):
    """
    Takes a string and guesses it's colour using Google image search.
    
    If bright_hue is set to True, a bright hue will be returned.
    
    :param string search_string: string to get colour of
    :param bool bright_hue: force a bright colour value (hsl = [0.0-1.0], 1.0, 0.5)
    :param bool is_file: treat search_string as a file path to open locally
    :returns: the guessed colour of the input string in 6-digit hexadecimal format (#[0-9a-f]{6})
    :rtype: string
    """
    if is_file:
        print(search_string)
        img = Image.open(search_string)
    else:
        img = get_image(search_string)
    return whatcoloris_image(img, bright_hue=bright_hue)


def main():
    parser = argparse.ArgumentParser(description='Returns colour of string based on Google image search.')
    parser.add_argument('x', help='string to find colour of')
    parser.add_argument('-b', '--bright_hue', action='store_true', help='return a bright colour; hsl=(x,1.0,0.5)')
    parser.add_argument('-f', '--is_file', action='store_true', help='treat x as a file path to open locally')
    args = parser.parse_args()
    return whatcoloris(args.x, bright_hue=args.bright_hue, is_file=args.is_file)

  
if __name__ == '__main__':
    sys.exit(main())