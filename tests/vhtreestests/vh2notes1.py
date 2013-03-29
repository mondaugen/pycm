'''
    Expects that the first line of the file is:
    length, number of formal elements per track, number of tracks
    then a line saying how long the follow list is
    after that is a list of (we call it the element list):
    track number, element number, length
    after this is the sequence of the piece, each entry of which consists of:
    time, track, length, element number

    For every element in the element list, generate a sequence of notes that is
    equal to the length of the element

    Then play the piece by going through the sequence, looking up the
    sub-sequence corresponding to the track and element numbers and writing the
    contained events, offset by the current index, to a list, each entry
    containing:
    time, track, pitch, dynamic, notelength

    Args are pitch offset
'''
import sys
import string
import random
import wander

if len(sys.argv) < 3:
    raise Exception("Not enough arguments, need progname, pitchoffset,\
	    length multiplier")

poffset = int(sys.argv[1])

# multiply the element lengths by a constant for variety
elemlenmult = int(sys.argv[2])

pitches = [0,2,4,5,7,9,11,12,14,16,17,19,21,23,24]
lowdynrange = [20,60]
hidynnrange = [40,90]

length, numelems, numtracks = sys.stdin.readline().split()
length = int(length)
numelems = int(numelems)
numtracks = int(numtracks)

elemlistlen = int(sys.stdin.readline())

# For storing the lengths by [track][element]
trelems = [[[] for x in xrange(numelems)] for y in xrange(numtracks)]
# For storing the sequences by [track][element]
trelseqs = [[[] for x in xrange(numelems)] for y in xrange(numtracks)]

for i in xrange(elemlistlen):
    tnum, enum, elen = sys.stdin.readline().split()
    tnum = int(tnum)
    enum = int(enum)
    elen = int(elen)
#    sys.stderr.write(str((tnum,enum,elen))+'\n')
    trelems[tnum][enum] = elen * elemlenmult

for i in xrange(numtracks):
    for j in xrange(numelems):
	seqlen = trelems[i][j]
	ptr = 0
	notelens = []
	while seqlen > 0:
	    notelen = random.randrange(seqlen) + 1
	    notelens.append((ptr,notelen))
	    ptr = ptr + notelen
	    seqlen = seqlen - notelen
	lo = random.randrange(*lowdynrange)
	hi = random.randrange(*hidynnrange)
	a = wander.int_wander(lo, hi, 0, abs(hi-lo)+1, 0, 120, len(notelens))
	ita = iter(a)
	# could wander the pitches too
	for t, l in notelens:
	    pitch = random.choice(pitches)
	    trelseqs[i][j].append((t, pitch, ita.next(), l))

# print the number of tracks on the first line
print repr(numtracks)
# then print the score data
for line in sys.stdin.readlines():
    t, tr, l, el = line.split()
    t = int(t) * elemlenmult
    tr = int(tr)
    l = int(l)
    el = int(el)
    for st, pitch, dy, le in trelseqs[tr][el]:
	print st+t, tr, pitch + poffset, dy, le






