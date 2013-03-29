#!/usr/bin/env python
__doc__ = '''
Creates a rhythm of notes or rests
args are: contourmaker.py <depth> <num_sections> <number_of_divisions>
<resolution> <rest_probability>
num_sections must be less than or equal to number of divisions
rest_probability is the probability of a rest occuring (silence)
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
generate a rhythm file which is a list of the pairs\
<fractional time>, ('note'|'rest')\
using a supplied form"

parser = argparse.ArgumentParser(\
	description=__doc__)

__form_file_help__ = 'see source'
#__form_file_help__ = '\
#File to read a form from. The file is merely a list of strings, some of which\
#might be the same so that there are repeated parts in the form. There is a\
#canonical form to the strings which is something like aAbBcCd, which may later\
#be used to control the rendering of sequences according to its name. Currently\
#the name is arbitrary.'

parser.add_argument('--form-file', dest='formfile', nargs='?',\
	const=None, default=None, help=__form_file_help__, type=str)


__resolution_help__ = 'see source'
#__resolution_help__ = '\
#Each item of the form is associated with some time span of music (say, a\
#measure). Resolution is how many chunks this measure has been divided into and\
#therefore dictates the quantization of possible rhythms. So if you assume the\
#time spans will be interpreted as measures and --resolution is set to 8 then\
#the measure could be iterpreted as a 4/4 bar with the fastest notes being 8th\
#notes.'

parser.add_argument('--resolution', dest='resolution', nargs='?',\
	const=1, default=1, help=__resolution_help__, type=int)

__rest_prob_help__ = 'see source'
#__rest_prob_help__ = '\
#A number between 0 and 1 dictating the probability that a note will be a rest.\
#So 0.1 means a 10% chance of being a rest.'

parser.add_argument('--rest-prob', dest='restprob', nargs='?',\
	const=0.0, default=0.0, help=__rest_prob_help__, type=float)

args = parser.parse_args()

def lenfun(aux):
    return Fraction(random.randint(1,args.resolution),args.resolution)

def datumfunc(aux):
    if random.random() < args.restprob:
	return 'rest'
    else:
	return 'note'

if args.formfile == None:
    f = sys.stdin
else:
    f = open(formfile, 'r')

lines = f.readlines()

for i in xrange(len(lines)):
    lines[i] = lines[i].strip()


random.seed()

sf = SectionFiller(lenfun, datumfunc)

seqdict = formfiller.make_sequence_dict(lines, sf)

for s in lines:
    for l, d in seqdict[s]:
	print str(l)+',', d

