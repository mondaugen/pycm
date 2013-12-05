import unittest
from cmmusicobjects import Note
from cmarpeggio import (PitchOrnamenter, PitchOrnamenterMulti,
    PitchRhythmOrnamenter)
from random import shuffle

class TestCMArpeggio(unittest.TestCase):

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

  def test_pitch_ornamenter_5(self):
    scale = [2,4,6,7,9,11,13]
    shuffle(scale)
    po = PitchOrnamenter(scale,[0,-2,1])
    newhead = po.ornament(self.off_note,True)
    notes = [n.pitch for n in newhead.to_list()]
    self.assertEqual(notes,[68,64,66])

  def test_pitch_ornamenter_multi_1(self):
    chords = [[2,4,10],[1,7,10],[2,7,11],[2,3,6]]
    orn_vec = [[x] for x in [0,-2,1,0]]
    snote = Note(1,69)
    pom = PitchOrnamenterMulti(chords, orn_vec)
    snote = pom.ornament(snote)
    notes = [n.pitch for n in snote.get_first().to_list()]
    self.assertEqual(notes,[70,61,67,66])

  def test_pitch_ornamenter_multi_2(self):
    chords = [[2,4,10],[1,7,10],[2,7,11],[2,3,6]]
    orn_vec = [[0],[0,-2],[1],[0]]
    snote = Note(1,69)
    pom = PitchOrnamenterMulti(chords, orn_vec)
    snote = pom.ornament(snote)
    notes = [n.pitch for n in snote.get_first().to_list()]
    self.assertEqual(notes,[70,70,61,67,66])

  def test_pitch_ornamenter_multi_3(self):
    chords = [[2,4,10],[1,7,10],[2,7,11],[2,3,6]]
    orn_vec = [[0],[-1,-1],[1],[0]]
    snote = Note(1,69)
    pom = PitchOrnamenterMulti(chords, orn_vec)
    snote = pom.ornament(snote)
    notes = [n.pitch for n in snote.get_first().to_list()]
    self.assertEqual(notes,[70,67,61,67,66])

  def test_pitch_ornamenter_multi_4(self):
    chords = [[2,4,10],[1,7,10],[2,7,11],[2,3,6]]
    orn_vec = [[0],[-1,-1],[1],[0]]
    snote = Note(1,56)
    snote.join(Note(1,69))
    snote.join(Note(1,79))
    pom = PitchOrnamenterMulti(chords, orn_vec)
    snote = pom.ornament(snote.after)
    notes = [n.pitch for n in snote.get_first().to_list()]
    self.assertEqual(notes,[56,70,67,61,67,66,79])

  def test_pitch_rhythm_ornamenter_1(self):
    scale = [63,65,66,68,70,72,73]
    rhythm = [0.25,0.75]
    shuffle(scale)
    po = PitchRhythmOrnamenter(scale,[-2,1],rhythm)
    newhead = None
    for n in reversed(self.bunch_o_notes.to_list()):
      newhead = po.ornament(n)
    notes = [(n.pitch,n.length) for n in newhead.to_list()]
    self.assertEqual(notes,[(66,0.25),(68,0.75),(60,0.25),(61,0.75),
      (63,0.25),(65,0.75)])

if __name__ == '__main__':
  unittest.main()
