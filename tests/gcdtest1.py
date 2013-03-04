from cmmath import *
from fractions import *

v = ['1/16','1/16','1/12','1/6','1/16','1/16','3/40','12/40','1/16','1/16']

for i in xrange(len(v)):
    v[i] = Fraction(v[i])

print(cm_gcd(v))
