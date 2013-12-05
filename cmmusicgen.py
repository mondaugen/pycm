from cmmusicobjects import Note
from cmarpeggio import (PitchOrnamenter, PitchOrnamenterMulti,
    PitchRhythmOrnamenter)

class MultiOrnamenter(object):
  """
  Accept a note (which is the starting note of a list of notes of at least the
  required length), a list of chords, a list of ornament vectors and a list of
  rhythm vectors and return the original note but but ornamented.
  """
  def __init__(self, chords, pitch_orns, rhythm_orns):
    self.ornamenters = []
    for c, p, r in zip(chords, pitch_orns, rhythm_orns):
      self.ornamenters.append(PitchRhythmOrnamenter(c,p,r))

  def ornament(self, notes, keep_first_pitch=False):
    newhead = None
    for n, o in zip(reversed(notes.to_list()[:len(self.ornamenters)]),
        reversed(self.ornamenters)):
      newhead = o.ornament(n,keep_first_pitch)
    return newhead

