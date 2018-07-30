/*
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3.
Output: 5
Explanation:

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
Note:
The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.
*/
#include <iostream>
#include <list>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

class Solution {
public:
	// brute force, try every combination
	//	Passed, but not a very good solution
	//	O(2^n)
	int findTargetSumWays(vector<int>& nums, int S) {
		vector<int> allResult;

		doRecurse(nums, 0, 0, allResult, S);

		return allResult.size();
	}
	void doRecurse(vector<int>& nums, int idx, int oneResult, vector<int>& allResult, int S) {
		// base case
		if (idx == nums.size()) {
			if (oneResult == S)	allResult.push_back(oneResult);
			return;
		}

		// recurse case
		doRecurse(nums, idx + 1, oneResult + nums[idx], allResult, S);
		doRecurse(nums, idx + 1, oneResult - nums[idx], allResult, S);
	}

	// DP, there is a better solution that I failed to understand
	int findTargetSumWays2(vector<int>& nums, int S) {
		int sum = 0;

		/*
		sum(pos) - sum(neg) = S
		2sum(pos) = S + sum(all)
		*/
		for (auto oneEle : nums) sum += oneEle;
		sum += S;
		// (sum of nums + S) must be even, or not possible
		if (sum & 1)	return 0;

		//...

	}
};

int main() {
	vector<int> nums = { 2,7,9,13,27,31,37,3,2,3,5,7,11,13,17,19,23,29,47,53 };
	int S = 107;

	Solution s;
	cout << s.findTargetSumWays(nums, S);

	return 0;

}