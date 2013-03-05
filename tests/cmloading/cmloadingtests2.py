from cmsequence import *
from fractions import *
cs = ContourSequence(f=open('./testfiles/5.dat', 'r'))

i = Fraction(0)
while i < Fraction(1):
    print cs[i]
    i = i + Fraction(1,24)
