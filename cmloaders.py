from fractions import *

def correct_keys_for_length(seqdict, length):
    '''
    Basically, if the keys represent some kind of index in a sequence, then this
    makes all indices between 0 and 1.
    '''
    tmpdict = dict()
    for k in sorted(seqdict):
	    tmpdict[Fraction(Fraction(k),length)] = seqdict[k]
    return tmpdict

def load_length_intlist_pairs(f):
    '''
    Loads int lists from a file stored
    in the format:
    <length>, int1 int2 ... intn
    into a dictionary of time:([ints]) pairs ie:
    {123/1000:([0 4 7]), etc. }
    '''

    ptr = Fraction(0)
    tmpdict = dict()
    for line in f:
	length, pcs = tuple(line.rstrip().split(','))
	length = Fraction(length.strip())
	pcstrs = pcs.strip().split(' ')
	pcs = []
	for p in pcstrs:
	    pcs.append((int(p.strip())))
	tmpdict[ptr] = pcs
	ptr = ptr + length

    # Now we divide all the keys by length to normalize the sequence length
    # to 1
    return correct_keys_for_length(tmpdict, ptr)

def load_length_pcs_pairs(f):
    '''
    Loads pitch-class-sets (often used to represent chords) from a file stored
    in the format:
    <length>, pc1 pc2 ... pcn
    into a dictionary of time:(pcs) pairs ie:
    {123/1000:([0 4 7]), etc. }
    '''
    return load_length_intlist_pairs(f)

def load_length_float_pairs(f):
    '''
    Loads floating point numbers (often used to represent contours) from a file
    stored in the format:
    <length>, fpn1
    .
    .
    into a dictionary of time:floating-point-number pairs ie:
    { 456/789:0.98736, etc. }
    '''
    ptr = Fraction(0)
    tmpdict = dict()
    for line in f:
	length, fpn = tuple(line.rstrip().split(','))
	length = Fraction(length)
	fpn = float(fpn)
	tmpdict[ptr] = fpn
	ptr = ptr + length

    return correct_keys_for_length(tmpdict, ptr)

