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
	int longestIncreasingPath(vector<vector<int>>& matrix) {
		if (matrix.size() == 0)
			return 0;

		//
		int row = matrix.size();
		int col = matrix[0].size();


		// dp[i][j] the longest path starting from matrix[i][j]
		vector<vector<int>> dp(row, vector<int>(col, 0));

        // assume longestPath = 1, 2, ..., row x col, loop search from 1
        //  one way to improve, another vector<int> isFixed, add fixed element to this vector
        //  e.g., for the example in main(), in first loo, we add 9, next add 8, ...
		for (int nowSearching = 1; ; nowSearching++) {
			bool found = false;
			for (int r = 0; r < row; r++) {
				for (int c = 0; c < col; c++) {
					int longestPath = 1;

					// can move up
					if (canMoveUp(matrix, r, c))	longestPath = max(longestPath, dp[r - 1][c] + 1);
					// can move down
					if (canMoveDown(matrix, r, c))	longestPath = max(longestPath, dp[r + 1][c] + 1);
					// can move left
					if (canMoveLeft(matrix, r, c))	longestPath = max(longestPath, dp[r][c - 1] + 1);
					// can move right
					if (canMoveRight(matrix, r, c))	longestPath = max(longestPath, dp[r][c + 1] + 1);

					if (longestPath == nowSearching) {
						dp[r][c] = longestPath;
						found = true;
					}
				}
			}
			if (!found) {
				return nowSearching - 1;
			}
		}
	}

	bool isCoordinateValid(const vector<vector<int>>& matrix, const int rIdx, const int cIdx) {
		if (rIdx < 0 || rIdx >= matrix.size())	return false;
		if (cIdx < 0 || cIdx >= matrix[0].size())	return false;

		return true;
	}

	bool canMoveUp(const vector<vector<int>>& matrix, const int rIdx, const int cIdx) {
		int upRIdx = rIdx - 1;
		int upCIdx = cIdx;
		// upper coordinate invalid
		if (!isCoordinateValid(matrix, upRIdx, upCIdx))
			return false;
		if (matrix[rIdx][cIdx] >= matrix[upRIdx][upCIdx])
			return false;

		return true;
	}
	bool canMoveDown(const vector<vector<int>>& matrix, const int rIdx, const int cIdx) {
		int downRIdx = rIdx + 1;
		int downCIdx = cIdx;
		// upper coordinate invalid
		if (!isCoordinateValid(matrix, downRIdx, downCIdx))
			return false;
		if (matrix[rIdx][cIdx] >= matrix[downRIdx][downCIdx])
			return false;

		return true;
	}
	bool canMoveLeft(const vector<vector<int>>& matrix, const int rIdx, const int cIdx) {
		int leftRIdx = rIdx;
		int leftCIdx = cIdx - 1;
		// upper coordinate invalid
		if (!isCoordinateValid(matrix, leftRIdx, leftCIdx))
			return false;
		if (matrix[rIdx][cIdx] >= matrix[leftRIdx][leftCIdx])
			return false;

		return true;
	}
	bool canMoveRight(const vector<vector<int>>& matrix, const int rIdx, const int cIdx) {
		int rightRIdx = rIdx;
		int rightCIdx = cIdx + 1;
		// upper coordinate invalid
		if (!isCoordinateValid(matrix, rightRIdx, rightCIdx))
			return false;
		if (matrix[rIdx][cIdx] >= matrix[rightRIdx][rightCIdx])
			return false;

		return true;
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

	cout << sol.longestIncreasingPath(matrix);

	system("pause");

	return 0;
}
