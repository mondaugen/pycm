# test loading length_intlist pairs
import cmloaders
from cmsequence import *
from fractions import *

#d = cmloaders.load_length_intlist_pairs(open('./testfiles/2.dat','r'))
#d2= cmloaders.load_length_float_pairs(open('./testfiles/3.dat','r'))

#print d
#print d2

rs = RangeSequence(f=open('./testfiles/4b.dat','r'))
cs = ContourSequence(f=open('./testfiles/5.dat', 'r'))
chs = ChordSequence(f=open('./testfiles/6.dat', 'r'))
rhs = RhythmSequence(f=open('./testfiles/rhythm1.dat', 'r'))

print rs.ranges
print cs.contour
print chs.chords

cnc = ContourRhythmNoteCombSeq(rhs,chs,rs,cs)

i = Fraction(0)
while i < Fraction(1):
    note, length = cnc[i]
    print float(i), note, float(length)
    i = i + Fraction(1,24)
