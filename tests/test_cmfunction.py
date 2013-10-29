import unittest
from cmfunction import LineSegment

class TestCMFunction(unittest.TestCase):

  def setUp(self):
    self.l_1 = LineSegment(1.0, 1.0, 3.0, 2.0)

  def test_line_seg_1(self):
    y = self.l_1(2.0)
    self.assertEqual(y, 1.5)

if __name__ == '__main__':
  unittest.main()
