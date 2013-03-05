import random
import itertools

def find_all_dot_products_for_sum(a,b,l):
	'''Given a, b, find all m and n >= 0 such that am + bn = l'''
	r = []
	for n in xrange(int(l/b)+1):
	    if ((l - b*n) % a) == 0:
		r.append(((l - b*n)/a, n))
	return r

def pick_set_in_ranges(ranges):
    '''Given a set {a0,...,ak], pick a set [n0,...,nk] s.t. 0 <= ni < ai for all
    i in [0,k]'''
    r = []
    for i in ranges:
	r.append(random.randrange(i))
    return r

def make_set_within_ranges(ranges):
    '''Given a list {r0,...,rn}, list all tuples {n0,..,nk} s.t. 0 <= ni < ri
    for all i in [0,k]'''
    expanded_ranges = []
    for i in ranges:
	expanded_ranges.append(range(i))
    return list(itertools.product(*expanded_ranges))

def dot_product(a,b):
    if len(a) != len(b):
	raise Exception('Cannot find the dot product of two differently sized\
			    vectors')
    return sum([p*q for p, q in zip(a,b)])

def find_rand_dot_product_for_sum(a,l):
    '''Finds some vector v with all elements positive s.t. v*a = l'''
    if min(a) > l:
	return tuple([0 for i in xrange(len(a))])
    ranges = []
    for k in a:
	ranges.append(l/k)
    while True:
	r = pick_set_in_ranges(ranges)
	if dot_product(a,r) == l:
	    return tuple(r)

class DotProductsThatSum:
    '''An object that will give you a dot product that will give the sum when
    operating on the vector stored within it'''
    vect = []
    l = None # l is sum
    expanded_ranges = []

    def __init__(self, vect, l):
	self.vect = vect
	self.sum = l 
	ranges = []
	for v in vect:
	    ranges.append(l/v)
	self.expanded_ranges = make_set_within_ranges(ranges)
	random.shuffle(self.expanded_ranges)

    def get_rand_dot_product_for_sum(self):
	while True:
	    if min(self.vect) > l:
		return tuple([0 for i in xrange(len(a))])
	    try:
		r = self.expanded_ranges.pop()
	    except IndexError:
		return tuple([0 for i in xrange(len(a))])
	    if dot_product(self.vect,r) == l:
		return tuple(r)

#r = find_all_dot_products_for_sum(2,3,1000)

#for i in xrange(10):
#    print repr(pick_set_in_ranges([4,4,2,3]))

a = [4,3,1]
l = 8
stuff = []
Dp = DotProductsThatSum(a,l)
for i in xrange(3):
    stuff.append(Dp.get_rand_dot_product_for_sum())
print repr(stuff)
print repr(dot_product(random.choice(stuff),a))
