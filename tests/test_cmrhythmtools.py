import unittest
from cmrhythmtools import abs_time_to_delta_time

class TestCMRhythmTools(unittest.TestCase):

  def setUp(self):
    self.someevents = [[1,62,1],(4.5, 60, 1),[7,65,2,6,9]]

  def test_abs_time_to_delta_time_1(self):
    result = abs_time_to_delta_time(self.someevents)
    self.assertEqual(result, [(1,[62,1]),(3.5,(60,1)),
      (2.5,[65,2,6,9])])

if __name__ == '__main__':
  unittest.main()

