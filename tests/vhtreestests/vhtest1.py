# Testin' vhtrees
from vhtrees import *
from formgenerator import *



def temp_form_gen(depth):
    return generate_random_form_from_frequencies([3,2,2,1])

s = Simultaneous('a')

s.grow_vh_tree(3, temp_form_gen, a_vert_generator)

print vh_str_rep_expand(str(s))
