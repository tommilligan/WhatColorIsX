import os

from WhatColorIsX import whatcoloris, InvalidSearchResults
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
        assert whatcoloris(os.path.join(TEST_IMAGES_DIR, k), is_file=True) == v


def test_known_images_bright():
    """
    Test included images with pre-calculated `bright_hue=True` colours.
    """
    known_images = {'red.jpg': '#ff0000',
                    'dirtycyan.png': '#00fffc',
                    'ladybird.jpg': '#ff5900',
                    'tulip.png': '#ff8900'}
    for k, v in known_images.items():
        assert whatcoloris(os.path.join(TEST_IMAGES_DIR, k), bright_hue=True, is_file=True) == v


def test_input_strings_invalid():
    """
    Test known invalid searches that should raise `WhatColorIsX.InvalidSearchResults`
    """
    assert_raises(InvalidSearchResults, whatcoloris, 'aslkdjfhskjghsdkjghalkjdsghskljahflksjdhfalksjhgasdfjaksjdgfajsdhgfjaksdghfkljsdhgkjfhalsjdhlaskjhadglkhasdfa')
    assert_raises(InvalidSearchResults, whatcoloris, '')
    assert_raises(InvalidSearchResults, whatcoloris, 'sky', images_to_try=0)


def test_input_strings():
    """
    Test known valid searches that should produce a valid 6 digit hex output.
    """
    hex_format = re.compile(r'^#[0-9a-f]{6}$')
    assert hex_format.match(whatcoloris('sky'))
    assert hex_format.match(whatcoloris('grass'))
    assert hex_format.match(whatcoloris('sun', bright_hue=True))
    assert hex_format.match(whatcoloris('earth', bright_hue=True))


