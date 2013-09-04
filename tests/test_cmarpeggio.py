import unittest
from cmmusicobjects import Note
from cmarpeggio import PitchOrnamenter
from random import shuffle

class TestDLList(unittest.TestCase):

  def setUp(self):
    self.single_note = Note(1,64)
    self.off_note = Note(1,68)
    self.bunch_o_notes = Note(1,70)
    self.bunch_o_notes.insert_after(Note(1,63))
    self.bunch_o_notes.get_last().insert_after(Note(1,66))

  def test_pitch_ornamenter_1(self):
    po = PitchOrnamenter([0,2,4,5,7,9,11],[0,-2,1])
    newhead = po.ornament(self.single_note)
    notes = [n.pitch for n in newhead.to_list()]
    self.assertEqual(notes,[64,60,62])

  def test_pitch_ornamenter_2(self):
    scale = [2,4,6,7,9,11,13]
    shuffle(scale)
    po = PitchOrnamenter(scale,[0,-2,1])
    newhead = po.ornament(self.off_note)
    notes = [n.pitch for n in newhead.to_list()]
    self.assertEqual(notes,[67,64,66])

  def test_pitch_ornamenter_3(self):
    scale = [63,65,66,68,70,72,73]
    shuffle(scale)
    po = PitchOrnamenter(scale,[0,-2,1])
    newhead = None
    for n in reversed(self.bunch_o_notes.to_list()):
      newhead = po.ornament(n)
    notes = [n.pitch for n in newhead.to_list()]
    self.assertEqual(notes,[70,66,68,63,60,61,66,63,65])

  def test_pitch_ornamenter_4(self):
    scale = [63,65,66,68,70,72,73]
    shuffle(scale)
    po = PitchOrnamenter(scale,[-2,1])
    newhead = None
    for n in reversed(self.bunch_o_notes.to_list()):
      newhead = po.ornament(n)
    notes = [n.pitch for n in newhead.to_list()]
    self.assertEqual(notes,[66,68,60,61,63,65])


if __name__ == '__main__':
  unittest.main()
