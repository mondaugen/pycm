'''
Given a function that returns fractional lengths and and another that returns
some kind of datum, sectionfiller is able to fill a list with (Fraction, datum)
tuples, usually representing some interesting musical parameter.
'''
from fractions import *

class SectionFiller:

    def __init__(self, sublengthfunc, datumfunc, length=Fraction(1)):
	'''
	sublengthfunc and datumfunc accept the parameter "aux" but needn't use
	it if they don't want
	'''
	self.sublengthfunc = sublengthfunc
	self.datumfunc = datumfunc
	self.length = length

    def get_list_of_data(self, aux=None):
	'''
	Because the section but have length equal to self.length at the end, the
	function will adjust the last item to have a length so that the total
	length equal self.length
	'''
	s = list()
	totlen = Fraction(0)
	while totlen < self.length:
	    sublen  = self.sublengthfunc(aux)
	    datum = self.datumfunc(aux)
	    s.append((sublen, datum))
	    totlen = totlen + sublen
	if (totlen > self.length) & (len(s) > 0):
	    sublen, datum = s[-1]
	    sublen = sublen - (totlen - self.length)
	    s.append((sublen, datum))
	return s


