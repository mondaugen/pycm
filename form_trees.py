import random
from fractions import Fraction
import ConfigParser

class FormTreeNode:

    def __init__(self, parent, name, children=[], proportion=Fraction(1,1)):
	self.parent = parent
	self.name = name
	self.children = children
	self.proportion = proportion

    def print_node_string(self):
	if self.parent == []:
	    return self.name
	else:
	    return self.name + self.parent.print_node_string()

    def print_leaves(self, string_list):
	if self.children == []:
	    string_list.append(self.print_node_string())
	else:
	    for c in self.children:
		c.print_leaves(string_list)
    
    def get_fraction(self):
	if self.parent == []:
	    return self.proportion
	else:
	    return self.proportion * self.parent.get_fraction()
    
    def print_leaves_and_fractions(self, tuple_list):
	if self.children == []:
	    tuple_list.append(( self.print_node_string(), float(self.get_fraction()) ))
	else:
	    for c in self.children:
		c.print_leaves_and_fractions(tuple_list)


def form_tree_generator(depth, section_names, number_of_divisions):
    random.seed()
    result = FormTreeNode([], section_names[0], [])
    next_roots = {}
    if (depth - 1) > 0:
	for s in set(section_names): #remove duplicates
	    r = form_tree_generator(depth-1, section_names, number_of_divisions)
	    r.parent = result
	    r.name = s
	    next_roots[s] = r
        for i in xrange(number_of_divisions):
		look_up = random.choice(section_names)
		result.children.append(next_roots[look_up])
    return result

def known_form_tree_builder(depth, form):
    '''grows a tree recursively in a predictable way. An acceptable depth is any
    integer greater than 0. An acceptable form is something like
    ['a','b','a','c','a'], where every subtree will have the same form.'''
    result = FormTreeNode([], form[0], [])
    next_roots = {}
    if (depth - 1) > 0:
	for s in set(form): #remove duplicates
	    r = known_form_tree_builder(depth-1, form)
	    r.parent = result
	    r.name = s
	    next_roots[s] = r
	for f in form:
	    result.children.append(next_roots[f])
    return result

def rough_form_tree_generator(section_names, number_of_divisions, continue_prob = 0.5, continue_coeff = 0.5):
    random.seed()
    result = FormTreeNode( [], section_names[0], [] )
    next_roots = []    
    if random.random() < continue_prob:
	for s in section_names:
	    r = rough_form_tree_generator(section_names, number_of_divisions, continue_prob*continue_coeff, continue_coeff)
	    r.parent = result
	    r.name = s
	    next_roots.append(r)
        for i in xrange(number_of_divisions):
		result.children.append(random.choice(next_roots))
    return result

def rand_width_tree_generator(section_names, continue_prob = 1, continue_coeff = 0.6, division_range=[2,4,8], proportion=Fraction(1,1)):
    random.seed()
    result = FormTreeNode( [], section_names[0], [], proportion )
    next_roots = []
    division_num = random.choice(division_range)
    if random.random() < continue_prob:
	for s in section_names:
	    r = rand_width_tree_generator(section_names, continue_prob*continue_coeff, continue_coeff, division_range, Fraction(1,division_num))
	    r.parent = result
	    r.name = s
	    next_roots.append(r)
        for i in xrange(division_num):
		result.children.append(random.choice(next_roots))
    return result

def ctl_depth_tree_generator(depth, end_depths, section_names, continue_prob = 1, continue_coeff = 0.6, division_range=[2,4,8], proportion=Fraction(1,1)):
    random.seed()
    result = FormTreeNode( [], section_names[0], [], proportion )
    next_roots = []
    division_num = random.choice(division_range)
    if depth > end_depths:
	for s in section_names:
	    r = ctl_depth_tree_generator(depth-1, end_depths, section_names, continue_prob*continue_coeff, continue_coeff, division_range, Fraction(1,division_num))
	    r.parent = result
	    r.name = s
	    next_roots.append(r)
        for i in xrange(division_num):
		result.children.append(random.choice(next_roots))
    else:
	for s in section_names:
	    r = rand_width_tree_generator(section_names, continue_prob*continue_coeff, continue_coeff, division_range, Fraction(1,division_num))
	    r.parent = result
	    r.name = s
	    next_roots.append(r)
        for i in xrange(division_num):
		result.children.append(random.choice(next_roots))

    return result

def form_trees_from_file(cfgfilepth):
    '''Returns a dictionary of form trees made from the configurations listed in
    the configuration file.'''
    cfg = ConfigParser.RawConfigParser()
    cfg.read(cfgfilepth)
    tns = {} #the trees go here
    for s in cfg.sections():
	names = cfg.get(s, 'names').split(',')
	formsects = cfg.get(s, 'sections').split(',')
	width = cfg.getint(s, 'width')
	depth = cfg.getint(s, 'depth')
	growth = cfg.get(s, 'growth')
	issignature = False
	try:
	    signature = cfg.get(s, 'signature').split(',')
	    issignature = True
	except ConfigParser.NoOptionError:
	    print 'Form Trees: No signature specified. Using random growth.'
	    growth = 'random'
	    issignature = False
	    signature = []
	if (len(signature) != width) & issignature:
	    print 'Form Trees: Signature length does not equal width. \
		    Using random growth'
	    growth = 'random'
	if growth == 'specified':
	    tree = known_form_tree_builder(depth, signature)
	else:
	    tree = form_tree_generator(depth, formsects, width)
	for n in names:
	    tns[n] = tree
    return tns

def form_strings_from_file(cfgfilepth):
    '''Does what form_trees_from_file does but returns a dictionary of form
    strings, rather than trees'''
    tns = form_trees_from_file(cfgfilepth)
    strs = {} #dictionary that holds the string lists
    for k in tns.keys():
	slist = []
	tns[k].print_leaves(slist)
	strs[k] = slist
    return strs

def test_script(depth = 4, section_names = ['a','b','c'], number_of_divisions=8):
    node = form_tree_generator(depth, section_names, number_of_divisions)
    s_list = []
    node.print_leaves(s_list)
    return s_list

def test_script_2(depth = 2, section_names = ['a','b'], number_of_divisions=4, num_trys=10):
    sets = []
    for i in xrange(num_trys):
	node = form_tree_generator(depth, section_names, number_of_divisions)
	s_list = []
	node.print_leaves(s_list)
	sets.append( set(s_list) )
    return sets

def test_script_3(section_names = ['a','b','c'], number_of_divisions=4, continue_prob=0.5, continue_coeff=0.5):
    node = rough_form_tree_generator(section_names, number_of_divisions, continue_prob, continue_coeff)
    s_list = []
    node.print_leaves(s_list)
    return s_list

def test_script_4(depth=6, end_depths=2, section_names=['a','b','c'], continue_prob = 1, continue_coeff = 0.5, division_range=[2,4]):
    node = ctl_depth_tree_generator(depth, end_depths, section_names, continue_prob, continue_coeff, division_range, proportion=Fraction(1,1))
    t_list = []
    node.print_leaves_and_fractions(t_list)
    return t_list
