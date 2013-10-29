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

