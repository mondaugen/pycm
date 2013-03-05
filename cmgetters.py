import cminterputils

def get_next_lowest_item(seqdict, key):
    '''
    Sequence is a dictionary stored as {<time>:<value>,...} pairs.
    Go through the sequence and look for an item with key
    equal to or less than key. Return the item at key.
    '''
    it = iter(sorted(seqdict))
    try:
	prv = it.next()
    except StopIteration:
	return None

    while True:
	try:
	    nxt = it.next()
	except StopIteration:
	    return seqdict[prv]
	if nxt <= key:
	    prv = nxt
	else:
	    return seqdict[prv]

def get_linearly_interpolated_item(seqdict, key):
    '''
    Go through the sequence until key is equal or greater than the first index
    and less than the next index. Return an interpolated value between the two
    indices.
    '''
    it = iter(sorted(seqdict))
    try:
	prv = it.next()
    except StopIteration:
	return None

    while True:
	try:
	    nxt = it.next()
	except StopIteration:
	    return seqdict[prv]
	if nxt <= key:
	    prv = nxt
	else:
	    return cminterputils.linterp(\
		    prv, seqdict[prv], nxt, seqdict[nxt], key)
    
