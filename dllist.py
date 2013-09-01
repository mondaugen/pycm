class DLList:
  """
  A doubly linked list.
  """

  def __init__(self, before=None, after=None):
    self.before = before
    self.after = after

  def __str__(self):
    print "List:"
    print "Before:"
    print repr(self.before)
    print "After:"
    print repr(self.after)

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
    self_first = self.get_first()
    self_last = self.get_last()
    if other == None:
# self_last.after should already be None
      return
    other_first = other.get_first()
    if (self_first
        == other_first):
#     This could be removed to make this more efficient and just warn people
#     against doing it
      raise ValueError("Can't join a list to itself, sorry (it sounds fun I"
                          + " know).")
    self_last.after = other_first
    other_first.before = self_last

  def insert_after(self, other):
    """
    Inserts other in its entirety directly after self and then joins the end of
    other with what originally came after self.
    """
    oldafter = self.after
    self.detach_after()
    # if other is not the head of a list, it will get broken
    if other != None:
      other.detach_before()
    else:
      # Inserting None just breaks the list
      return
    self.join(other)
    other.join(oldafter)

  def insert_before(self, other):
    """
    Inserts other before self in its entirety. What was originally before self
    is joined to the head of other.
    """
    oldbefore = self.before
    self.detach_before()
    # if other is not the head of a list, it will get broken
    if other != None:
      other.detach_before()
      other.join(self)
    else:
      # Inserting None just breaks the list
      return
    if oldbefore != None:
      oldbefore.join(other)

  def next(self,default=None):
    if self.after == None:
      if default != None:
        return default
      else:
        raise StopIteration
    else:
      return self.after

  def __iter__(self):
    return self

