# Testin' vhtrees
from vhtrees import *
from formgenerator import *
from cmrandom import *
from random import *
from fractions import *
from cmmath import *

seed()


def temp_form_gen(depth, minlen,node):
    formfreqs = n_randoms_that_sum_to_k(3,minlen)
    return generate_random_form_from_frequencies(formfreqs)

def another_vert_generator(depth,node):
    column = []
    for i in xrange(1):
	column.append(Sequential(chr(ord('A') + i)))
    return column

def temp_len_gen(depth,node):
    return 8
#    return choice([4,5,6])

s = Simultaneous('a')

s.grow_vh_tree_w_lengths(4, temp_form_gen, another_vert_generator, temp_len_gen)

seq = []
curlen = Fraction(0)
s.fill_w_seq(seq, curlen)
seq.sort()

#for se in seq:
#    print repr(se)

print seq
print '----'

b = [y for x, y, z in seq]
gcd = cm_gcd(b)
seqary = [[] for x in xrange(gcd.denominator)]
for t, l, name in seq:
    mult = gcd.denominator / t.denominator
    idx = t / gcd
    mult = gcd.denominator / l.denominator
    newlen = l / gcd
    #print repr(idx)
    seqary[int(idx)].append((name,int(newlen)))

for se in seqary:
    print repr(se)

for i in xrange(len(seqary)):
    seqary[i] = tuple(seqary[i])
print '----'

for se in set(seqary):
    print repr(se)

#print vh_str_rep_expand(str(s))
