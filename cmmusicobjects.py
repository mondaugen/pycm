__doc__ = """
Objects that represent music.
"""

class Note:
  """
  Represents a pitch and a length of time.
  """
  def __init__(self, length, pitch, after=None, previous=None):
    self.length = length
    self.pitch = pitch
    self.after = after
    self.previous = previous

  def append(self, other):
    if other != None:
      other.after = self.after
      other.previous = self
    if self.after != None:
      self.after.previous = other
    self.after = other

  def __str__(self):
    return (('(%.2f,%.2f)->' % (self.length,self.pitch))
            + self.after.__str__())

  def next(self, default=None):
    if self.after == None:
      if default != None:
        return default
      else:
        raise StopIteration
    else:
      return self.after
  
  def __iter__(self):
    return self

  def detach(self):
    if self.after != None:
      self.after.previous = self.previous
    if self.previous != None:
      self.previous.after = self.after
    self.previous = None
    self.after = None
    return self

  def insert_before(self, other):
    if self.previous != None:
      self.previous.after = other
    other.previous = self.previous
    other.after = self
    self.previous = other
