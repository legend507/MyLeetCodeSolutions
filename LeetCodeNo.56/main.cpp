
#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <queue>
#include <string>
#include <stack>
#include <unordered_set>
using namespace std;


struct Interval {
	int start;
	int end;
	Interval() : start(0), end(0) {}
	Interval(int s, int e) : start(s), end(e) {}

	static bool compare(Interval& i1, Interval& i2) {
		return (i1.start < i2.start);
	}
};

class Solution {
public:
	vector<Interval> merge(vector<Interval>& intervals) {
		if (intervals.size() <2) return intervals;


		sort(intervals.begin(), intervals.end(), Interval::compare);

		for (int i = 0; i < intervals.size() - 1; i++) {
			Interval i1 = intervals[i];
			Interval i2 = intervals[i + 1];

			// overlaped
			if (i1.end >= i2.start) {
				// erase 
				intervals.erase(intervals.begin() + i, intervals.begin() + i + 1 + 1);

				// merge into a new Interval
				Interval merged(i1.start, max(i1.end, i2.end));
				intervals.insert(intervals.begin() + i, merged);
				i--;
			}

		}

		return intervals;
	}
};

int main()
{


	vector<Interval> nums = { { 1,4 },{ 2,3 } };

	Solution s;

	s.merge(nums);



	system("pause");
	return 0;
}

