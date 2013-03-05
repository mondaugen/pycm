'''
Tools that aid in computer music.
'''
import math
import random

def get_random_rhythm(lengths, length):
    '''Return a sequence of tuples of the format (time,length) where the sum of
    all the lengths of the tuples is less than the length argument. The rhythm
    also should not overlap, and shouldn't 'hang' off of the end.'''
    rhythm = []
    rechead = 0
    while(rechead < length):
	def fits(x): return x <= (length - rechead)
	poslens = filter(fits, lengths)
	if len(poslens) > 0:
	    #see if a length in lengths will fit
	    tmplen = random.choice(poslens)
	    rhythm.append((rechead,tmplen))
	    rechead += tmplen
	else:
	    #else just add the remaining bit
	    rhythm.append((rechead,(length - rechead)))
	    rechead += (length - rechead)
    return rhythm



