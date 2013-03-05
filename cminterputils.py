# Copyright 2013 Nicholas Esterer

def linterp(x1, y1, x2, y2, x):
    '''
    Make a line that fits the points (x1,y1), (x2,y2) and evaluate the point x on
    this line.
    '''
    if x2 == x1:
	#raise ArithmeticError('Denominator: %f - %f equals zero.' % (x2,x1))
	# Return y1, it's more fun
	return y1
    return ((y2 - y1)/(x2 - x1)) * (x - x1) + y1;

def linterp_norm(y1, y2, x):
    '''
    Sometimes you just wanna simply linearly interpolate between two values using
    0-1 as the domain.
    '''
    return linterp(0, y1, 1, y2, x)
