# Copyright 2013 Nicholas Esterer. All rights reserved.

import abc
from fractions import *
import cmgetters
import cmloaders
import cmseqdict
import cmpitchtools
import cminterputils
import cmquantize

class IndexableSequence:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def __len__(self):
	'''
	Length of the sequence. Often the sum of all the sublengths of each
	element contained in the sequence.
	'''
	pass

    @abc.abstractmethod
    def __getitem__(self, key):
	'''
	IndexableSequences may be sparse. How is a value retrieved from a sparse
	sequcence? Is the next lowest defined index chosen? Through
	interpolation?
	'''
	pass

    @abc.abstractmethod
    def load_from_file(self, f):
	'''
	Load in sequence data from a file.
	'''
	pass

    @abc.abstractmethod
    def adjust_indices(self, how):
	'''
	Adjust the indices. Often the data is stored in a reduced form but to
	allow for high resolution look-ups the indices may need to be multiplied
	by a number.
	'''
	pass

class CombiningSequence(IndexableSequence):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def combine(self, args):
	'''
	If the sequence is made up of a few simultaneous sub-sequences, how are
	the values to be combined?
	'''
	pass

class ChordSequence(IndexableSequence):
    '''
    A sequence that stores chords. Chords are stored in a dictionary as
    (Fraction(time,length), [pc1,...,pcn]) key:value pairs.
    '''

    def __init__(self, loading_function=cmloaders.load_length_pcs_pairs,\
	    f=None):
	self.chords = dict()
	self.loading_function = loading_function
	if f == None:
	    return
	self.load_from_file(f)

    def __getitem__(self, key):
	'''
	Gets the chord stated last before key. Could be made faster using a
	binary search.
	'''
	return cmgetters.get_next_lowest_item(self.chords, key)

    def load_from_file(self, f):
	self.chords = self.loading_function(f)

    def adjust_indices(self, i):
	self.chords = cmseqdict.index_multiplier(self.chords, i)

    def __len__(self):
	return sum(self.chords) # sums the keys in the dictionary

class RangeSequence(IndexableSequence):
    '''
    A sequence that stores ranges. Chords are stored in a dictionary as
    (Fraction(time,length), [lower-bound, upper-bound]) key:value pairs.
    '''

    def __init__(self, loading_function=cmloaders.load_length_intlist_pairs,\
	    f=None):
	self.ranges = dict()
	self.loading_function = loading_function
	if f == None:
	    return
	self.load_from_file(f)

    def __getitem__(self, key):
	'''
	Gets the chord stated last before key. Could be made faster using a
	binary search.
	'''
	return cmgetters.get_next_lowest_item(self.ranges, key)

    def load_from_file(self, f):
	self.ranges = self.loading_function(f)

    def adjust_indices(self, i):
	self.ranges = cmseqdict.index_multiplier(self.ranges, i)

    def __len__(self):
	return sum(self.ranges) # sums the keys in the dictionary

class ContourSequence(IndexableSequence):
    '''
    A sequence that stores heights (usually between 0 and 1).
    '''

    def __init__(self, loading_function=cmloaders.load_length_float_pairs,\
	    f=None):
	self.contour = dict()
	self.loading_function = loading_function
	if f == None:
	    return
	self.load_from_file(f)

    def __getitem__(self, key):
	'''
	Gets the contour value linearly interpolated between two points in the
	sequence.
	'''
	return cmgetters.get_linearly_interpolated_item(self.contour, key)

    def load_from_file(self, f):
	self.contour = self.loading_function(f)

    def adjust_indices(self, i):
	self.contour = cmseqdict.index_multiplier(self.contour, i)

    def __len__(self):
	return sum(self.contour)

class RhythmSequence(IndexableSequence):
    '''
    A sequence that stores a sequence of some combination of "note" and "rest".
    This is to have a way to store rhythmic sequences that can be polled to see
    if a note should be sounding or not at a given time. It will also be
    possible to just iterate the elements of the sequence, which can then be
    used to lookup values in other sequences to make complete descriptions of
    notes (with pitch, dynamics etc).
    It is also possible to quantize the notes in the sequence as it sublasses
    Quantizer.
    The total length is the desired resulting length if you were to add all the
    fractional rhythmic values up.
    '''

    def __init__(self, loading_function=cmloaders.load_length_string_pairs,\
	    f=None, totallength=Fraction(1), divisor=0, offset=0):
	self.totallength=totallength
	self.rhythm = dict()
	self.loading_function = loading_function
	self.divisor = divisor
	self.offset = offset
	if f == None:
	    return
	self.load_from_file(f)

    def __getitem__(self, key):
	'''
	Returns the tuple ('note',length) if key is in self.rhythm, otherwise
	returns ('rest',0). Length is calculated by subtracting the next note
	time from the current one (key)
	'''
	key = cmgetters.get_quantized_key(self.rhythm, key, self.divisor,\
		self.offset)
	if key == None:
	    return ('rest', 0)
	tup = cmgetters.get_item_and_length_at_key(self.rhythm, key,\
	    self.totallength)
	if tup == None:
	    return ('rest', 0)
	status, length = tup
	return (status, length)

    def load_from_file(self, f):
	self.rhythm = self.loading_function(f)

    def adjust_indices(self, i):
	self.rhythm = cmseqdict.index_multiplier(self.rhythm, i)

    def __len__(self):
	return sum(self.contour)


class ContourNoteCombSeq(CombiningSequence):
    '''
    Holds a chord sequence, a range sequence and a contour sequence and gives
    notes by combining lookups from all three.
    '''
    def __init__(self, chordsequence, rangesequence, contoursequence):
	self.chordsequence = chordsequence
	self.rangesequence = rangesequence
	self.contoursequence = contoursequence

    def combine(self, args):
	'''
	args is a dictionary of the pairs:
	'chord':<list>
	'contour':<float>
	'range':<list>
	and they are combined to give a midinote number (given that range is
	describing midinotes
	'''
	chord = args['chord']
	lowerbound = args['range'][0]
	upperbound = args['range'][1]
	contour = args['contour']
	return cmpitchtools.get_nearest_pitch(\
		cmpitchtools.map_pcs_to_range(chord, lowerbound, upperbound),\
		cminterputils.linterp_norm(\
		    float(lowerbound),float(upperbound),contour))

    def __len__(self):
	'''
	Without loss of generality we should be able to return the length of any
	sequence.
	'''
	return sum(self.chordsequence)

    def __getitem__(self, key):
	'''
	Look up items in all the sub sequences and bring them together yeah.
	TODO: A better way to do this might be to pass combdict to some method
	in the IndexableSequences like:
	combdict = self.somesequence.fill_dict_entry(combdict, key)
	Then it's only upto combine to have to know what the keys are and how to
	put them together. Further more, we can then have an arbitrary number of
	sequences and it is only up to combine to know how to put them together:
	for s in self.sequences:
	    combdict = s.fill_dict_entry(combdict, key)
	return self.combine(combdict)
	'''
	combdict = dict()
	combdict['chord'] = self.chordsequence[key]
	combdict['contour'] = self.contoursequence[key]
	combdict['range'] = self.rangesequence[key]
	return self.combine(combdict)

    def load_from_file(self, f):
	'''
	I don't know how we're going to load the three from a single file yet.
	'''
	raise NotImplementedError

    def adjust_indices(self, i):
	self.chordsequence.adjust_indices(i)
	self.rangesequence.adjust_indices(i)
	self.contoursequence.adjust_indices(i)

class ContourRhythmNoteCombSeq(CombiningSequence):
    '''
    Holds a chord sequence, a range sequence, a contour sequence and a rhythm and gives
    notes by combining lookups from all four.
    '''
    def __init__(self, rhythmsequence, chordsequence, rangesequence, contoursequence):
	self.rhythmsequence = rhythmsequence
	self.chordsequence = chordsequence
	self.rangesequence = rangesequence
	self.contoursequence = contoursequence

    def combine(self, args):
	'''
	args is a dictionary of the pairs:
	'chord':<list>
	'contour':<float>
	'range':<list>
	and they are combined to give a midinote number (given that range is
	describing midinotes
	'''
	note, length = args['note']
	if note == 'rest':
	    return args['note']
	chord = args['chord']
	lowerbound = args['range'][0]
	upperbound = args['range'][1]
	contour = args['contour']
	return (cmpitchtools.get_nearest_pitch(\
		cmpitchtools.map_pcs_to_range(chord, lowerbound, upperbound),\
		cminterputils.linterp_norm(\
		    float(lowerbound),float(upperbound),contour)),length)

    def __len__(self):
	'''
	Without loss of generality we should be able to return the length of any
	sequence.
	'''
	return sum(self.chordsequence)

    def __getitem__(self, key):
	'''
	Look up items in all the sub sequences and bring them together yeah.
	TODO: A better way to do this might be to pass combdict to some method
	in the IndexableSequences like:
	combdict = self.somesequence.fill_dict_entry(combdict, key)
	Then it's only upto combine to have to know what the keys are and how to
	put them together. Further more, we can then have an arbitrary number of
	sequences and it is only up to combine to know how to put them together:
	for s in self.sequences:
	    combdict = s.fill_dict_entry(combdict, key)
	return self.combine(combdict)
	'''
	combdict = dict()
	combdict['note']  = self.rhythmsequence[key]
	combdict['chord'] = self.chordsequence[key]
	combdict['contour'] = self.contoursequence[key]
	combdict['range'] = self.rangesequence[key]
	return self.combine(combdict)

    def load_from_file(self, f):
	'''
	I don't know how we're going to load the three from a single file yet.
	'''
	raise NotImplementedError

    def adjust_indices(self, i):
	self.rhythmsequence.adjust_indices(i)
	self.chordsequence.adjust_indices(i)
	self.rangesequence.adjust_indices(i)
	self.contoursequence.adjust_indices(i)


