import cmmath
from fractions import *


class Quantizer:
    '''
    Intended for use as a Mix-In or superclass. Works by storing the original
    keys of a sequence and replacing the referenced sequence's keys with quantized
    keys. If the original sequence keys are desired, pass 0 as the divisor
    argument to quantize.
    '''

    def __init__(self, seqdict=None):
	self.originalkeys = sorted(seqdict.keys())
	self.seqref = seqdict

    def quantize(self, divisor=0, offset=0):
	'''
	Quantizes the keys to divisor with offset. See cmmath.cm_round for how
	this works. It basically applies cm_round to all the keys. If you would
	like to go back to the original, unquantized rhythm, pass 0 for divisor.
	Passing 0 for divisor will ignore whatever is in offset.
	'''
	if self.seqref == None:
	    raise Exception('self.seqref is None')
	tmpdict = dict()
	for origk, oldk in zip(self.originalkeys, sorted(self.seqref.keys())):
	    tmpdict[origk] = self.seqref.pop(oldk)
	if divisor == 0:
	    for k in tmpdict.keys():
		self.seqref[k] = tmpdict[k]
	else:
	    for k in tmpdict.keys():
		self.seqref[cmmath.cm_round(k,divisor,offset)] = tmpdict[k]
	

