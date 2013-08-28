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
    # Chord must be sorted
    chord.sort()
    self.chord = [note % 12 for note in chord]
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
  scale [0,2,3,4,5,7,9,11], the ornament [0,-2,1] and a note with length 4 and
  pitch 62, returns (4,62)->(4,59)->(4,60)->None.
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
    tail = note.previous
    after = note.after
    note.detach()
    newhead = Note(note.length, arp.advance_n(self.ornament_vector[0]))
    if tail != None:
      tail.append(newhead)
    tail = newhead
    for i in xrange(1,len(self.ornament_vector)):
      pitch = arp.advance_n(self.ornament_vector[i])
      tail.append(Note(note.length,pitch))
      tail = tail.next()
    tail.append(after)
    return newhead

