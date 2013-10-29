import unittest
from cmfunction import LineSegment, PieceWiseFunction, FunctionIterator

def f_1(x): return 2 * x

def f_2(x): return 3 * (x - 1) + 6

class TestCMFunction(unittest.TestCase):

  def setUp(self):
    self.l_1 = LineSegment(1.0, 1.0, 3.0, 2.0)
    self.pwf_1 = PieceWiseFunction()
    self.pwf_1.insert((float("-inf"),f_1))
    self.pwf_1.insert((1,f_2))

  def test_line_seg_1(self):
    y = self.l_1(2.0)
    self.assertEqual(y, 1.5)

  def test_piece_wise_func_1(self):
    result = [self.pwf_1(x) for x in xrange(-2,3)]
    self.assertEqual(result, [-4,-2,0,6,9])

  def test_function_iter_1(self):
    fi = FunctionIterator(self.pwf_1,initialx=-2)
    result = [fi.eval_inc(1) for x in xrange(-2,3)]
    self.assertEqual(result, [-4,-2,0,6,9])

  def test_function_iter_2(self):
    fi = FunctionIterator(self.pwf_1,initialx=-2)
    result = [fi.eval_inc(0.5) for x in xrange(10)]
    self.assertEqual(result, [-4,-3,-2,-1,0,1,6,7.5,9,10.5])


if __name__ == '__main__':
  unittest.main()
