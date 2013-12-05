# Assuming that the input is a list of sequence types with the first index
# representing the absolute time, sort the times in ascending order and then
# output (delta,event) pairs. Asssuming the input is a list, then an events that
# looks like this: [[1,62,1],[4.5, 60, 1],[7,65,2]], end up like this:
# [(1,[62,1]),(3.5,[60,1]),(2.5,[65,2])], got it?
def abs_time_to_delta_time(seq):
  seq = sorted(seq,key=lambda x: x[0])
  lasttime = 0
  result = []
  for event in seq:
    result.append((event[0] - lasttime, event[1:]))
    lasttime = event[0]
  return result
