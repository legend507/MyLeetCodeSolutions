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
struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;

	// Constructor
	TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
///////////////////////////////////////////////////////////////////////
class Solution {
public:
// Say I'm in curPos now, if I jump to nextPos, I want to make sure that nextPos-curPos+nums[nextPos] reachs the maximum
	int jump(vector<int>& nums) {

		int n = nums.size();

		if (n == 1)
			return 0;

		int curPos = 0;
		int howManySteps = 0;
		while (curPos < n - 1) {
			if (nums[curPos] == 0)	return 0;	// stuck at current position
			if (curPos == n - 1)	return howManySteps;

			int furthestMove = 0;
			int nextPos = -1;
			// from nums[curPos], take step steps, land on nums[nextPos]
			for (int step = 1; step <= nums[curPos]; step++) {
				if (curPos + step >= n - 1) {
					return (howManySteps + 1);
				}

				else if (furthestMove <= step + nums[curPos + step]) {
					furthestMove = step + nums[curPos + step];
					nextPos = curPos + step;          
				}
			}
			curPos = nextPos;
			howManySteps++;
		}

		return howManySteps;
	}

	int jump_timeExceed(vector<int>& nums) {
		int n = nums.size();

		// dp[i][j] = min Jumps from nums[i] to nums[j]
		vector<vector<int>>	dp(n, vector<int>(n, -1));

		// 
		for (int begin = n-1-1; begin >=0; begin--) {
			for (int end = begin+1; end <n; end++) {

				// if we can jump from begin to end with 1 jump
				if (nums[begin] >= end - begin) {
					dp[begin][end] = 1;
				}
				// if we cannot
				else {
					int jumps = INT_MAX;

					for (int stepStone = begin + 1; stepStone < end; stepStone++) {
						//
						if (dp[begin][stepStone] > 0 && dp[stepStone][end] > 0) {
							jumps = min(jumps, dp[begin][stepStone] + dp[stepStone][end]);
						}
					}
					if (jumps != INT_MAX)
						dp[begin][end] = jumps;
				}

			}
		}

		return dp[0][n - 1] == -1 ? 0:dp[0][n-1];
	}

};

int main() {
	Solution sol;

	string s = "cbacdcbc";

	vector<vector<int>> matrix = {
		{1,2,3},
		{8,9,4},
		{7,6,5}
	};

	vector<int> nums = { 1,2, 1};

	cout << sol.jump(nums);


	system("pause");

	return 0;
}
