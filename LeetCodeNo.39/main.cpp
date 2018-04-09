/*
Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7,
A solution set is:
[
[7],
[2, 2, 3]
]
*/

#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <queue>
#include <string>
#include <stack>
#include <unordered_set>
using namespace std;

struct ListNode {
	int val;
	ListNode *next;
	ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:

	vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
		vector<bool> visited(candidates.size(), false);
		vector<int> oneResult;
		vector<vector<int>> ret;


		doRecurse(candidates, target, 0, oneResult, ret, visited, 0);
		return ret;
	}
	void doRecurse(vector<int>& candidates,
		const int target,
		int sum,
		vector<int>& oneResult,
		vector<vector<int>>& result,
		vector<bool>& visited,
		int start) {
		// base case
		if (sum == target) {
			result.push_back(oneResult);
			return;
		}
		if (sum > target) return;

		// recurse case
		for (int i = start; i < candidates.size(); i++) {
			//if (visited[i] == true)	continue;	// if each element in candidates can only be used once, uncomment this line

			sum += candidates[i];
			visited[i] = true;
			oneResult.push_back(candidates[i]);
			doRecurse(candidates, target, sum, oneResult, result, visited, i);

			// erase i
			sum -= candidates[i];
			visited[i] = false;
			oneResult.pop_back();
		}
	}

};

int main()
{

	vector<int> input = { 2, 3, 6, 7 };
	Solution s;

	vector<vector<int>> ret = s.combinationSum(input, 7);

	system("pause");
	return 0;
}

