from cmmath import *
from fractions import *

keys = [ Fraction(-3,5), Fraction(2,5), Fraction(8,5), Fraction(23,10),\
	Fraction(37,10) ]
newkeys = []
for k in keys:
    newkeys.append(cm_round(k, Fraction(1), Fraction(1,2)))

print "Old keys"
for k in keys:
    print k
print "New keys"
for k in newkeys:
    print k

print "Some keys"

d = { Fraction(4,3):'bate', Fraction(-3,7):'parasol', Fraction(6,11):'love' }
for k in sorted(d.keys()):
    print k

