#include <iostream>
#include <vector>
using namespace std;

class MyCalendarTwo {
private:
  // Store all events as-is.
  vector<pair<int, int> > events;

  // Store ONLY the overlapped period.
  vector<pair<int, int> > overlaps;
public:
  MyCalendarTwo() {
  }
  
  bool book(int start, int end) {
    if (end < start) return false;

    // Check overlap vector.
    for (auto & overlap : overlaps) {
      if (overlap.first < end && start < overlap.second)
        return false;
    }

    // Decide what to put into overlap vector.
    for (auto & event : events) {
      if (event.first < end && start < event.second)
        this->overlaps.push_back(make_pair(
          max(event.first, start), min(event.second, end)));
    }

    this->events.push_back(make_pair(start, end));
    return true;
  }
};

int main() {
  MyCalendarTwo mc = MyCalendarTwo();

  cout << mc.book(10, 20);
  cout << mc.book(15, 25);
  cout << mc.book(20, 30);
  return 0;
}