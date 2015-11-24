import os

import WhatColorIsX
from PIL import Image
import re
from nose.tools import assert_raises


TEST_IMAGES_DIR = os.path.join('tests', 'img')


def test_known_images():
    """
    Test included images with pre-calculated colours.
    """
    known_images = {'red.jpg': '#fe0000',
                    'dirtycyan.png': '#69c6c5',
                    'ladybird.jpg': '#833911',
                    'tulip.png': '#e3800e'}
    for k, v in known_images.items():
        wcix = WhatColorIsX.new(os.path.join(TEST_IMAGES_DIR, k))
        assert wcix.color() == v


def test_known_images_bright():
    """
    Test included images with pre-calculated `bright_hue=True` colours.
    """
    known_images = {'red.jpg': '#ff0000',
                    'dirtycyan.png': '#00fffc',
                    'ladybird.jpg': '#ff5900',
                    'tulip.png': '#ff8900'}
    for k, v in known_images.items():
        wcix = WhatColorIsX.new(os.path.join(TEST_IMAGES_DIR, k))
        assert wcix.color(bright_hue=True) == v

def test_known_images_common():
    """
    Test included images with pre-calculated colours.
    """
    known_images = {'red.jpg': '#fe0000',
                    'dirtycyan.png': '#69c6c5',
                    'ladybird.jpg': '#961801',
                    'tulip.png': '#eedb13'}
    for k, v in known_images.items():
        wcix = WhatColorIsX.new(os.path.join(TEST_IMAGES_DIR, k))
        assert wcix.color(method='common_color') == v


def test_known_images_common_bright():
    """
    Test included images with pre-calculated colours.
    """
    known_images = {'red.jpg': '#ff0000',
                    'dirtycyan.png': '#00fffc',
                    'ladybird.jpg': '#ff2700',
                    'tulip.png': '#ffe900'}
    for k, v in known_images.items():
        wcix = WhatColorIsX.new(os.path.join(TEST_IMAGES_DIR, k))
        assert wcix.color(method='common_color', bright_hue=True) == v


def test_strings_invalid():
    """
    Test known invalid searches that should raise `WhatColorIsX.InvalidSearchResults`
    """
    known_invalid_search_errors = [('aslkdjfhskjghsdkjghalkjdsghskljahflksjdhfalksjhgasdfjaksjdgfajsdhgfjaksdghfkljsdhgkjfhalsjdhlaskjhadglkhasdfa', 10),
                                   ('', 10),
                                   ('sky', 0)]
    for s in known_invalid_search_errors:
        assert_raises(WhatColorIsX.InvalidSearchResults, WhatColorIsX.new, s[0], images_to_try=s[1])


def test_strings():
    """
    Test known valid searches that should produce a valid 6 digit hex output.
    """
    known_valid_seatches = [('sky', False),
                            ('grass', False),
                            ('sun', True),
                            ('earth', True)]
    hex_format = re.compile(r'^#[0-9a-f]{6}$')
    for s in known_valid_seatches:
        wcix = WhatColorIsX.new(s[0])
        assert hex_format.match(wcix.color(bright_hue=s[1]))


