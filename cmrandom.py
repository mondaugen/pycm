import random

'''A collection of functions involving randomness'''

def n_randoms_that_sum_to_k(n,k):
    '''Returns n numbers > 0 that sum to k. k must be positive. Note the
    distribution of the numbers in the result is not really great for large n
    and k. What you get is a few big numbers and a lot of 1s. How could we
    make the distribution more even? '''
    if k < 0:
	raise Exception('k: ',k,'must be positive')
    if n > k:
	raise Exception('n_randoms_that_sum_to_k: n',n,'cannot be greater than\
			    k',k)
    if n == k:
	return [1 for i in xrange(n)]
    if n < 2:
	return [k]
    #rand = random.randrange(1,(k - n + 1) + 1)
    #The distribution tries to weight mid range values more highly to make more
    #evenly sized pieces, the exact distribution may change
    rand = 1 + (int)(float(k - n + 1)*random.betavariate(2.0,2.0))
    return [rand] +\
	    n_randoms_that_sum_to_k(n-1, k - rand)

def random_reduce_by_summing(a,newl):
    '''Reduce a list by summing random k-tuples where k = len(a) / newl. If
    len(a) / newl == 0, it makes newl = len(a) see below.'''
    if len(a) / newl == 0:
	newl = len(a)
    if newl <= 0:
	newl = len(a)
    r = []
    k = len(a) / newl
    while len(a) > 0:
	s = 0
	for i in xrange(k):
	    s += a.pop(random.randrange(len(a)))
	r.append(s)
    return r
