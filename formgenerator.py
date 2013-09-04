# Copyright 2013 Nicholas Esterer. All Rights Reserved.
import random
import cmrandom

def generate_random_form_from_frequencies(a, prefix=''):
    '''a is a list of frequencies of each part of a form. The convention is that
    index 0 is 'a', index 1 is 'b' etc. This function will return a form in the
    style ['a','b','a','a'] or whatever. For example, if you give the function,
    [2,3,1], the function might give you [b,a,b,c,b,a] or some other permutation
    of this. The function also accepts a prefix (default is the empty string)
    with which it prepends the form so for the above example, if the prefix were
    set as 'k' then the result would be ['ka','kb','ka','ka'] '''
    c = ord('a')
    r = []
    for i in xrange(len(a)):
	for j in xrange(a[i]):
	    r.append(prefix+chr(c+i))
    random.shuffle(r)
    return r

def generate_random_form_from_distinctness(totlen, d, prefix=''):
    '''d is a number that means the number of parts of the form that are
    different and totlen is the length of the form. Here are some examples:
    totlen = 8, d = 1 : ['a','a','a','a','a','a','a','a'], totlen = 4, d = 3:
    ['a','b','a','c']. Prefix is just some string to prepend to the form, ie.
    prefix 'brahms' would give, for the latter example:
    ['brahmsa','brahmsb','brahmsa','brahmsc'].'''
    formfreqs = cmrandom.n_randoms_that_sum_to_k(d, totlen)
    return generate_random_form_from_frequencies(formfreqs, prefix)

def count_formal_elements(a):
    '''Count the number of occurences of each section of a form a return a
    dictionary with the frequencies'''
    aset = set(a)
    fdict = {}
    for k in aset:
	fdict[k] = a.count(k)
    fdict = dict(sorted(fdict.items()))
    return fdict

