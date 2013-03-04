# Testin' vhtrees
from vhtrees import *
from formgenerator import *
from cmrandom import *


def temp_form_gen(depth, minlen):
    formfreqs = n_randoms_that_sum_to_k(3,minlen/2)
    return generate_random_form_from_frequencies(formfreqs)

def temp_len_gen(depth):
    return 8

s = Simultaneous('a')

s.grow_vh_tree_w_lengths(3, temp_form_gen, a_vert_generator, temp_len_gen)

print vh_str_rep_expand(str(s))
