from contour import *
from random import *
import sys
seed()
def make_line(m,b):
    """Return a function that evaluates a line"""
    return lambda x: float(m) * float(x) + float(b)

def make_segments(numsegs, totlen, maxsublen, yrange):
    top = ContourSegment(totlen, make_line(0.1, 0.0), [])
    subs = []
    for i in xrange(numsegs):
	subs.append(ContourSegment(uniform(0.0,maxsublen/2.0),\
	    make_line(uniform(yrange*(-1.0),yrange),0.0),[]))
    s = None
    accumx = 0.0
    while accumx < top.get_length():
	s = choice(subs)
	top.subcontours.append(s)
	accumx += s.get_length()
    return top

def make_segments_recursive(numsegs, totlen, maxsublen, yrange, depth):
    top = ContourSegment(totlen, make_line(uniform(yrange*(-1.0),yrange), 0.0), [])
    subs = []
    for i in xrange(numsegs):
	if depth == 0:
	    subs.append(ContourSegment(uniform(0.0,maxsublen/2.0),\
		    make_line(uniform(yrange*(-1.0),yrange),0.0),[]))
	else:
	    subs.append(make_segments_recursive(numsegs,\
		totlen/numsegs,uniform(0.0, totlen/numsegs/2.0),\
		uniform(0.0,yrange),depth-1))
    s = None
    accumx = 0.0
    while accumx < top.get_length():
	s = choice(subs)
	top.subcontours.append(s)
	accumx += s.get_length()
    return top

def make_test_segments(numsegs):
    top = ContourSegment(10, make_line(0.0, 0.0), [])
    subs = []
    for i in xrange(numsegs):
	totlen = choice([1,2])
	subs.append(make_segments(randrange(1,5),totlen,\
	    uniform(0.0,totlen), uniform(0.0,4.0)))
    s = None
    accumx = 0.0
    while accumx < top.get_length():
	s = choice(subs)
	top.subcontours.append(s)
	accumx += s.get_length()
    return top


#print 'Looking up 1.0: ' + repr(top.look_up(1.0))
#print 'Looking up 2.0: ' + repr(top.look_up(2.0))
#print 'Looking up 2.1: ' + repr(top.look_up(2.1))

if len(sys.argv) != 5:
    raise Exception('''First argument is script name, second is sampling
	    interval, third is number of segments, fourth is depth, fifth is
	    length''')
samplingival = float(sys.argv[1])
numsegs = int(sys.argv[2])
depth = int(sys.argv[3])
length = float(sys.argv[4]);
top = make_segments_recursive(numsegs, length, length/3.0, 2.0, depth)

i = 0.0
tlen = top.get_length()
#print '''Length is: '''+repr(tlen)
while i < tlen:
    print repr(top.look_up(i))
    i += samplingival


