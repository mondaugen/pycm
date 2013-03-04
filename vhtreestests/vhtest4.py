# Testin' vhtrees
from vhtrees import *
from formgenerator import *
from cmrandom import *
from random import *
from cmmath import *


def temp_form_gen(depth, minlen):
    formfreqs = n_randoms_that_sum_to_k(3,minlen/2)
    return generate_random_form_from_frequencies(formfreqs)

def temp_len_gen(depth):
    return randrange(6,9)

s = Simultaneous('a')

s.grow_vh_tree_w_lengths(3, temp_form_gen, a_vert_generator, temp_len_gen)

ptr = []
s.get_all_deep_leaf_lengths(ptr)
for i in ptr:
    print repr(i)
b = [y for x, y in ptr]
print repr(b)
gcd = cm_gcd(b)
print repr(gcd)
newptr = []
lensum = Fraction(0)
for name, frac in ptr:
    if lensum == 1:
	print "-----: "+repr(lensum)
	lensum = 0
    print "Lensum: "+repr(lensum)
    lensum = lensum + frac
    mult = gcd.denominator / frac.denominator
    newptr.append((name,frac,frac.numerator*mult,frac.denominator*mult))
    print repr(newptr[-1])

fracsum = int(sum([y for x, y in ptr]))
print "Fraction Sum: " +repr(sum([y for x, y in ptr]))
bigsum = sum([y for w, x, y, z in newptr])
print "Big sum:      " + repr(sum([y for w, x, y, z in newptr]))
print "Big sum/gcd:  " + repr(sum([y for w, x, y, z in newptr])/gcd.denominator)


seq = [[] for x in xrange(bigsum/fracsum)]
idx = 0
for name, frac, l, d in newptr:
    seq[idx].append((name,l))
    idx = idx + l
    if idx > (bigsum/fracsum):
	print "We are mis-aligned after " + repr((name,frac,l,d))
	print "Index is " + repr(idx)
	idx = 0
    if idx == (bigsum/fracsum):
	idx = 0

print "The sequence"

for l in seq:
    print repr(l)

print "Length: " + repr(len(seq))



    
#print "sum: " + repr(sum(ptr))

#gcd = cm_gcd(ptr)
#print vh_str_rep_expand(str(s))
#for i in ptr:
#    print repr(i/gcd)

