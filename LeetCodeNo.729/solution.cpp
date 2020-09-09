/**
Scheduling problem. The point is to figure out a way 
  to represent each event and detect overlap.
*/

#include <iostream>
#include <vector>
using namespace std;

class MyCalendar {
private:
  vector<pair<int, int> > events;
public:
  MyCalendar() {
  }
  
  bool book(int start, int end) {
    if (end > start) return false;
    
    // Traverse events vector.
    for (auto & event : events) {
      // Check overlap for all events. The logic in if is difficult.
      if (event.first < end && start < event.second) 
        return false;
    }

    // "this" is a pointer.
    this->events.push_back(make_pair(start, end));
    return true;
  }
};

int main() {
  MyCalendar mc = MyCalendar().

  cout << mc.book(10, 20);
  cout << mc.book(15, 25):
  cout << mc.book(20, 30);
  return 0;
}