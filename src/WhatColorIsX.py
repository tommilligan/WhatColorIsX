from PIL import Image
import urllib
import urllib2
import simplejson
import cStringIO

def rgb2hex(rgb):
    def clamp(x): 
        return max(0, min(x, 255))
    hex = "#{0:02x}{1:02x}{2:02x}".format(clamp(rgb[0]), clamp(rgb[1]), clamp(rgb[2]))
    return hex

def average_image_color(i): # Takes image, returns rgb
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

def get_image(searchTerm): # Takes string, returns image
    fetcher = urllib2.build_opener()
    startIndex = 0
    searchUrl = "http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=" + searchTerm + "&start=" + str(startIndex)
    f = fetcher.open(searchUrl)
    deserialized_output = simplejson.load(f)
    imageUrl = deserialized_output['responseData']['results'][0]['unescapedUrl']
    file = cStringIO.StringIO(urllib.urlopen(imageUrl).read())
    img = Image.open(file)
    return img

def what_color(searchTerm): # Takes string, returns hex
    img = get_image(searchTerm)
    avg = average_image_color(img)
    hex = rgb2hex(avg)
    print(img, avg, hex)
    return hex

    
if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        print what_color(sys.argv[1])
    else:
        print 'usage: WhatColorIsX.py STRING'
        print 'prints the average color of STRING as hex value as determined by a Google image search.'