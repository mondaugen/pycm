from contour import *
top = ContourSegment(1.0, make_line(0.0, 0.0), [])
points = [[-0.2,-0.7],[0.3,0.25],[0.9,-0.4],[1.1,0.8]]
bend_contour_segment(top, points)
i = 0.0
while i < top.get_length():
    print repr(top.look_up(i))
    i += 0.01
