'''
Accepts a list of strings and a section filler function and returns a dictionary
where each unique string in the string list is associated with a section.
'''

def make_sequence_dict(formstringlist, sectionfiller):
    seqdict = dict()
    for s in set(formstringlist):
	seqdict[s] = sectionfiller.get_list_of_data()
    return seqdict
