from contour import *
import random
random.seed()
import sys
def make_line(m,b):
    """Return a function that evaluates a line"""
    return lambda x: float(m) * float(x) + float(b)

'''We make a contour segment with contours as follows:
    top: y = 3/4x + 0
    sub: y1 = 2x + 0 , y2 = 0.5x + 0'''
def make_test_segments():
    top = ContourSegment(4, make_line(3.0/4.0, 0.0), [])
    top.subcontours.append(ContourSegment(2, make_line(2.0, 0.0), []))
    top.subcontours.append(ContourSegment(1, make_line(0.5, 0.0), []))
    return top

top = make_test_segments()

#print 'Looking up 1.0: ' + repr(top.look_up(1.0))
#print 'Looking up 2.0: ' + repr(top.look_up(2.0))
#print 'Looking up 2.1: ' + repr(top.look_up(2.1))

if len(sys.argv) != 2:
    raise Exception('''First argument is script name, second is sampling interval''')
samplingival = float(sys.argv[1])

i = 0.0
tlen = top.get_length()
while i < tlen:
    print repr(top.look_up(i))
    i += samplingival


