# Testin' vhtrees
from vhtrees import *
from formgenerator import *
from cmrandom import *
from random import *
from fractions import *
from cmmath import *
from math import *
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

startdepth = 3

def temp_form_gen(depth,newlen,curnode):
    if curnode.parent != None:
	if curnode.parent.name == 'D':
	    return generate_random_form_from_distinctness(4,3)
    return generate_random_form_from_distinctness(8,3)
#    return generate_random_form_from_distinctness(newlen/2,\
#	    int(log(newlen/2)/log(2))+1)
#    return generate_random_form_from_distinctness(*choice([(2,2),(4,3),(8,3)]))

def temp_len_gen(depth,curnode):
    if curnode.parent != None:
	if curnode.parent.name == 'D':
	    return 4
    return choice([16])

def my_depth_adjust(depth,curnode):
    return depth

def another_vert_generator(depth,curnode):
    column = []
#    if (depth == (3)):
#	for i in xrange(2):
#	    column.append(Sequential(chr(ord('A') + i)))
    if (depth == (2)):
	for i in xrange(4):
	    column.append(Sequential(chr(ord('A') + i)))
    else:
	    column.append(Sequential(chr(ord('A'))))
    return column

# see what track an element is in, return -1 if it isn't in these tracks
def what_track(elem, trks):
    e = elem.translate(None,string.ascii_lowercase)
    if e in trks:
	return trks.index(e)
    return -1

# strip out the capital letters basically
def strip_track(elem):
    return elem.translate(None, string.ascii_uppercase)

s = Simultaneous('a')

s.grow_vh_tree_w_lengths(startdepth, temp_form_gen,\
	another_vert_generator, temp_len_gen, my_depth_adjust)

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
formstrs = []
for p in parts:
    t = p.translate(None,string.ascii_lowercase)
    tracks.append(t)
    formstrs.append(p.translate(None,string.ascii_uppercase))
tracks = list(set(tracks))
formstrs = list(set(formstrs))

#print "num tracks: "+repr(len(tracks))
#for se in seqary:
#    print repr(se)

#print length, number of formal elements, number of tracks
pdict = list(set(parts))
print repr(int(gcd.denominator)), repr(len(formstrs)), repr(len(tracks))
#for x, y, z in deltaseq:
for i in xrange(len(seqary)):
    for j in xrange(len(seqary[i])):
	x, y = seqary[i][j]
	print repr(i), repr(what_track(x,tracks)), repr(int(y)),\
		repr(formstrs.index(strip_track(x)))
#    print repr(x), repr(y), repr(z)

#print repr(len(set(parts)))
#print repr(set(parts))

#print vh_str_rep_expand(str(s))
