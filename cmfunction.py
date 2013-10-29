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

