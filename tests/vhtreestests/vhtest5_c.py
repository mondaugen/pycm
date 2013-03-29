# Testin' vhtrees
from vhtrees import *
from formgenerator import *
from cmrandom import *
from random import *
from fractions import *
from cmmath import *


''' Prints out a sequence of events in this format:
    The first line is a pair of numbers: the first is the total length, the
    second is the number of possible different events.
    Each successive line afterward is the delta time between two events, an
    event identifier (just a number) and the length of the event
'''


def temp_form_gen(depth, minlen):
    formfreqs = n_randoms_that_sum_to_k(3,minlen)
    return generate_random_form_from_frequencies(formfreqs)

def another_vert_generator(depth):
    column = []
    for i in xrange(4):
	column.append(Sequential(chr(ord('A') + i)))
    return column

def temp_len_gen(depth):
    return choice([4,5,6])

s = Simultaneous('a')

s.grow_vh_tree_w_lengths(3, temp_form_gen, another_vert_generator, temp_len_gen)

seq = []
curlen = Fraction(0)
s.fill_w_seq(seq, curlen)
seq.sort()

#for se in seq:
#    print repr(se)

b = [y for x, y, z in seq]
gcd = cm_gcd(b)
seqary = [[] for x in xrange(gcd.denominator)]
parts = []
lasttime = 0
deltaseq = []
stripidx = 2
for t, l, name in seq:
    mult = gcd.denominator / t.denominator
    idx = t / gcd
    mult = gcd.denominator / l.denominator
    newlen = l / gcd
#    print repr(idx)
    seqary[int(idx)].append((name[-stripidx:],int(newlen)))
    deltatime = idx - lasttime
    deltaseq.append((int(deltatime),name[-stripidx:],int(newlen)))
    lasttime = idx
    parts.append(name[-stripidx:])

#for se in seqary:
#    print repr(se)

pdict = list(set(parts))
print repr(gcd.denominator), repr(len(pdict))
for x, y, z in deltaseq:
    print repr(x), repr(pdict.index(y)), repr(z)
#    print repr(x), repr(y), repr(z)

#print repr(len(set(parts)))
#print repr(set(parts))

#print vh_str_rep_expand(str(s))
