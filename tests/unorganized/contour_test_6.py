from contour import *
import wander
import random

def make_line(m,b):
    """Return a function that evaluates a line"""
    return lambda x: float(m) * float(x) + float(b)

top = ContourSegment(4, make_line(3.0/4.0, 0.0), [])

sects = ['a','a','b','b','c','a']

for i in xrange(3):
    print wander_from_contour(top,sects,-4.0,4.0,-10,10)


