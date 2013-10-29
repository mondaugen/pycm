'''
Accepts a list of strings and a section filler function and returns a dictionary
where each unique string in the string list is associated with a section.
'''

def make_sequence_dict(formstringlist, sectionfiller):
    seqdict = dict()
    for s in set(formstringlist):
	seqdict[s] = sectionfiller.get_list_of_data()
    return seqdict

def augment_form_dict(d, formstring, selection_func, generator_func=None):
  to_do = []
  while formstring != "":
    if formstring in d:
      break
    to_do.append(formstring)
    formstring = formstring[:-1]
  for t in reversed(to_do):
    try:
      s = d[t[:-1]]
    except KeyError:
      if generator_func == None:
        raise Exception( "Key not found and generator function is None" )
      else:
        d[t] = generator_func()
        continue
    d[t] = selection_func(s)


