__doc__ = """
Objects that represent music.
"""

import dllist

class Note(dllist.DLList):
  """
  Represents a pitch and a length of time.
  """
  def __init__(self, length, pitch, before=None, after=None):
    dllist.DLList.__init__(self,before,after)
    self.length = length
    self.pitch = pitch

  def __str__(self):
    return (('(%.2f,%.2f)->' % (self.length,self.pitch))
            + self.after.__str__())

  def to_dict(self):
    """
    Returns the notes paired with keys representing their accumulative time
    position. For example:
    Note(1,60)->Note(0.5,62)->Note(2.5,64)
    is returned as:
    { 0 : Note(1,60), 1 : Note(0.5,62), 1.5 : Note(2.5,64) }

    Take note of the obvious problem that will arise if there are notes of 0
    length...
    """
    notelist = self.to_list()
    notedict = dict()
    curt = 0
    for n in notelist:
      notedict[curt] = n
      curt += n.length
    return notedict

  def to_tuple_list(self):
    """
    Returns a list of tuples of the form: (time, pitch, length). The result is
    sorted by time.
    """
    d = self.to_dict()
    result = []
    for k in d:
      result.append((k,d[k].pitch,d[k].length))
    return list(sorted(result,key=lambda x: x[0]))

  def shallow_copy(self):
    """
    Returns a copy of this Note only, pointing to the exact same previous and
    after notes (the same addresses) as the original. It does not touch the
    previous and after notes, you get something like this:

    n1->n2->n3->n4
        \->n3cp-^

    The copy just points to the old notes.
    """
    return Note(self.length, self.pitch, self.before, self.after)

  def deep_copy(self):
    """
    Returns a copy of this Note and every note that comes after this note. The
    beginning note's previous Note will become None.
    """
    newnotes = []
    for n in self.to_list():
      newnotes.append(n.shallow_copy())
      newnotes[-1].before = None
      newnotes[-1].after = None
    newhead = newnotes[0]
    for n in newnotes[1:]:
      newhead.join(n)
    return newhead

# UNTESTED, but works so far
def suspend(n):
  """
  Suspend a note by tying it to the next one.
  """
  # Don't do it if this is the last note
  if n.after == None:
    return n
  new_time = n.length + n.after.length
  n.after.pop()
  n.length = new_time
  return n
