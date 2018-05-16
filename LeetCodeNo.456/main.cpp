/*
Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.

Note: n will be less than 15,000.

Example 1:
Input: [1, 2, 3, 4]

Output: False

Explanation: There is no 132 pattern in the sequence.
Example 2:
Input: [3, 1, 4, 2]

Output: True

Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
Example 3:
Input: [-1, 3, 2, 0]

Output: True

Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
*/


#include    <iostream>
#include    <queue>
#include	<functional>
#include	<stack>
#include	<string>
#include	<unordered_set>
#include	<sstream>			// istringstream and ostringstream
#include	<set>
#include	<climits>
#include	<algorithm>
#include    <unordered_map>
#include	<vector>
#include	<map>
using namespace std;

class Solution {
public:

	/*
	O(n^2)
	Though better than a brute force solution (which is O(n^3)),
	this one is still not good enough.
	*/
	bool find132pattern(vector<int>& nums) {
		int size = nums.size();

		// input check
		if (size < 3)    return false;

		int minSoFar = INT_MAX;
		for (int i = 0; i < size-1; i++) {
			// 1st, try to find if nums[i] is min so far
			if (minSoFar > nums[i])	minSoFar = nums[i];
			// 2nd, if not min so far, check from i+1, the sequence now is (minSoFar, nums[i], nums[j])
			else {
				for (int j = i + 1; j < size; j++) {
					// nums[i] should be max, nums[j] should be middle, minSoFar is min
					if (minSoFar < nums[i] && minSoFar < nums[j] && nums[i] > nums[j])
						return true;
				}
			}
		}
		return false;
	}

	/*
	Time: O(n), also space
	Best solution,
	The idea is to first fix all minSoFar on each index,
	then traverse from back to start, trying to find the 3 in 132, 
	if not found, put the 3 into stack as a candidate for the 2
	*/
	bool find132pattern2(vector<int>& nums) {
		int size = nums.size();

		// input check
		if (size < 3)    return false;

		vector<int> minSoFar;
		minSoFar.push_back(nums[0]);

		// for every index, record minSoFar
		for (int i = 0; i < size; i++)
			minSoFar.push_back(min(minSoFar[minSoFar.size() - 1], nums[i]));

		// 
		stack<int> candidates;
		for (int j = size - 1; j >= 0; j--) {
			// nums[j] can only == minSoFar[j], when this happens, skip
			if (nums[j] == minSoFar[j])	continue;

			// candidates is for the 2 in 132, so pop out all candidates that is < 1
			while (!candidates.empty() && candidates.top() <= minSoFar[j])
				candidates.pop();

			// sequence is (minSoFar, nums[j], candidates.top())
			if (!candidates.empty() && candidates.top() < nums[j] && candidates.top() > minSoFar[j]) 
				return true;


			candidates.push(nums[j]);

		}
		return false;
	}

};

int main() {
	vector<int> nums = { 6, 12, 3, 4, 6, 11, 20 };

	Solution s;
	s.find132pattern2(nums);

	return 0;
}