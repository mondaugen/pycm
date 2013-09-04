from fractions import *
'''
Loaders storing keys as floats for speed
'''

def correct_keys_for_length(seqdict, length, newlength=1.0):
    '''
    Basically, if the keys represent some kind of index in a sequence, then this
    makes all indices between 0 and newlength.
    '''
    tmpdict = dict()
    for k in sorted(seqdict):
	    tmpdict[k*newlength/length] = seqdict[k]
    return tmpdict

def load_length_string_pairs(f,totallength=1.0):
    '''
    Loads string lists from a file stored in the format:
    <length>, string
    .
    .
    into a dictionary of time:string pairs ie:
    {123/1000:'my new band is syskill', etc.}
    '''
    ptr = 0.0
    tmpdict = dict()
    for line in f:
	length, string = tuple(line.rstrip().split(','))
	length = Fraction(length.strip())
	tmpdict[ptr] = string.strip()
	ptr = ptr + float(length)

    return correct_keys_for_length(tmpdict, ptr, totallength)

def load_length_intlist_pairs(f,totallength=1.0):
    '''
    Loads int lists from a file stored
    in the format:
    <length>, int1 int2 ... intn
    into a dictionary of time:([ints]) pairs ie:
    {123/1000:([0 4 7]), etc. }
    '''

    ptr = 0.0
    tmpdict = dict()
    for line in f:
	length, pcs = tuple(line.rstrip().split(','))
	length = Fraction(length.strip())
	pcstrs = pcs.strip().split(' ')
	pcs = []
	for p in pcstrs:
	    pcs.append((int(p.strip())))
	tmpdict[ptr] = pcs
	ptr = ptr + float(length)

    # Now we divide all the keys by length to normalize the sequence length
    # to totallength 
    return correct_keys_for_length(tmpdict, ptr, totallength)

def load_length_pcs_pairs(f,totallength=1.0):
    '''
    Loads pitch-class-sets (often used to represent chords) from a file stored
    in the format:
    <length>, pc1 pc2 ... pcn
    into a dictionary of time:(pcs) pairs ie:
    {123/1000:([0 4 7]), etc. }
    '''
    return load_length_intlist_pairs(f,totallength)

def load_length_float_pairs(f, totallength=1.0):
    '''
    Loads floating point numbers (often used to represent contours) from a file
    stored in the format:
    <length>, fpn1
    .
    .
    into a dictionary of time:floating-point-number pairs ie:
    { 456/789:0.98736, etc. }
    '''
    ptr = 0.0
    tmpdict = dict()
    for line in f:
	length, fpn = tuple(line.rstrip().split(','))
	length = Fraction(length)
	fpn = float(fpn)
	tmpdict[ptr] = fpn
	ptr = ptr + float(length)

    return correct_keys_for_length(tmpdict, ptr, totallength)

