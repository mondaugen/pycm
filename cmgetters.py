import cminterputils
import cmmath
import cmbisect


def get_two_closest_keys(seqdict, key):
    it = iter(sorted(seqdict.keys()))
    prevkey = None
    nextkey = None
    while True:
	try:
	    nextkey = it.next()
	except StopIteration:
	    return (prevkey, None)
	if nextkey > key:
	    return (prevkey, nextkey)
	prevkey = nextkey

def get_quantized_key(seqdict, key, divisor=0, offset=0):
    lkey, rkey = get_two_closest_keys(seqdict, key)
    closestkey = None
    if lkey != None:
	if divisor != 0:
	    lkey = cmmath.cm_round(lkey,divisor,offset)
    if rkey != None:
	if divisor != 0:
	    rkey = cmmath.cm_round(rkey,divisor,offset)
    # prefer the lesser key
    if lkey != None:
	if lkey == key:
	    return lkey
    if rkey != None:
	if rkey == key:
	    return rkey
    return None
    
def quantized_get(seqdict, key, divisor=0, offset=0):
    newkey = None
    newkey = get_quantized_key(seqdict, key, divisor, offset)
    if newkey != None:
	return seqdict[newkey]
    return None

def get_item_at_key(seqdict, key):
    '''
    Return the item at key only if it is in seqdict, None, otherwise.
    '''
    if key in seqdict.keys():
	return seqdict[key]
    else:
	return None

def get_item_and_length_at_key(seqdict, key, totallength=1):
    '''
    Return the item and the distance between it and the next item as a tuple, or the
    distance between it and the totallength if it is the last item. Raises
    ValueError if the key is greater than totallength. Returns None if key not
    in seqdict.
    THIS is faster, not tested
    '''
    if key > totallength:
	raise ValueError
    if key not in seqdict:
	return None
    sortedkeys = sorted(seqdict.keys())
    secondindex = sortedkeys.index(key) + 1
    if secondindex == len(sortedkeys):
	secondkey = totallength
    else:
	secondkey = sortedkeys[secondindex]
    return (seqdict[key], secondkey - key)

def get_next_lowest_item(seqdict, key):
    '''
    Sequence is a dictionary stored as {<time>:<value>,...} pairs.
    Go through the sequence and look for an item with key
    equal to or less than key. Return the item at key.
    Faster, not tested.
    '''
    sortedkeys = sorted(seqdict.keys())
    lekey = None
    try:
	lekey = cmbisect.find_le(sortedkeys, key)
    except ValueError:
	return None
    return seqdict[lekey]

def get_next_greatest_item(seqdict, key):
    '''
    Sequence is a dictionary stored as {<time>:<value>,...} pairs.
    Go through the sequence and look for an item with key
    greater than key. Return the item at key.
    Faster, not tested.
    '''
    sortedkeys = sorted(seqdict.keys())
    gtkey = None
    try:
	gtkey = cmbisect.find_gt(sortedkeys, key)
    except ValueError:
	return None
    return seqdict[gtkey]

def get_linearly_interpolated_item(seqdict, key):
    '''
    Go through the sequence until key is equal or greater than the first index
    and less than the next index. Return an interpolated value between the two
    indices.
    '''
    lekey = None
    try:
	lekey = cmbisect.find_le(seqdict.keys(), key)
    except ValueError:
	# Key is less than lowest key in list, return first item
	return seqdict[iter(sorted(keys())).next()]
    gtkey = None
    try:
	gtkey = cmbisect.find_gt(seqdict.keys(), key)
    except:
	# lekey is the last key
	return seqdict[lekey]
    return cminterputils.linterp(\
	lekey, seqdict[lekey], gtkey, seqdict[gtkey], key)
    
