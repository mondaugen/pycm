import dllist
import unittest

class IntDLList(dllist.DLList):
  """
  A sub class of DLLList that has integer values.
  """
  def __init__(self, value=0, before=None, after=None):
    dllist.DLList.__init__(self,before,after)
    self.value = value

def make_list(dll):
  result = []
  item = dll.value
  while True:
    try:
      result.append(item)
      dll = dll.next()
      item = dll.value
    except:
      StopIteration
      break
  return result

class TestDLList(unittest.TestCase):

  def setUp(self):
  
    self.lista = IntDLList(1)
    self.lista.after = IntDLList(2)
    self.lista.after.before = self.lista
    self.lista.after.after = IntDLList(3)
    self.lista.after.after.before = self.lista.after

    self.listb = IntDLList(4)
    self.listb.after = IntDLList(5)
    self.listb.after.before = self.listb
    self.listb.after.after = IntDLList(6)
    self.listb.after.after.before = self.listb.after

  def test_detach_before(self):
    # If called on first element, list remains unchanged
    self.lista.detach_before()
    self.assertEqual(make_list(self.lista), [1,2,3])
    # If called on a middle element, ensure the last element of the left list is
    # the old previous element of the right list
    oldafter = self.lista.after
    self.lista.after.detach_before()
    self.assertEqual(make_list(self.lista),[1])
    self.assertEqual(make_list(oldafter),[2,3])

  def test_detach_after(self):
    # If called on last element, list remains unchanged
    self.lista.after.after.detach_after()
    self.assertEqual(make_list(self.lista), [1,2,3])
    # If called on a middle element, ensure the first element of the right list
    # is the old after element of the left list
    oldafter = self.lista.after.after
    self.lista.after.detach_after()
    self.assertEqual(make_list(self.lista),[1,2])
    self.assertEqual(make_list(oldafter),[3])
    self.assertEqual(self.lista.after.after, None)
    self.assertEqual(oldafter.before, None)

  def test_append_1(self):
    # ensure it does what you want
    result = self.lista.after.after.append(self.listb)
    self.assertEqual(make_list(self.lista),[1,2,3,4,5,6])

  def test_append_2(self):
    oldafter = self.lista.after.after
    result = self.lista.after.append(self.listb)
    self.assertEqual(make_list(self.lista),[1,2,4,5,6])
    # and that the dangling ends are okay too
    self.assertEqual(make_list(oldafter),[3])

  def test_append_3(self):
    oldafter = self.lista.after.after
    oldbefore = self.listb
    result = self.lista.after.append(self.listb.after)
    self.assertEqual(make_list(self.lista),[1,2,5,6])
    self.assertEqual(make_list(oldafter),[3])
    self.assertEqual(make_list(oldbefore),[4])

  def test_prepend_1(self):
    # ensure it does what you want
    result = self.lista.prepend(self.listb.after.after)
    self.assertEqual(make_list(self.listb),[4,5,6,1,2,3])

  def test_prepend_2(self):
    oldafter = self.listb.after.after
    result = self.lista.prepend(self.listb.after)
    self.assertEqual(make_list(self.listb),[4,5,1,2,3])
    self.assertEqual(make_list(oldafter),[6])

  def test_prepend_3(self):
    oldbefore = self.lista
    oldafter = self.listb.after.after
    result = self.lista.after.prepend(self.listb.after)
    self.assertEqual(make_list(self.listb),[4,5,2,3])
    # and that the dangling ends are okay too
    self.assertEqual(make_list(oldbefore),[1])
    self.assertEqual(make_list(oldafter),[6])

  def test_get_last(self):
    self.assertEqual(make_list(self.lista.get_last()),[3])

  def test_get_first(self):
    self.assertEqual(make_list(self.lista.after.after.get_first()),[1,2,3])

  def test_join_1(self):
    oldafter = self.listb.after.after
    self.lista.after.join(self.listb.after)
    self.assertEqual(make_list(self.lista),[1,2,3,4,5,6])
    self.assertEqual(oldafter.get_first().value,1)

  def test_join_2(self):
    self.listb.after.join(self.lista.after)
    self.assertEqual(make_list(self.listb),[4,5,6,1,2,3])

  def test_join_3(self):
    with self.assertRaises(ValueError):
      self.lista.after.join(self.lista.after.after)

  def test_insert_after_1(self):
    oldend = self.listb.after.after
    self.lista.after.after.insert_after(self.listb)
    self.assertEqual(make_list(self.lista),[1,2,3,4,5,6])
    self.assertEqual(oldend.get_first().value,1)

  def test_insert_after_2(self):
    newend = self.lista.after.after
    oldbefore = self.listb
    self.lista.after.insert_after(self.listb.after)
    self.assertEqual(make_list(self.lista),[1,2,5,6,3])
    self.assertEqual(make_list(oldbefore),[4])
    self.assertEqual(newend.get_first().value,1)

  def test_insert_after_3(self):
    oldbegin = self.lista
    oldend   = self.lista.after.after
    self.lista.insert_after(None)
# Ensure that inserting None just breaks the list
    self.assertEqual(make_list(oldbegin),[1])
    self.assertEqual(make_list(oldend.get_first()),[2,3])

  def test_insert_before_1(self):
    newend = self.lista.after.after
    self.lista.insert_before(self.listb)
    self.assertEqual(make_list(self.listb),[4,5,6,1,2,3])
    self.assertEqual(newend.get_first().value,4)

  def test_insert_before_2(self):
    newend = self.lista.after.after
    oldbefore = self.listb
    self.lista.after.insert_before(self.listb.after)
    self.assertEqual(make_list(self.lista),[1,5,6,2,3])
    self.assertEqual(make_list(oldbefore),[4])
    self.assertEqual(newend.get_first().value,1)

  def test_insert_before_3(self):
    oldbegin = self.lista
    oldend   = self.lista.after.after
    self.lista.after.insert_before(None)
# Ensure that inserting None just breaks the list
    self.assertEqual(make_list(oldbegin),[1])
    self.assertEqual(make_list(oldend.get_first()),[2,3])

  def test_pop(self):
    listelem = self.lista.after.pop()
    self.assertEqual(make_list(self.lista),[1,3])
    self.assertEqual(make_list(listelem),[2])

  def test_replace(self):
    self.lista.after.replace(self.listb)
    self.assertEqual(make_list(self.lista),[1,4,5,6,3])

  def test_to_list(self):
    l = self.lista.to_list()
    lvals = [el.value for el in l]
    self.assertEqual(make_list(self.lista),[1,2,3])

if __name__ == '__main__':
  unittest.main()
