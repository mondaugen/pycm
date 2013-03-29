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
    style of output (numbers | sc)
    path to pitch range file
    path to dynamic range file
    path to pitch contour file
    path to dynamic contour file
    path to chord sequence file
    path to rhythm sequence file

    example useage:
    ./cmloadingtests5_b.py sc ./testfiles/pitch-range-1.dat
    ./testfiles/dynamic-range-1.dat ./testfiles/contour-2.dat
    ./testfiles/contour-2.dat ./testfiles/chords-3.dat
    ./testfiles/rhythm-contour-2.dat > ./testfiles/render-2.dat
    
'''

if len(sys.argv) != 8:
    sys.stderr.write(__doc__)
    exit()


pitchrange = RangeSequence(f=open(sys.argv[2],'r'))
dynrange = RangeSequence(f=open(sys.argv[3],'r'))
pitchcs = ContourSequence(f=open(sys.argv[4], 'r'))
dyncs = ContourSequence(f=open(sys.argv[5], 'r'))
chs = ChordSequence(f=open(sys.argv[6], 'r'))
rhs = RhythmSequence(f=open(sys.argv[7], 'r'))

cnc = ContourRhythmNoteDynSeq(rhs,chs,pitchrange,pitchcs,dynrange,dyncs)

if sys.argv[1] == 'numbers':
    cnciter = iter(cnc)
    for e in cnc:
        if len(e) == 3:
	   time, note, length = e
	   print length, note
        if len(e) == 4:
	   time, note, dynamic, length = e
	   print length, note, dynamic

elif sys.argv[1] == 'sc':
    cnciter = iter(cnc)
    for e in cnc:
        if len(e) == 3:
	   time, note, length = e
	   print "[ %f, [\\pitch, %d, \\amp, %s]]" % (length, -1, '-inf')
        if len(e) == 4:
	   time, note, dynamic, length = e
	   print "[ %f, [\\pitch, %f, \\amp, %f]]" % (length, note, dynamic)


