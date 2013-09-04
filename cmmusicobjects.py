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
