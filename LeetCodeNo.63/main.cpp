/*
63. Unique Paths II

A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would there be?



An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
[0,0,0],
[0,1,0],
[0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

*/

#include <vector>
#include <iostream>
using namespace std;

class Solution {
	int bottom;	// how many rows
	int left;	// how many cols
public:
	/*--
	我原创
	Error! Following implementation exceeded time on test case 27/43.
	So the logic makes sense, but time consuming.
	*/
	int uniquePathsWithObstacles_error(vector<vector<int>>& obstacleGrid) {
		int ret = 0;
		bottom = obstacleGrid.size();
		if (bottom == 0)	return 0;
		left = obstacleGrid[0].size();

		doRecurse(obstacleGrid, ret, 0, 0);
		return ret;
	}
	void doRecurse(vector<vector<int>>& obstacleGrid, int& ret, int row, int col) {
		//base case, reached end
		if (row == bottom - 1 && col == left - 1 && obstacleGrid[row][col] == 0) {
			ret++;
			return;
		}
		//base case, invalid coordinate
		if (row >= bottom || col >= left) return;
		//base case, steped on a 1 
		if (obstacleGrid[row][col] == 1) return;

		// recurse case
		doRecurse(obstacleGrid, ret, row + 1, col);
		doRecurse(obstacleGrid, ret, row, col + 1);
	}

	/*
	我原创，这个是对的，并且beat 100%
	想法是，用一个path matrix来表示，到[i][j]一共有多少种方法
	1. 先看第一行和第一列，在看到1之前，把所有的path[i][0]和path[0][j]都设为1
	2. 再从[1][1]一行一行看，如果当前[i][j]是1，则path[i][j]设为0；否则 path[i][j]=path[i-1][j] + path[i][j-1]
	3. 最后看path[bottom-1][left-1]
	*/
	int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
		bottom = obstacleGrid.size();
		if (bottom == 0)	return 0;
		left = obstacleGrid[0].size();

		vector<vector<int>> path(bottom, vector<int>(left, 0));
		for (int i = 0; i < bottom && obstacleGrid[i][0] == 0; i++)	path[i][0] = 1;	// 看第一行，只有一种方法可以去这些cell
		for (int j = 0; j < left && obstacleGrid[0][j] == 0; j++) path[0][j] = 1;	// 看第一列，同样只有一种方法可以去这些cell

		for (int i = 1; i < bottom; i++) {
			for (int j = 1; j < left; j++) {
				if (obstacleGrid[i][j] == 1) {
					path[i][j] = 0;		// 这个cell是obstacle
					continue;
				}
				path[i][j] = path[i - 1][j] + path[i][j - 1];	// 从左边或上边都可以来这个cell
			}
		}

		return path[bottom - 1][left - 1];
	}
};