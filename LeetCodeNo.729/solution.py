class MyCalendar(object):
  def __init__(self):
    # Array for tuple (start, end).
    self.calendar = []

  def book(self, start, end):
    # s = 1st element in a tuple, e = 2nd element in a tuple.
    for s, e in self.calendar:
      if s < end and start < e:
          return False
    self.calendar.append((start, end))
    return True