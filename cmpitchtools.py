'''
Tools for manipulating pitches.
'''
import cmmath
import sys
import random

chromatic = [0,1,2,3,4,5,6,7,8,9,10,11]

def map_pcs_to_range(pcs, lowerbound, upperbound):
  '''Takes a set of pitches as pitchclasses and returns a list of all the
  occurrences of the pitches within the range. Ie pcs = [1,7], lowerbound =
  55, upperbound = 70 gives: 55, 61, 67'''
  pchs = []
  for pc in pcs:
    #subtract lowerbound from pc and find pc
    pc = (pc - lowerbound)%12
    #then add lowerbound to pc
    pc = pc + lowerbound
    while(pc <= upperbound): #range is inclusive
      pchs.append(pc)
      pc = pc + 12
  sys.stderr.write(str(sorted(pchs))+'\n')
  return sorted(pchs)

def get_nearest_pch(pchs, pch):
  '''Finds the nearest pch to pch in pchs'''
  normpch = pch % 12
  normpchs = [pch % 12 for pch in pchs]
  index = -1
  mindist = sys.maxint
  for i in xrange(len(pchs)):
    dist = min(abs((normpchs[i] - normpch) % 12), \
        abs((normpch - normpchs[i]) % 12))
    if dist < mindist:
      mindist = dist
      index = i
  return pchs[index]

def make_chord_by_intervals_chrom(ivals, numchoice):
  '''
  Try to make a chord from numchoice selections from pitches, jumping by a
  random choice of ivals each ivals each selection and returning a list of
  lesser length if no value of that jump amount may be found
  ivals is list
  numchoice is single value
  pitches is list
  '''
  pitches = [0,1,2,3,4,5,6,7,8,9,10,11]
  if len(pitches) < numchoice:
    numchoice = len(pitches)
  result = []
  if numchoice == 0:
    return result
  lastchoice = pitches.pop(random.randint(0,len(pitches)-1))
  result.append(lastchoice)
  for n in xrange(numchoice-1):
    valfound = False
    random.shuffle(ivals)
    for i in ivals:
      try:
        lastchoice = pitches.pop(pitches.index((lastchoice + i)%12))
        result.append(lastchoice)
        valfound = True
        break
      except ValueError:
        continue
    if not valfound:
      return sorted(result)
  return sorted(result)
