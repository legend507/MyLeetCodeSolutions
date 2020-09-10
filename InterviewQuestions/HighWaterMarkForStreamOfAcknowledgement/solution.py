
class JobServer(object):
  def __init__(self, n):
    self._HWM = n
    self._acked = set([])
  
  def start(self, n):
    self._HWM = n

  def ack(self, n):
    if (n <= self._HWM):
      return 0

    leap = 0

    self._acked.add(n)

    while True:
      # Search for _HWM+1 in the set.
      if (self._HWM + 1) not in self._acked:
        break
      else:
        # If _HWM+1 exists, move _HWM by 1 step.
        self._acked.remove(self._HWM + 1)

        leap = leap + 1
        self._HWM = self._HWM + 1

    return leap