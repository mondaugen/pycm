#!/usr/bin/env python
__doc__ = '''
Creates a rhythm of notes or rests
args are: contourmaker.py <depth> <num_sections> <number_of_divisions>
num_sections must be less than or equal to number of divisions
'''
import form_trees
import sys
from vhtrees import *
from formgenerator import *
from fractions import *
from sectionfiller import *
import random
from cmrandom import *
import argparse
import formfiller

__doc__ = "\
generate a form file which is just a list of strings separated by newlines, \
some of which are the same."

parser = argparse.ArgumentParser(\
	description=__doc__)

__depth_help__ = 'How deep the form tree grows.'
parser.add_argument('--depth', dest='depth', nargs='?',\
	const=2, default=2, help=__depth_help__, type=int)

__nsections_help__ = 'The number of distinct sections at a given layer of the \
tree.'

parser.add_argument('--nsections', dest='nsections', nargs='?',\
	const=1, default=1, help=__nsections_help__, type=int)

__ndivisions_help__ = 'The total number of sections at a given layer of the tree \
some of which will repeat.'

parser.add_argument('--ndivisions', dest='ndivisions', nargs='?',\
	const=1, default=1, help=__ndivisions_help__, type=int)

parser.add_argument('--verbose', dest='verbose', action='store_true',\
	help='print the generated form to stderr')

args = parser.parse_args()

if args.nsections > args.ndivisions:
    sys.stderr.write("number of sections must be less than number of divisions\n")
    exit()

def temp_form_gen(depth, minlen,node):
    formfreqs = n_randoms_that_sum_to_k(args.nsections,minlen)
    return generate_random_form_from_frequencies(formfreqs)

def another_vert_generator(depth,node):
    column = []
    for i in xrange(1):
	column.append(Sequential(chr(ord('A') + i)))
    return column

def temp_len_gen(depth,node):
    return args.ndivisions

tree = Simultaneous('a')

tree.grow_vh_tree_w_lengths(args.depth, temp_form_gen, another_vert_generator, temp_len_gen)

seqary = []
curlen = Fraction(0)
tree.fill_w_seq(seqary, curlen)

for i in xrange(len(seqary)):
    t, l, d = seqary[i]
    seqary[i] = d
    if args.verbose:
        sys.stderr.write(str(d)+'\n')

for s in seqary:
    sys.stdout.write(s+'\n')
