import random
from formgenerator import *
from finddotproducts import *

def stretch_form_randomly(f,length):
    '''Given form f and a new length l, return a random dictionary of lengths so that
    when you look up each element of the form in the dictionary sequentially and
    sum the result, they sum to l'''
    fdict = count_formal_elements(f)
    if sum(fdict.values()) > length:
	raise Exception("Can't have a length: ", length, "less than the sum of the \
			    value frequencies", sum(fdict.values()))
    ftups = sorted(fdict.items()) # the keys are sorted, ie. [('a',3),('b',2) ...]
    sects = [x for x, y in ftups] # just the sections ie. ['a','b', ... ]
    freqs = [y for x, y in ftups] # just the frequencies, ie. [3,2, ... ]
    ldict = {} # the length of each section, just 1 for each section at first
    for t in sects:
	ldict[t] = 1
    Dp = DotProductsThatSum(freqs,length - sum(fdict.values()))
    r = Dp.get_rand_dot_product_for_sum() # some additions to be made to each
					  # formal element's length
    fadds = dict(zip(sects,r))
    for b in fadds:
	ldict[b] += fadds[b]
    return ldict

def give_form_lengths(f,minlen,maxlen):
    ''' Give each formal element in f a length between min and max ( min <= l <
    max). Return a dictionary so that the element may look up its length'''
    ldict = {}
    for el in set(f):
	ldict[el] = random.randrange(minlen,maxlen)
    return ldict

def get_formal_length_tuples(form, ldict, scalar=1):
    '''Accepts a form (ie. [a,b,b,a]) and an dictionary of lengths ldict
    (ie, {a:2, b:3}), and an optional scalar (default 1) and returns a list of
    tuples of the form (<formal name>, <length as looked up in ldict * scalar>).
    So for the above example and a scalar of 2, the result would be:
    [('a',4),('b',6),('a',6),('b',4)] '''
    r = []
    for f in form:
	r.append((f,ldict[f]*scalar));
    return r

