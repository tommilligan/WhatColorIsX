from PIL import Image
import argparse
import simplejson
from colour import Color
try:
    # Python 2
    from urllib import quote_plus
    from urllib2 import urlopen
    from cStringIO import StringIO as BytesIO
except ImportError:
    # Python 3
    from urllib.parse import quote_plus
    from urllib.request import urlopen
    from io import BytesIO

def average_image_color(i): # Takes image, returns rgb - http://stackoverflow.com/questions/29726148/finding-average-color-using-python
	h = i.histogram()

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
    
def get_image(searchTerm): # Takes string, returns image - http://stackoverflow.com/questions/20716842/python-download-images-from-google-image-search
    startIndex = 0
    searchUrl = "http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=" + quote_plus(searchTerm) + "&start=" + str(startIndex)
    f = urlopen(searchUrl)
    deserialized_output = simplejson.load(f)
    # 4 image URLs returned - take first one that doesn't IOerror and is RGB(A) format
    for i in range(4):
        imageUrl = deserialized_output['responseData']['results'][i]['unescapedUrl']
        try:
            file = BytesIO(urlopen(imageUrl).read())
            img = Image.open(file)
        except IOError:
            continue
        if (img.mode == "RGB" or img.mode == "RGBA"):
            return img
    return False

def whatcoloris(searchTerm, bright_hue=False): # Takes string, returns hex
    img = get_image(searchTerm)
    avg = average_image_color(img)
    color = Color(rgb=[float(avg[x])/255.0 for x in range(3)])
    if bright_hue is True:
        color = Color(hue=color.hue, saturation=1.0, luminance=0.5)
    return color.hex

def main():
    parser = argparse.ArgumentParser(description='Returns colour of string based on Google image search.')
    parser.add_argument('x', help='string to find colour of')
    parser.add_argument('-b', '--bright_hue', action='store_true', help='return a bright colour; hsl=(x,1.0,0.5)')
    args = parser.parse_args()
    return whatcoloris(args.x, bright_hue=args.bright_hue)
    
if __name__ == '__main__':
    sys.exit(main())