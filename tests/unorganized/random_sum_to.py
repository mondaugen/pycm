#this doesn't work properly, the lo and hi do not constrain the values..

from random import *
def random_sum_to(sm, nterms, lo, hi):
    if nterms < 2:
	return [sm]
    rand = uniform(lo, hi)
    print "sum " + repr(sm) + " nterms " + repr(nterms) + " lo " \
	    + repr(lo) + " hi " + repr(hi)
    sterms = randrange(1,nterms)
    return random_sum_to(rand, sterms, lo, hi) +\
	    random_sum_to(sm - rand, nterms - sterms, lo, hi)

seed()
vals = random_sum_to(0.0, 3, -1.0, 1.0)
i = 0
for v in vals:
    print repr(i) + ' ' + repr(v)
    i += 1
print 'sum ' + repr(sum(vals))
