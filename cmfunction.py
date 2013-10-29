from bisect import bisect_right, bisect_left

def find_le(a, x):
  'Find rightmost value less than or equal to x'
  i = bisect_right(a, x)
  if i:
    return a[i-1]
  raise ValueError

def dict_find_le(a ,x):
  'Convenient when a is a dictionary and you just compare keys.'
  i = find_le(sorted(a.keys()), x)
  return a[i]

def index(a, x):
  'Locate the leftmost value exactly equal to x'
  i = bisect_left(a, x)
  if i != len(a) and a[i] == x:
      return i
  raise ValueError

class LineSegment:
  """
  Builds a functor representing a line segment.
  """

  def __init(self, slope, yintercept):
    self.slope = slope
    self.yintercept = yintercept

  def __init__(self,x0,y0,x1,y1):
    self.__init((y1 - y0) / (x1 - x0), y0 - x0 * (y1 - y0) / (x1 - x0))

  def __call__(self, x):
    return self.slope * x + self.yintercept

class PieceWiseFunction:
  """
  Functions are stored as a range value that x is less than or equal to and a
  corresponding function. For example, if you want to have the function be y =
  2*x for all x, you would do this:

  # Define your function somewhere:
  def my_func(x): return 2*x

  # Add your function to a piecewise function
  pwf = PieceWiseFunction()
  pwf.insert((float(-inf), my_func))

  If you want to have more functions defined for specific ranges, then just
  define them and add them in, for example:

  # We now want y = -2 * x + 7
  def my_other_func(x): return -2 * x + 7

  # We want this only when x >= 6.9
  pwf.insert((6.9, my_other_func))

  You can do this for as many functions as you want/can-handle.
  """

  def __init__(self):
    self.functions = dict()

  def insert(self,rangefuncpair):
    r, f = rangefuncpair
    self.functions[r] = f
    return

  def __call__(self,x):
    return dict_find_le(self.functions,x)(x)

class FunctionIterator:
  """
  Holds a state and a function and gives methods for advancing an x value
  incrementally and returning a function evaluated at a point.
  """

  def __init__(self,function,initialx=0):
    self.function = function
    self.curx = initialx

  def eval_inc(self,dx):
    """
    Evaluate the function, storing the result, then increment the current x
    value by dx and then return the result.
    """
    result = self.function(self.curx)
    self.curx += dx
    return result

