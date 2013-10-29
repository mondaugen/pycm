class FormTreeNode:

  def __init__(self,parent = None, children = [], name = None):
    self.parent = parent
    self.children = children
    self.name = name

  def get_section_names(self):
    if self.children == []:
      return [self.name]
    big_list = []
    for c in self.children:
      big_list += c.get_section_names()
    for i in xrange(len(big_list)):
      big_list[i] = self.name + big_list[i]
    return big_list

  def grow_using_dict(self,d):
    """
    Dictionary contains form pairs i.e.:
    { a : ab, b : ccb, c : aba, ... }
    """
    if self.children == []:
      formstring = d[self.name]
      for f in formstring:
        self.children.append(FormTreeNode(parent=self, name=f, children=[]))
    else:
      for c in self.children:
        c.grow_using_dict(d)
