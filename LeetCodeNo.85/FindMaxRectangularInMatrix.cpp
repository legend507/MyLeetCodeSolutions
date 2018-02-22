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

		vector<int> height(colBoundary, 0);

		for (int rIdx = 0; rIdx < rowBoundary; rIdx++) {
			for (int cIdx = 0; cIdx < colBoundary; cIdx++) {
				if (matrix[rIdx][cIdx] == '0') {
					height[cIdx] = 0;
				}
				else
					height[cIdx] ++;
			}
			// calculate max rectangular after finish scanning one row
			maxRec = max(maxRec, largestRectangleArea(height));
		}

		return maxRec;
	}

	// solution for LeetCodeNo.84
	int largestRectangleArea(vector<int>& heights) {
		int n = heights.size();
		if (0 == n)  return 0;
		if (1 == n)  return heights[0];

		// traverse
		int area = 0;
		stack<int>	lowerHeight;	// a stack for index
		heights.push_back(0);

		for (int i = 0; i < heights.size(); i++) {

			while (!lowerHeight.empty() && heights[i] <= heights[lowerHeight.top()]) {
				int curHeight = heights[lowerHeight.top()];

				lowerHeight.pop();

				// stack[..., n-1, n], i		<- distance is between i and n-1
				//				   ^ poped out
				int distance = lowerHeight.empty() ? -1 : lowerHeight.top();	// !!! This is tricky
				area = max(area, curHeight * (i - distance - 1));				// updating area is tricky
			}

			lowerHeight.push(i);
		}
		return area;
	}
};

int main() {
	Solution s;
	/* matrix[row][col] */
	vector<vector<char>> matrix = {
		{ '1','0','1','0','0' },
		{ '1','0','1','1','1' },
		{ '1','1','1','0','1' },
		{ '1','0','0','1','1' }
	};

	cout << s.maximalRectangle(matrix);

	system("pause");
	return 0;
}
