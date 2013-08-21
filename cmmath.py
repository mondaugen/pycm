# Copyright 2013 Nicholas Esterer. All Rights Reserved.
import fractions
def cm_gcd(args):
    '''You should copy the list you put into args if you don't want to lose it
    (BUG)'''
    while len(args) > 1:
	r = args.pop()
	l = args.pop()
	args.append(fractions.gcd(l,r))
#    if len(args) > 1:
#	a = args.pop()
#	return fractions.gcd(a,cm_gcd(args))
    result = args.pop()
    return result

def cm_factorize(a, primes):
    '''Factor a number into primes. Primes must have available all the primes up
    to the number.'''
    i = 0
    if a == 1:
	return []
    while (a % primes[i]) != 0:
	i = i + 1
    f = [primes[i]]
    return f + cm_factorize(a/primes[i], primes)

def cm_primes_to_n(n):
    '''Return a list of all the primes up to n'''
    if n < 2:
	return [2]
    l = [True for i in xrange(n+1)]
    primes = []
    l[0] = False
    l[1] = False
    while True:
	i = 0
	while l[i] == False:
	    i = i + 1
	    if i > n:
		return primes
	primes.append(i)
	j = 0
	while i*j <= n:
	    l[i*j] = False
	    j = j + 1

def cm_lcm(a,b):
    '''Find x and y st. a*x = b*y = c and c is minimal'''
    # Find the factors of a and b
    facta = cm_factorize(a, cm_primes_to_n(a))
    factb = cm_factorize(b, cm_primes_to_n(b))
    facta.append(1)
    factb.append(1)
    for i in xrange(len(facta)):
	for j in xrange(len(factb)):
	    if facta[i] == factb[j]:
		facta[i] = 1
		factb[j] = 1
    if len(facta) > 0:
	proda = reduce(lambda x,y: x*y, facta)
    else:
	proda = 1
    if len(factb) > 0:
	prodb = reduce(lambda x,y: x*y, factb)
    else:
	prodb = 1
    return [prodb, proda]

#def cm_new_denom(nums, frac):
#    '''If frac is 1/q then for each n in nums n = 

def linear_interpolation(index, table):
    '''Linear interpolate between values in a table'''
    idxflr = math.floor(index)
    idxfract = index - idxflr
    print idxfract
    return table[int(idxflr)%len(table)]+ \
	(idxfract*(table[(int(idxflr)+1)%len(table)]-table[int(idxflr)%len(table)]))

def find_nearest(ary, val):
    '''
    Find the closest value in ary to val.
    '''
    nearest = ary[0]
    smallestdistance = abs(ary[0]-val)
    for i in xrange(1, len(ary)):
	    distance = abs(ary[i]-val)
	    if distance < smallestdistance:
	      smallestdistance = distance
	      nearest = ary[i]
    return nearest

def cm_round(n, d, offset=0):
    '''
    Round n to nearest d. Offset is used as follows:
    Say you have the numbers -0.6, 0.4, 3.7.
    If d is 1 and offset 0, these become -1.0, 0, 4.0.
    If d is 1 and offset 0.5, these become -0.5, 0.5, 3.5.
    If the value is halfway between two round points, the algorithm rounds up to
    the absolute highest value, that is, if offset is 0, d is 1, then -0.5
    rounds to -1.0 and 0.5 rounds to 1.0 
    '''
    n = n - offset
    q = n % d
    if q < (d / 2):
	n = n - q
    else:
	n = n - q + d
    return n + offset


