import rhythmgenerator
import formgenerator
import random
from itertools import product

random.seed()
a = formgenerator.generate_random_form_from_distinctness(8,3)
b = rhythmgenerator.stretch_form_randomly(a,16)
c = rhythmgenerator.get_formal_length_tuples(a,b,4)
a2 = formgenerator.generate_random_form_from_distinctness(8,3)
b2 = rhythmgenerator.stretch_form_randomly(a2,16)
c2 = rhythmgenerator.get_formal_length_tuples(a2,b2,4)
#print repr(c)
cc1 = {}
cc2 = {}
for x, y in set(c):
    aa = formgenerator.generate_random_form_from_distinctness(4,3,x)
    bb = rhythmgenerator.stretch_form_randomly(aa,y)
    cc1[x] = rhythmgenerator.get_formal_length_tuples(aa,bb,1)
for x, y in set(c2):
    aa = formgenerator.generate_random_form_from_distinctness(4,3,x)
    bb = rhythmgenerator.stretch_form_randomly(aa,y)
    cc2[x] = rhythmgenerator.get_formal_length_tuples(aa,bb,1)

d1 = []
d2 = []
for x, y in c:
    d1.append(cc1[x])
    d2.append(cc2[x])
trans = [u+w for u,w in product('abcd', repeat=2)]
random.shuffle(trans)
trans2 = trans
random.shuffle(trans2)
scr1 = []
scr2 = []
for x, y in zip(d1,d2):
    for yy, zz in zip(x,y):
	scr1.append((yy[1],trans.index(yy[0])))
	scr2.append((zz[1],trans2.index(zz[0])))
accum = 0
accumscr1 = []
for x, y in scr1:
    accumscr1.append((accum, y))
    accum += x
accum = 0
accumscr2 = []
for x, y in scr2:
    accumscr2.append((accum, y))
    accum += x

accumscr = accumscr1+accumscr2
deltascr = []
prev = 0
for x, y in sorted(accumscr):
    deltascr.append((x - prev, 'drums', y))
    prev = x

for x, y, z in deltascr:
    print x, y, z, ';'
