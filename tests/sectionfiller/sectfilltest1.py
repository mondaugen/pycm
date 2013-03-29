from sectionfiller import *
from fractions import *
import random

random.seed()

def lenfun(aux):
    return Fraction(random.randint(1,24),24)

def datumfunc(aux):
    return 48 + random.choice([0,2,4,5,7,9,11,12])

sf = SectionFiller(lenfun, datumfunc)

for s in sf.get_list_of_data():
    print s
    
