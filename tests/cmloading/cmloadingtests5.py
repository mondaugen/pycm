#!/usr/bin/env python
# test loading length_intlist pairs
import cmloaders
from cmsequence import *
from fractions import *
import cmmath
import sys

__doc__ =\
'''
args are:
    path to pitch range file
    path to dynamic range file
    path to pitch contour file
    path to dynamic contour file
    path to chord sequence file
    path to rhythm sequence file
'''

if len(sys.argv) != 7:
    sys.stderr.write(__doc__)
    exit()


pitchrange = RangeSequence(f=open(sys.argv[1],'r'))
dynrange = RangeSequence(f=open(sys.argv[2],'r'))
pitchcs = ContourSequence(f=open(sys.argv[3], 'r'))
dyncs = ContourSequence(f=open(sys.argv[4], 'r'))
chs = ChordSequence(f=open(sys.argv[5], 'r'))
rhs = RhythmSequence(f=open(sys.argv[6], 'r'))

cnc = ContourRhythmNoteDynSeq(rhs,chs,pitchrange,pitchcs,dynrange,dyncs)

cnciter = iter(cnc)
for e in cnc:
    print e
