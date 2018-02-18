#include    <iostream>
#include    <vector>
#include	<deque>
using namespace std;



class Solution {
public:
	vector<int> maxSlidingWindow(vector<int>& nums, int k) {

		if (1 == k || nums.empty()) {
			return nums;
		}

		// after input check, declare vars
		vector<int> ret;
		deque<int>	largestIndex;

		//	[x, x, x, x, x, ..., x, x, x]
		//	[		  ^], if i is in ^, only see elements that is before i
		for (int i = 0; i < nums.size(); i++) {

			// as i increment, pop out the element that no longer exists in the window
			//	solve i - x + 1 = k + 1 (becuase I only want k elements in a window) for x, x = i - k
			if (!largestIndex.empty() && largestIndex.front() == i - k) {
				largestIndex.pop_front();
			}

			// traverse from back, stop until found an index s.t. nums[largestIndex.back()] < nums[i] or deque empty
			while (!largestIndex.empty() && nums[largestIndex.back()] < nums[i]) {
				largestIndex.pop_back();
			}
			largestIndex.push_back(i);

			// reach the last element of the 1st window
			if (i >= k - 1) {
				ret.push_back(nums[largestIndex.front()]);
			}

		}

		return ret;
	}
};

int main() {

	vector<int> input = { 1,3,-1,-3,5,3,6,7 };
	//vector<int> input = { 7,2,4 };

	Solution s;

	vector<int> ret;



	ret = s.maxSlidingWindow(input, 3);

	for (auto ele : ret)
		cout << ele << endl;

	system("pause");
	return 0;
}
