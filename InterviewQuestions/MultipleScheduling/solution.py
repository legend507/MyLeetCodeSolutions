# The initial problem is very similar to LeetCodeNo.729.
# The complete problem has some resemblance to LeetCodeNo.731, but essentially different.

# For 4 core machine.

# Initial problem - 1 core. Reuse code from LeetCodeNo.729.
class MyCalendar(object):
  def __init__(self, label):
    # Array for tuple (start, end).
    self.calendar = []
    self.label = label

  def book(self, start, end):
    # s = 1st element in a tuple, e = 2nd element in a tuple.
    for s, e in self.calendar:
      if s < end and start < e:
          return False
    self.calendar.append((start, end))
    return True

# Complete problem - 4 cores.
class MyCores(object):
  def __init__(self):
    self.cores = [MyCalendar(0), MyCalendar(1), MyCalendar(2), MyCalendar(3)]
  
  def book(self, start, end):
    # Ask 4 cores one by one, until one core returns true.
    for core in self.cores:
      if (core.book(start, end)):
        return True
    return False

