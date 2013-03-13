# test loading length string pairs
import cmloaders
from cmsequence import *
from fractions import *

rhs = RhythmSequence(f=open('./testfiles/rhythm1.dat', 'r'))

print rhs.rhythm

rhs.divisor = Fraction(1,2)
rhs.offset  = Fraction(1,8)

i = Fraction(0)
while i < Fraction(1):
    print rhs[i]
    i = i + Fraction(1,32)

print '-----'
rhs.divisor = Fraction(1,4)
rhs.offset  = 0

i = Fraction(0)
while i < Fraction(1):
    print rhs[i]
    i = i + Fraction(1,32)

print '-----'
rhs.divisor = 0

i = Fraction(0)
while i < Fraction(1):
    print rhs[i]
    i = i + Fraction(1,32)
