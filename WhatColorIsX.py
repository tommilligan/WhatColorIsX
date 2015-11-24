#!/usr/bin/env python3

import argparse
import json
import codecs
import urllib.parse
import urllib.request
import io
import math
import operator

from colour import Color
from PIL import Image


class InvalidSearchResults(Exception):
    """
    Raised if no valid image is returned by Google Search
    """
    pass


class whatcolorisx(object):
    """
    The whatcolorisx object. Can also be created by the
    :py:func:`~WhatColorIsX.new` factory function.

    :param string input: The search term to pass to Google image search.
                          If given with a .jpg or .png extension, it is treated
                          as a local file path. Will also accept a
                          `PIL.Image.Image` object.
    :param int images_to_try: The number of images to try processing before raising
                              :py:exc:`~WhatColorIsX.InvalidSearchResults`
    :returns: An :py:class:`~WhatColorIsX.whatcolorisx` object.
    :raises: :py:exc:`~WhatColorIsX.InvalidSearchResults` if no valid image is returned
             by the search
    """
    
    def __init__(self, input, images_to_try=10):
        self.input = input
        if isinstance(input, Image.Image):
            self.img = input
        elif input.lower().endswith(('.jpg', '.png')):
            self.img = Image.open(input)
        else:
            self.img = self._search_image(images_to_try=images_to_try)
    
    
    def _search_image(self, images_to_try=10):
        """
        Takes string, returns image using the `Google Custom API`_.
        
        .. _Google Custom API: https://developers.google.com/custom-search/docs/xml_results
        
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
        search_string_safe = urllib.parse.quote_plus(self.input)
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


    def average_color(self):
        """
        Returns the average colour of :py:attr:`whatcolorisx.img`.
        
        Recommended for most uses.
        
        :returns: RGB value in a three-member tuple
        :rtype: tuple
        """
        img = self.img.convert('RGB')
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

    
    def common_color(self):
        """
        Returns the most common colour of :py:attr:`whatcolorisx.img`.
        
        Not recommended for complex images which may be over or under-exposed; there
        is a high chance a black or white color will be returned.
        
        :returns: RGB value in a three-member tuple
        :rtype: tuple
        """
        img = self.img.convert('RGB')
        colors = sorted(img.getcolors(img.width*img.height), key=operator.itemgetter(0), reverse=True)
        return colors[0][1]


    def color(self, bright_hue=False, method='average_color'):
        """
        Returns the colour of :py:attr:`whatcolorisx.img`.
        
        If bright_hue is set to True, a bright hue will be returned.
        
        :param bool bright_hue: force a bright colour value
                                *(saturation = 1.0, luminance = 0.5)*
        :param string method: The helper method that will pick the colour from the image.
                       Options are :py:meth:`~whatcolorisx.average_color` or
                       :py:meth:`~whatcolorisx.common_color`
        :returns: the guessed colour of the input string in 6-digit hexadecimal format
                  *(e.g. #ffffff)*
        :rtype: string
        """
        method = getattr(self, method)
        picked = method()
        color = Color(rgb=[float(picked[x])/255.0 for x in range(3)])
        if bright_hue is True:
            color = Color(hue=color.hue, saturation=1.0, luminance=0.5)
        return color.hex_l



def new(input, images_to_try=10):
    """
    Factory function: creates a new whatcolorisx object from the given input.

    See :py:class:`WhatColorIsX.whatcolorisx` for parameters and more info.
    
    :returns: An :py:class:`~WhatColorIsX.whatcolorisx` object.
    """
    return whatcolorisx(input, images_to_try=images_to_try)


def main():
    parser = argparse.ArgumentParser(description='Returns colour of string based on Google image search.')
    parser.add_argument('x',
                        help='string/file to find colour of')
    parser.add_argument('-b', '--bright_hue', action='store_true',
                        help='return a bright colour; hsl=(x,1.0,0.5)')
    parser.add_argument('-m', '--method', choices=['average_color', 'common_color'],
                        help='Helper method to use for colour picking. Defaults to average')
    parser.add_argument('--images_to_try', type=int, default=10,
                        help='number of images to try processing before erroring')
    args = parser.parse_args()
    
    wcix = new(args.x, images_to_try=args.images_to_try)
    return wcix.color(bright_hue=args.bright_hue, method=args.method)


if __name__ == '__main__':
    sys.exit(main())