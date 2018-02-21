#include    <iostream>
#include    <queue>
#include	<functional>
#include	<stack>
#include	<string>
#include	<iostream>
#include	<unordered_set>
#include	<sstream>			// istringstream and ostringstream
#include	<set>
#include	<climits>
#include	<algorithm>
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
	int maximalRectangle(vector<vector<char>>& matrix) {
		if (matrix.empty()) return 0;

		int maxRec = 0;
		int colBoundary = matrix[0].size();
		int rowBoundary = matrix.size();

		for (int rIdx = 0; rIdx < rowBoundary; rIdx++) {
			for (int cIdx = 0; cIdx < colBoundary; cIdx++) {
				if (matrix[rIdx][cIdx] == '1') {
					maxRec = max(maxRec, findMaxArea(matrix, rIdx, cIdx));
				}
			}
		}

		return maxRec;
	}

	bool isCoordinateExist(const int rIdx, const int cIdx, const vector<vector<char>>& matrix) {
		if ((rIdx >= 0 && rIdx < matrix.size()) || (cIdx >= 0 && cIdx < matrix[0].size()))
			return true;
		return false;
	}

	int findMaxArea(const vector<vector<char>>& matrix, const int rIdx, const int cIdx) {
		int colBoundary = matrix[0].size();
		int rowBoundary = matrix.size();



		bool foundZero = false;
		multiset<pair<int, int>> rowCol;

		for (int rowPtr = rIdx; rowPtr < rowBoundary; rowPtr++) {
			for (int colPtr = cIdx; colPtr < colBoundary; colPtr++) {

				// 
				if (matrix[rowPtr][colPtr] == '0') {
					if (rowPtr == rIdx) {
						rowBoundary = rowPtr;
						continue;
					}
					if (colPtr == cIdx) {
						colBoundary = colPtr;
						continue;
					}
					rowCol.emplace(make_pair(rowPtr, colPtr));
				}
			}
		}

		int maxArea = 0;

		return 0;
	}


};

int main() {
	Solution s;
	/* matrix[row][col] */
	vector<vector<char>> matrix = {
		{ '1','0','1','0','0' },
		{ '1','0','1','1','1' },
		{ '1','1','1','1','1' },
		{ '1','0','0','1','1' }
	};

	cout << s.findMaxArea(matrix, 0, 0);

	system("pause");
	return 0;
}
