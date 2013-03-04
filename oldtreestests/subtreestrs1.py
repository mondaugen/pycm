#!/usr/bin/env python
from form_trees import *
import sys
import string

depth	     = int(sys.argv[1])
sectionnames = list(sys.argv[2])
numdivs	     = int(sys.argv[3])

strs = [[] for x in xrange(depth)]

ft = form_tree_generator(depth, sectionnames, numdivs)

ft.print_leaves(strs[0])
for n in xrange(len(strs[0])):
    strs[0][n] = string.join([x for x in reversed(strs[0][n])],'')

for n in xrange(1,depth):
    s = []
    for st in strs[0]:
	s.append(st[:-n])
    strs[n] = list(set(s))

for s in strs:
    for t in s:
	print t



