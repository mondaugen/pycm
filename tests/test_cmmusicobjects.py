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
    n = 

if __name__ == '__main__':
  unittest.main()
