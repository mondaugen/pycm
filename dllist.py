class DLList:
  """
  A doubly linked list.
  """

  def __init__(self, before=None, after=None):
    self.before = before
    self.after = after

  def detach_before(self):
    """
    Deletes connection between self and the element before it. If the element
    before it is not None then its "after" is made to point to None.
    """
    if self.before != None:
      self.before.after = None
    self.before = None

  def detach_after(self):
    """
    Deletes connection between self and the element after it. If the element
    after it is not None then its "before" is made to point to None.
    """
    if self.after != None:
      self.after.before = None
    self.after = None

  def append(self, other):
    """
    Append other to self (put other directly after self).
    """
    self.detach_after()
    self.after = other
    if other != None:
      other.detach_before()
      other.before = self

  def prepend(self, other):
    """
    Prepend other to self (put other directly before self).
    """
    self.detach_before()
    self.before = other
    if other != None:
      other.detach_after()
      other.after = self

  def get_last(self):
    d = self
    while d.after != None:
      d = d.after
    return d

  def get_first(self):
    d = self
    while d.before != None:
      d = d.before
    return d

  def join(self, other):
    """
    Joins two lists together at their ends. This means that the last element of
    self is found and the first element of other is found and then these are
    joined.
    """
    if self != None:
      # this could be optimized with inline if (does it even matter?)
      if other == None:
        self.get_last().after = other
      else
        self.get_last().after = other.get_first()
    if other != None:
      if self == None:
        other.get_first().before = self
      else:
        other.get_first().before = self.get_last()

  def insert_after(self, other):
    """
    Inserts other in its entirety directly after self and then joins the end of
    other with what originally came after self.
    """
    oldafter = self.after
    self.after = None
    # if other is not the head of a list, it will get broken
    if other != None:
      other.detach()
    self.join(self, other)
    other.join(oldafter)

  def insert_before(self, other):
    """
    Inserts other before self in its entirety. What was originally before self
    is joined to the head of other.
    """
    oldbefore = self.previous
    self.previous = None
    # if other is not the head of a list, it will get broken
    if other != None:
      other.detach()
    other.join(self)
    oldbefore.join(other)

