def index_multiplier(seqdict, mult):
    '''
    If you have a sequence {0:v1,1:v2,4:v3} you might want it to be
    {0:v1, 4:v2, 16:v3}. Then mult would be 4 blah blah
    '''
    newdict = dict()
    for k in sorted(seqdict):
	newdict[Fraction(k * mult)] = seqdict[k]

    return newdict

class SequenceDictionary:
    pass
#    self.dictionary = dict()
#    self.length = 0

