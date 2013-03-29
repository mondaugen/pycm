# Testin' vhtrees
from vhtrees import *
from formgenerator import *
from cmrandom import *
from random import *
from fractions import *
from cmmath import *


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

for se in seq:
    print repr(se)

b = [y for x, y, z in seq]
gcd = cm_gcd(b)
seqary = [[] for x in xrange(gcd.denominator)]
parts = []
for t, l, name in seq:
    mult = gcd.denominator / t.denominator
    idx = t / gcd
    mult = gcd.denominator / l.denominator
    newlen = l / gcd
    print repr(idx)
    seqary[int(idx)].append((name,int(newlen)))
    parts.append(name[-4:])

for se in seqary:
    print repr(se)

print repr(len(set(parts)))
print repr(set(parts))

#print vh_str_rep_expand(str(s))
