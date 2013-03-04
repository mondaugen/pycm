# Contour Segments
import random
import wander

class ContourLookupError(Exception):
    def __init__(self, value):
	self.value = value
    def __str__(self):
	return "Lookup error with value: " + repr(self.value)

class ContourSegment:
    """Holds a length and a function and possibly a sublist of ContourSegments.
    The function is evaluated from [0,length), as a piecewise function."""
    length = 0
    function = None
    subcontours = []

    def __init__(self, length, function, subcontours):
	self.length = length
	self.function = function
	self.subcontours = subcontours

    def get_length(self):
	return self.length

    def get_delta(self):
	if self.function == None:
	    raise AttributeError('No function.')
	return self.function(self.length)

    def look_up(self, x):
	if (x < 0) | (x > self.get_length()):
	    raise ContourLookupError(x)
	s = None
	i = iter(self.subcontours)
	accumx = 0.0
	accumy = 0.0
	while True :
	    try:
		s = i.next()
	    except StopIteration:
		s = None
		break
	    if (accumx + s.get_length()) > x:
		return accumy + s.look_up(x - accumx)
	    accumx += s.get_length()
	    accumy += s.get_delta()
	return self.function(x)

def make_constrainer(mi, ma, idx):
    return lambda x: (x[idx] >= mi) and (x[idx] < ma)

def make_line(m,b):
    """Return a function that evaluates a line"""
    return lambda x: float(m) * float(x) + float(b)

def bend_contour_segment(c, points):
    '''Takes a set of points (x,y) s.t. x is in [0,c.get_length()). Those
    not in the domain will be discarded. Completes line segments so that a
    trajectory is drawn from 0 to c.get_delta().'''
    f = make_constrainer(0, c.get_length(), 0)
    points = filter(f, points)
    accumx = 0.0
    accumy = 0.0
    for p in sorted(points):
	xdiff = p[0] - accumx
	if xdiff != 0.0:
	    c.subcontours.append(ContourSegment(p[0] - accumx,\
		make_line((p[1] - accumy)/xdiff, 0.0), []))
	accumx = p[0]
	accumy = p[1]
    xdiff = c.get_length() - accumx
    if xdiff != 0.0:
	c.subcontours.append(ContourSegment(c.get_length() - accumx,\
		make_line((c.get_delta() - accumy)/xdiff, 0.0), []))
    return

def wander_from_contour(cs, sects, kmi, kma, lbnd, ubnd):
    '''Take  a contour segment and calculate some trajectory it could take using
    a form set. The result is a list of deltas'''
    a = wander.wander(0.0, cs.get_delta(), kmi, kma, lbnd, ubnd, len(set(sects))+1)
    deltas = wander.get_deltas(a)
    random.shuffle(deltas) # maybe not needed
    return wander.map_sections_to_deltas(deltas,sects)


