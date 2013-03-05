from contour import *
import wander
import random

def make_line(m,b):
    """Return a function that evaluates a line"""
    return lambda x: float(m) * float(x) + float(b)

'''
def make

def make_recursive_contours
'''

top = ContourSegment(6, make_line(0.0, 0.0), [])

#sects = ['a','a','b','b','c','a']
sects = ['a','b','a','c','a','b']
    
y = wander_from_contour(top,sects,-1.0,1.0,-1.0,1.0)
y = wander.make_segments(0.0,y)
x = []
for i in xrange(len(sects)):
    x.append(top.get_length()*float(i) / float(len(sects)))

points = zip(x,y)
#print points

bend_contour_segment(top, points)

i = 0.0
ival = 0.1
while i < top.get_length():
    print top.look_up(i)
    i += ival


