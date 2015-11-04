import os


from WhatColorIsX import whatcoloris
from PIL import Image


TEST_IMAGES_DIR = os.path.join('tests', 'img')


def test_known_images():   
    known_images = {'red.jpg': '#fe0000',
                    'dirtycyan.png': '#69c6c5',
                    'ladybird.jpg': '#833911',
                    'tulip.png': '#e3800e'}
    for k, v in known_images.items():
        assert whatcoloris(os.path.join(TEST_IMAGES_DIR, k), is_file=True) == v


def test_known_images_bright():
    known_images = {'red.jpg': '#ff0000',
                    'dirtycyan.png': '#00fffc',
                    'ladybird.jpg': '#ff5900',
                    'tulip.png': '#ff8900'}
    for k, v in known_images.items():
        assert whatcoloris(os.path.join(TEST_IMAGES_DIR, k), bright_hue=True, is_file=True) == v


def test_input_strings():
    known_values = {'sky': '#779bb9',
                    'grass': '#3e850f',
                    'sun': '#873107',
                    'earth': '#363a4c'}
    for k, v in known_values.items():
        assert whatcoloris(k) == v


def test_input_strings_bright():
    known_values = {'sky': '#008aff',
                    'grass': '#65ff00',
                    'sun': '#ff5400',
                    'earth': '#0029ff'}
    for k, v in known_values.items():
        assert whatcoloris(k, bright_hue=True) == v

