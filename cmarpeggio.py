from cmpitchtools import get_nearest_pch
from cmmusicobjects import Note

def chord_arp(jumps, chord, start_pitch):
  norm_chord = [c % 12 for c in chord]
  norm_pitch = start_pitch % 12
  close_pitch = get_nearest_pch(norm_chord, start_pitch)
  true_start_pitch = start_pitch - norm_pitch
  result = []
  index = norm_chord.index(close_pitch)
#  result.append(true_start_pitch + norm_chord[index])
  offset = 0
  for j in jumps:
    result.append(true_start_pitch + norm_chord[index] + offset)
#    offset = (12 * (index + j) / len(norm_chord))
    index = (index + j) % len(norm_chord)
  result.append(true_start_pitch + norm_chord[index])
  return result

class Arp:
  """
  Arpeggiate through notes in a chord, relative to some starting note.
  """

  def __init__(self, chord, start_pitch):
    self.chord = [note % 12 for note in chord]
    # Chord must be sorted
    self.chord.sort()
    self.cur_pitch = get_nearest_pch(self.chord, start_pitch % 12)
    self.ival_vect = []
    for i in xrange(len(self.chord)):
      val = self.chord[(i+1)%len(self.chord)] - self.chord[i]
      while val < 0:
        val = val + 12
      self.ival_vect.append(val)
    self.index = self.chord.index(self.cur_pitch)
    self.cur_pitch += 12 * (start_pitch / 12)

  def next(self):
    self.cur_pitch += self.ival_vect[self.index]
    self.index = (self.index + 1) % len(self.ival_vect)
    return self.cur_pitch

  def prev(self):
    self.index = (self.index - 1) % len(self.ival_vect)
    self.cur_pitch -= self.ival_vect[self.index]
    return self.cur_pitch

  def current(self):
    return self.cur_pitch

  def advance_n(self, n):
    """
    If n is positive call next() n times, outputting last result only. If n is
    negative, call prev() n times, outputting last result only.
    """
    if (n > 0):
      while (n > 1):
        self.next()
        n -= 1
      return self.next()
    elif (n < 0):
      while (n < -1):
        self.prev()
        n += 1
      return self.prev()
    return self.current()

class PitchOrnamenter:
  """
  Ornaments a pitch according to a scale and an ornament vector e.g., given the
  scale [0,2,4,5,7,9,11], the ornament [0,-2,1] and a note with length 4 and
  pitch 62, returns (4,62)->(4,59)->(4,60)->None.

  Warning: If you double pitch classes in the scale you will get strange
  results. Consider this: [60,64,67,72], which has pitchclasses [0,4,7,0]. If you
  arpeggiate 60 with the ornament [0,-2,1], you will get [60,55,60] even though
  what you wanted (probably) was [60,52,55].
  """
  def __init__(self, scale, ornament_vector):
    if len(scale) == 0:
      self.scale = [0]
    else:
      self.scale = scale

    if len(ornament_vector) == 0:
      self.ornament_vector = [0]
    else:
      self.ornament_vector = ornament_vector

  def ornament(self, note):
    arp = Arp(self.scale, note.pitch)
    newhead = Note(note.length, arp.advance_n(self.ornament_vector[0]))
    for i in xrange(1,len(self.ornament_vector)):
      pitch = arp.advance_n(self.ornament_vector[i])
      newhead.join(Note(note.length,pitch))
    note.replace(newhead)
    return newhead

class PitchOrnamenterMulti:
  """
  Given a starting note, a vector (list) of chords, and a vector of intervals,
  create a string of notes that arpeggiates over the chords.
  """
  def __init__(self, scales, ornament_vector):
    if len(scales) == 0:
      self.scales = [[0]]
    if len(scales[0]) == 0:
      self.scales = [[0]]
    else:
      self.scales = scales

    if len(ornament_vector) == 0:
      self.ornament_vector = [[0]]
    else:
      self.ornament_vector = ornament_vector

    if len(self.scales) != len(self.ornament_vector):
      raise Exception("Lengths of scales and ornament_vector must be equal.")

  def ornament(self, note):
    po = PitchOrnamenter(self.scales[0], self.ornament_vector[0])
    head = po.ornament(note)
    tail = head[len(self.ornament_vector[0]) - 1]
    newtail = tail.shallow_copy()
    newtail.sever()
    tail.insert_after(newtail)
    for c, o in zip(self.scales[1:], self.ornament_vector[1:]):
      po = PitchOrnamenter(c,o)
      newtail = po.ornament(newtail)
      tail = newtail[len(o) - 1]
      newtail = tail.shallow_copy()
      newtail.sever()
      tail.insert_after(newtail)
    newtail.pop()
    return head
