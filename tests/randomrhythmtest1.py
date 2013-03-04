import rhythmgenerator
import formgenerator
import random
from itertools import product

a = formgenerator.generate_random_form_from_distinctness(8,4)
b = rhythmgenerator.stretch_form_randomly(a,32)
c = rhythmgenerator.get_formal_length_tuples(a,b,4)
#print repr(c)
cc = {}
for x, y in set(c):
    aa = formgenerator.generate_random_form_from_distinctness(4,3,x)
    bb = rhythmgenerator.stretch_form_randomly(aa,y)
    cc[x] = rhythmgenerator.get_formal_length_tuples(aa,bb,1)

d = []
for x, y in c:
    d.append(cc[x])
trans = [u+w for u,w in product('abcd', repeat=2)]
random.shuffle(trans)
for x in d:
    for y, z in x:
	print repr(trans.index(y)) + ' ' + repr(z) + ';'


