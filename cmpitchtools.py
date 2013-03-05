'''
Tools for manipulating pitches.
'''
import cmmath

def map_pcs_to_range(pcs, lowerbound, upperbound):
    '''Takes a set of pitches as pitchclasses and returns a list of all the
    occurrences of the pitches within the range. Ie pcs = [1,7], lowerbound =
    55, upperbound = 70 gives: 55, 61, 67'''
    pchs = []
    for pc in pcs:
	#subtract lowerbound from pc and find pc
	pc = (pc - lowerbound)%12
	#then add lowerbound to pc
	pc = pc + lowerbound
	while(pc <= upperbound): #range is inclusive
	    pchs.append(pc)
	    pc = pc + 12
    return sorted(pchs)

def get_nearest_pitch(pchs, pch):
    '''Finds the nearest pitch to pch in pchs'''
    return cmmath.find_nearest(pchs, pch)
