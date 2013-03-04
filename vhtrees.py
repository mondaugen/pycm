# Copyright 2013 Nicholas Esterer. All Rights Reserved.
'''Vertical and horizontal tree elements'''

from rhythmgenerator import *
from fractions import *

def a_vert_generator(depth):
    column = []
    for i in xrange(2):
	column.append(Sequential(chr(ord('A') + i)))
    return column

def default_depth_adjust(depth,curnode):
    return depth

def vh_str_rep_expand(s):
    '''Expand the string s representing the tree from over one line to several
    lines.'''
    # Convert to list
    s = list(s)
    news = []
    bracketdepth = 0
    for c in s:
	if c in "{[":
	    bracketdepth = bracketdepth + 1
	    news.append(c)
	    news.append('\n')
	    for i in xrange(bracketdepth):
		news.append('  ')
	elif c in "}]":
	    bracketdepth = bracketdepth - 1
	    news.append('\n')
	    for i in xrange(bracketdepth):
		news.append('  ')
	    news.append(c)
	    news.append('\n')
	    for i in xrange(bracketdepth):
		news.append('  ')
	else:
	    news.append(c)
    return ''.join(news)

class Simultaneous:
    '''Holds an array of Sequentials'''
    name = None
    members = []
    length = 1
    parent = None

    def __init__(self, name, length=1, parent=None):
	self.name = name
	self.length = length
	self.parent = parent

    def __str__(self):
	result = '\\'+self.name+'<'+str(self.length)+'>{'
	if len(self.members) == 0:
	    result = result + 'M'
	else:
	    for m in self.members:
		result = result + str(m)
	result = result + '}'
	return result

    def get_deep_length(self):
	if self.parent == None:
	    return (self.name, Fraction(self.length))
	else:
	    pname, plength = self.parent.get_deep_length()
	    return (pname+self.name,\
		    Fraction(self.length) * Fraction(plength))

    def get_all_deep_leaf_lengths(self, ptr):
	if len(self.members) == 0:
	    ptr.append(self.get_deep_length())
	else:
	    for m in self.members:
		m.get_all_deep_leaf_lengths(ptr)

    def grow_vh_tree(self, depth, form_gen, vert_gen):
	if depth > 1:
	    self.members = vert_gen(depth) # Generates list of sequences
	    for c in self.members:
		c.form = form_gen(depth) # Generates list of formal names
		c.parent = self
		for f in set(c.form):
		    subs = Simultaneous(f,parent=c)
		    subs.grow_vh_tree(depth-1, form_gen, vert_gen)
		    c.members[f] = subs
	else:
	    self.members = []

    def grow_vh_tree_w_lengths(self, depth, form_gen, vert_gen, len_gen,\
	    depth_adjust=default_depth_adjust):
	if depth > 1:
	    self.members = vert_gen(depth,self) # Generates list of sequences
	    # Multiply the length so we can fit some subsequences therein
	    self.length = self.length# * len_gen(depth)
	    for c in self.members:
		# Generate list of formal names, the sum of the frequencies of
		# the formal names must be less than or equal to newlen
		newlen = len_gen(depth,self)
		c.form = form_gen(depth, newlen,self)
		c.parent = self
		lendict = stretch_form_randomly(c.form, newlen)
		for f in set(c.form):
		    subs = Simultaneous(f, lendict[f], c)
		    tmpdepth = depth_adjust(depth,subs)
		    subs.grow_vh_tree_w_lengths(tmpdepth-1, form_gen, vert_gen,\
			    len_gen, depth_adjust)
		    c.members[f] = subs
	else:
	    self.members = []

    def grow_vh_tree_w_lengths_2(self, depth, form_gen, vert_gen, len_gen):
	''' len_gen returns a tuple (minlen,maxlen) for the possible range of
	    lengths for the new subsequences. it accepts depth as an argument.
	    form_gen returns a form and accepts depth as an argument
	    '''
	if depth > 1:
	    self.members = vert_gen(depth) # Generates list of sequences
	    # Multiply the length so we can fit some subsequences therein
	    self.length = self.length# * len_gen(depth)
	    for c in self.members:
		# Generate list of formal names, the sum of the frequencies of
		# the formal names must be geater or equal to self.length
		newminlen, newmaxlen = len_gen(depth)
		c.form = form_gen(depth)
		c.parent = self
		lendict = give_form_lengths(c.form, newminlen, newmaxlen)
		for f in set(c.form):
		    subs = Simultaneous(f, lendict[f], c)
		    subs.grow_vh_tree_w_lengths_2(depth-1, form_gen, vert_gen,\
			    len_gen)
		    c.members[f] = subs
	else:
	    self.members = []
    
    def fill_w_seq(self, seq, curlen):
	if len(self.members) < 1:
	    deeplen = self.get_deep_length()
	    name, slen = deeplen	    
	    seq.append((curlen,slen,name))
	    name, slen = deeplen
	    return curlen + slen
	else:
	    tmplen = curlen
	    for m in self.members:
		curlen = tmplen
		curlen = m.fill_w_seq(seq, curlen)
	return curlen
    
    def fill_w_seq(self, seq, curlen):
	if len(self.members) < 1:
	    deeplen = self.get_deep_length()
	    name, slen = deeplen	    
	    seq.append((curlen,slen,name))
	    name, slen = deeplen
	    return curlen + slen
	else:
	    tmplen = curlen
	    for m in self.members:
		curlen = tmplen
		curlen = m.fill_w_seq(seq, curlen)
	return curlen

class Sequential:
    '''Holds an array of Simultaneouses'''
    name = None
    members = None
    form = []
    parent = None

    def __init__(self, name, parent=None):
	self.name = name
	self.members = dict()
	self.parent = parent

    def __str__(self):
	result = '\\'+self.name+'['
	if len(self.members) == 0:
	    result = result + 'M'
	else:
	    for f in self.form:
		result = result + str(self.members[f])
	result = result + ']'
	return result

    def get_shallow_length(self):
	totlen = 0;
	for f in self.form:
	    totlen += self.members[f].length
	return totlen

    def get_deep_length(self):
	if self.parent == None:
	    return (self.name,Fraction(1,self.get_shallow_length()))
	else:
	    pname, plength = self.parent.get_deep_length()
	    return (pname+self.name,\
		    Fraction(plength,self.get_shallow_length()))

    def get_all_deep_leaf_lengths(self, ptr):
	if len(self.members) == None:
	    ptr.append(self.get_deep_length())
	else:
	    for f in self.form:
		self.members[f].get_all_deep_leaf_lengths(ptr)
   
    def fill_w_seq(self, seq, curlen):
	if len(self.members) < 1:
	    return curlen
	for f in self.form:
	    curlen = self.members[f].fill_w_seq(seq, curlen)
	return curlen









