# Calendar II.
# Follow up on LeetCodeNo.729, but essentially a different problem.


class MyCalendarTwo(object):
  def __init__(self):
    self.calendar = []
    self.overlap = []
  
  def book(self, start, end):
    # If already overlapped, false.
    for s,e in self.overlap:
      if start < e and s < end:
        return False
    # 
    for s,e in self.calendar:
      if start < e and s < end:
        # Append overlapped section.
        self.overlap.append((max(s, start), min(e, end)))
    self.calendar.append((start, end))
    return True

