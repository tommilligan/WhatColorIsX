#!/usr/bin/env python3

import argparse
import json
import codecs
import urllib.parse
import urllib.request
import io
import math

from colour import Color
from PIL import Image


class InvalidSearchResults(Exception):
    """
    Raised if no valid image is returned by Google Search
    """
    pass

def average_image_color(img):
    """
    Takes image, returns average colour.
    
    :param i: A ``PIL.Image.Image`` object
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


def search_image(search_string, images_to_try=10):
    """
    Takes string, returns image using the `Google Custom API`_.
    
    .. _Google Custom API: https://developers.google.com/custom-search/docs/xml_results
    
    :param string search_string: The string to find image of
    :param int images_to_try: The number of images to try processing before raising
                          :py:exc:`~WhatColorIsX.InvalidSearchResults`
    :returns: An image corresponding to string_search
    :rtype: ``PIL.Image.Image``
    :raises: :py:exc:`~WhatColorIsX.InvalidSearchResults` if no valid image is returned
             by the search
    """
    start_index = 0
    results_per_search = 4 # Max 20
    search_attempts = int(math.ceil(images_to_try/results_per_search))
    search_string_safe = urllib.parse.quote_plus(search_string)
    for attempt in range(search_attempts):
        images_already_searched = attempt*results_per_search
        searchUrl = "http://ajax.googleapis.com/ajax/services/search/images?v=1.0&start={0}&num={1}&q={2}".format(
                    str(start_index+images_already_searched),
                    str(results_per_search+images_already_searched),
                    search_string_safe)
        f = urllib.request.urlopen(searchUrl)   
        reader = codecs.getreader("utf-8")
        deserialized_output = json.load(reader(f))
        # take first URL that doesn't IOerror and is RGB(A) format
        try:
            for i in range(results_per_search):
                imageUrl = deserialized_output['responseData']['results'][i]['unescapedUrl']
                try:
                    file = io.BytesIO(urllib.request.urlopen(imageUrl).read())
                    img = Image.open(file)
                except IOError:
                    continue
                if (img.mode == "RGB" or img.mode == "RGBA"):
                    return img
        except IndexError:
            raise InvalidSearchResults('No valid image could be found')
    raise InvalidSearchResults('No valid image could be found')

def whatcoloris_image(img, bright_hue=False):
    """
    Takes a ``PIL.Image.Image`` object and returns it's average colour.
    
    If bright_hue is set to True, a bright hue will be returned.
    
    :param img: A ``PIL.Image.Image`` object to get colour of
    :param bool bright_hue: force a bright colour value
                            *(saturation = 1.0, luminance = 0.5)*
    :returns: the guessed colour of the input string in 6-digit hexadecimal format
              *(e.g. #ffffff)*
    :rtype: string
    """
    avg = average_image_color(img)
    color = Color(rgb=[float(avg[x])/255.0 for x in range(3)])
    if bright_hue is True:
        color = Color(hue=color.hue, saturation=1.0, luminance=0.5)
    return color.hex_l

    
def whatcoloris(search_string, bright_hue=False, is_file=False, images_to_try=10):
    """
    Takes a string and returns it's colour using Google image search.
    
    If bright_hue is set to True, a bright hue will be returned.
    
    A specific file can be processed by providing the file path as search_string
    and setting is_file to True.
    
    This function can be accessed from the command line by calling the
    :ref:`whatcoloris_command`.
    
    :param string search_string: string to get colour of
    :param bool bright_hue: force a bright colour value
                            *(saturation = 1.0, luminance = 0.5)*
    :param int images_to_try: The number of images to try processing before raising
                              :py:exc:`~WhatColorIsX.InvalidSearchResults`.
                              No effect if ``is_file=True``
    :param bool is_file: treat search_string as a file path to open locally
    :returns: the guessed colour of the input string in 6-digit hexadecimal format
              *(e.g. #ffffff)*
    :rtype: string
    :raises: :py:exc:`~WhatColorIsX.InvalidSearchResults` if no valid image
             is returned by Google Search
    """
    if is_file:
        print(search_string)
        img = Image.open(search_string)
    else:
        img = search_image(search_string, images_to_try=images_to_try)
    return whatcoloris_image(img, bright_hue=bright_hue)


def main():
    parser = argparse.ArgumentParser(description='Returns colour of string based on Google image search.')
    parser.add_argument('x',
                        help='string to find colour of')
    parser.add_argument('-b', '--bright_hue', action='store_true',
                        help='return a bright colour; hsl=(x,1.0,0.5)')
    parser.add_argument('-f', '--is_file', action='store_true',
                        help='treat x as a file path to open locally')
    parser.add_argument('--images_to_try', type=int, default=10,
                        help='number of images to try processing before erroring')
    args = parser.parse_args()
    return whatcoloris(args.x, bright_hue=args.bright_hue,
                       is_file=args.is_file, images_to_try=args.images_to_try)

  
if __name__ == '__main__':
    sys.exit(main())