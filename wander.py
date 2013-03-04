import random

def clip(val, mi, ma):
    if val > ma:
	return ma
    elif val < mi:
	return mi
    else:
	return val

def wander(s, g, kmi, kma, lbnd, ubnd, le):
    random.seed()
    '''Wander from s to g stepping by at most kma and at least kmi, remaining
    between lbnd and ubnd, taking len steps'''
    try:
	if le < 1:
	    raise Exception('Bad length:', le)
	if le == 1:
	    return [s] # Just return starting positon if length is 1
	if kmi > kma:
	    raise Exception('Bad kmi:', kmi,'or kma',kma)
	if not ((abs(g-s) >= kmi*(le-1)) and (abs(g-s) <= kma*(le-1))):
	    raise Exception('Unreachable goal',g,'from',s,'in',le,'steps')
	if (lbnd>s) or (lbnd>g) or (ubnd<s) or (ubnd<g):
	    raise Exception('Bad boundaries:',lbnd,ubnd)
	i = 0
	a = [s]
	i += 1
	while i < le:
	    ma = g - s - kmi*(le - 1 - i)
	    mi = g - s - kma*(le - 1 - i)
	    s += random.uniform(max(clip(kmi,mi,ma),lbnd-s),\
		    min(clip(kma,mi,ma),ubnd-s))
	    a.append(s)
	    i += 1
	return a
    except Exception as e:
	print "Error in wander:", e.args

def int_wander(s, g, kmi, kma, lbnd, ubnd, le):
    random.seed()
    '''Wander from s to g stepping by at most kma and at least kmi, remaining
    between lbnd and ubnd, taking len steps. Returns integers.'''
    try:
	if le < 1:
	    raise Exception('Bad length:', le)
	if le == 1:
	    return [s] # Just return starting positon if length is 1
	if kmi > kma:
	    raise Exception('Bad kmi:', kmi,'or kma',kma)
	if not ((abs(g-s) >= kmi*(le-1)) and (abs(g-s) <= kma*(le-1))):
	    raise Exception('Unreachable goal',g,'from',s,'in',le,'steps')
	if (lbnd>s) or (lbnd>g) or (ubnd<s) or (ubnd<g):
	    raise Exception('Bad boundaries:',lbnd,ubnd)
	i = 0
	a = [s]
	i += 1
	while i < le:
	    ma = g - s - kmi*(le - 1 - i)
	    mi = g - s - kma*(le - 1 - i)
	    s += int(random.uniform(max(clip(kmi,mi,ma),lbnd-s),\
		    min(clip(kma,mi,ma),ubnd-s)))
	    a.append(s)
	    i += 1
	return a
    except Exception as e:
	print "Error in wander:", e.args

def get_deltas(a):
    '''Take a list and return a list of length len(a)-1 of the deltas between
    items of a. ie: a= [1,0,2] returns [-1,2]'''
    rslt = []
    for i in xrange(0,len(a)-1):
	rslt.append(a[i+1]-a[i])
    return rslt

def make_segments(start,deltas):
    '''Take a starting point s and a list of deltas and make segments'''
    rslt = [start]
    for d in deltas:
	rslt.append(rslt[-1]+d)
    return rslt

def map_sections_to_deltas(deltas, sections):
    '''Take a set of deltas and a set of sections and return a list s.t. each
    section is mapped to a unique element in the delta list and the elements of
    the resulting list are these mappings divided by the frequency of each
    section in the mapping. ie. a possible result of deltas = [0.6,0.4] and
    sections = [a,b,b,a,a] is, a->0.6 and b->0.4 so [0.2,0.2,0.2,0.2,0.2]'''
    try:
	if(len(deltas) != len(set(sections))):
	    raise Exception('Delta length',len(deltas),\
		    'd.n.e length set of sections',len(set(sections)))
	fdict = dict() # frequency of each section
	pdict = dict() # resulting proportion of delta of each section
	for s in set(sections):
	    fdict[s] = sections.count(s)
	    pdict[s] = deltas.pop()
	rslt = []
	for s in sections:
	    rslt.append(pdict[s]/fdict[s])
	return rslt
    except Exception as e:
	print 'error in map_sections_to_deltas:',e.args



'''
a = wander(0.0, 0.0, -1.0, 1.0, -1.0, 1.0, 4)
deltas = get_deltas(a)
sects = ['a','b','b','a','c','a']
random.shuffle(deltas)
r = map_sections_to_deltas(deltas,sects)
q = make_segments(0.0,r)
for v in q:
    print v
'''
