import unittest
from cmmusicobjects import Note

class TestCMMusicObjects(unittest.TestCase):

  def setUp(self):
    self.note = Note(1,60)
    self.note.join(Note(0.5,69))
    self.note.join(Note(2.5,420))

  def test_to_dict_1(self):
    d = self.note.to_dict()
    self.assertEqual(d, { 0 : self.note, 
      1 : self.note.after, 1.5: self.note.after.after })

  def test_shallow_copy_1(self):
    n = self.note.after.shallow_copy()
    self.assertNotEqual(n, self.note.after)
    self.assertEqual(n.before, self.note.after.before)
    self.assertEqual(n.after, self.note.after.after)

  def test_deep_copy_1(self):
    n = self.note.deep_copy()
    equal = True
    equal &= (n == self.note)
    equal &= (n.after == self.note.after)
    equal &= (n.after.after == self.note.after.after)
    self.assertFalse(equal)
    self.assertEqual(n.get_first().pitch, 60)
    m = self.note.after.deep_copy()
    self.assertEqual(m.get_first().pitch, 69)

if __name__ == '__main__':
  unittest.main()
