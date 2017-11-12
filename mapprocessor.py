import requests
import numpy

req = requests.get('https://data.montgomerycountymd.gov/resource/twfs-669f.json')
r = req.text
y = r.split("\n")

#print("\n".join(y)) #the right code
#del y[0::2]
#w, h = 8, 5;
#Matrix = [[0 for e in range(w)] for y in range(h)] # finished product type shit
#x=y[0].strip('[{",{":}').split("," and ":") these were unneeded bcuz n u m p y

print(y[0])
y = [x.strip('[{",{":}''@').split('":"' and '","' and '",":@') for x in y]

print("marker")
print(y[0])
print(y[10])

#y[0] is a list, but y is also a list. list in a list, not list in array
#how to convert to array?? numpy?? looking into it

print("marker")
y=(numpy.array(y))

## the array command that took WAY too long for me to find
# #also we spent 14 hours on this code lmao
#kill redundancies
#get to solving problems


#lol fuck encapsulation
def returnmiddleschools():
    return

def returnhighschools():
    return

def returnelementaryschools():
    return
def returnphonenumber():
    return

listofdata = [] #incredibly non specific
