/*
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
[2],
[3,4],
[6,5,7],
[4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
*/
#include <iostream>
#include <list>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
	int minimumTotal(vector<vector<int>>& triangle) {
		int row = triangle.size();
		if (row == 0)	return 0;
		if (row == 1)	return triangle[0][0];

		// dp[i][j] = min on triangle[i][j]
		vector<vector<int>> dp(row, vector<int>(row, 0));
		dp[0][0] = triangle[0][0];
		for (int i = 1; i < row; i++) {

			// 
			for (int j = 0; j <= i; j++) {
				// deal with 2 edge cases
				if (j == 0) { dp[i][j] = dp[i - 1][j] + triangle[i][j]; continue; }
				if (j == i) { dp[i][j] = dp[i - 1][j - 1] + triangle[i][j]; continue; }

				// for element in the middle, 
				//	from t[i-1][j] or t[i-1][j-1], we can go to t[i][j]
				dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j];
			}
		}

		int ret = INT_MAX;
		for (auto oneEle : dp[row - 1])
			ret = min(ret, oneEle);

		return ret;
	}
};