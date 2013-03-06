class Dumb:
    def __init__(self, dumbref):
	self.dumbref = dumbref

seqdict = {1:'balls', 2:'lyfe', 3:'cats'}

D = Dumb(seqdict)

print "Before change"
print D.dumbref 

tmp = seqdict.pop(1)
seqdict[10] = tmp

print "After change"
print D.dumbref

newdict = dict()
for k in sorted(seqdict.keys()):
    newdict[ k + 2 ] = seqdict.pop(k)
for k in newdict.keys():
    seqdict[k] = newdict[k]

#seqdict = newdict

print "After another change"
print D.dumbref

print "But I thought newdict was"
print newdict
