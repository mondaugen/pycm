import unittest
from cmmusicobjects import Note
from cmmusicgen import MultiOrnamenter

class TestCMMusicGen(unittest.TestCase):

  def setUp(self):
    self.mo = MultiOrnamenter([[0,4,7],[2,5,9]],
                              [[0,2,-1],[0,-2,1]],
                              [[0.25,0.25,0.5],[0.5,0.25,0.25]])

  def test_multi_ornamenter_1(self):
    note = Note(2,60)
    note.join(Note(1,62))
    note = self.mo.ornament(note)
    notes = [(n.pitch,n.length) for n in note.to_list()]
    self.assertEqual(notes,
        [(60,0.5),(67,0.5),(64,1.0),(62,0.5),(53,0.25),(57,0.25)])

if __name__ == '__main__':
  unittest.main()
