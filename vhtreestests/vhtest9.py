# Testin' vhtrees
from vhtrees import *
from formgenerator import *
from cmrandom import *
from random import *
from fractions import *
from cmmath import *
import string

seed()


''' Prints out a sequence of events in this format:
    The first line is a pair of numbers: the first is the total length, the
    second is the number of possible different events.
    Each successive line afterward is the ABSOLUTE TIME OF the events, an
    event identifier (just a number) and the length of the event

    To find the number of "tracks" we strip all the lowercase letters out of the
    formal strings. The number of unique resulting strings is the number of
    tracks... Not quite
'''

startdepth = 4

def temp_form_gen(depth,newlen):
    return generate_random_form_from_distinctness(8, 3)

def another_vert_generator(depth):
    column = []
    if depth <= (2):
	for i in xrange(2):
	    column.append(Sequential(chr(ord('A') + i)))
    else:
	    column.append(Sequential(chr(ord('A'))))
    return column

def temp_len_gen(depth):
    return 16

s = Simultaneous('a')

s.grow_vh_tree_w_lengths(startdepth, temp_form_gen, another_vert_generator, temp_len_gen)

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
#stripidx = 2
for t, l, name in seq:
    mult = gcd.denominator / t.denominator
    idx = t / gcd
    mult = gcd.denominator / l.denominator
    newlen = l / gcd
#    print repr(idx)
    seqary[int(idx)].append((name,int(newlen)))
    deltatime = idx - lasttime
    deltaseq.append((int(deltatime),name,int(newlen)))
    lasttime = idx
    parts.append(name)
# determine the number of tracks and their strings
tracks = []
for p in parts:
    t = p.translate(None,string.ascii_lowercase)
    tracks.append(t)
tracks = list(set(tracks))

#print "num tracks: "+repr(len(tracks))

# see what track an element is in, return -1 if it isn't in these tracks
def what_track(elem, trks):
    e = elem.translate(None,string.ascii_lowercase)
    if e in trks:
	return trks.index(e)
    return -1

# strip out the capital letters basically
def strip_track(elem):
    return elem.translate(None, string.ascii_uppercase)

#for se in seqary:
#    print repr(se)

pdict = list(set(parts))
print repr(gcd.denominator), repr(len(pdict))
#for x, y, z in deltaseq:
for i in xrange(len(seqary)):
    for j in xrange(len(seqary[i])):
	x, y = seqary[i][j]
	print repr(i), repr(what_track(x,tracks)), repr(y), repr(strip_track(x))
#    print repr(x), repr(y), repr(z)

#print repr(len(set(parts)))
#print repr(set(parts))

#print vh_str_rep_expand(str(s))
