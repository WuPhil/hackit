import gmplot
from mapprocessor import returnelementaryschools, returnhighschools, returnmiddleschools

name = "placeholder"
moco = gmplot.GoogleMapPlotter(37.428, -122.145, 16)

print("succ")

moco.draw('htmlfiles/' + name + '.html')


