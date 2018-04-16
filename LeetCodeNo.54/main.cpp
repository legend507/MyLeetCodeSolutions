
#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <queue>
#include <string>
#include <stack>
#include <unordered_set>
using namespace std;

class Solution {
public:
	vector<int> spiralOrder(vector<vector<int>>& matrix) {
		vector<int> ret;
		if (matrix.size() == 0) return ret;


		int row = matrix.size();
		int col = matrix[0].size();
		int STEP = row * col;
		int count = 0;
		vector<vector<bool>> visited(row, vector<bool>(col, false));

		int i = 0;	// for row
		int j = 0;	// for col

		int dir = 0x0;	// 0x0, 0x1, 0x2, 0x3, 4 directions

		while (count < STEP) {
			visited[i][j] = true;	// mark current(i,j) visited
			ret.push_back(matrix[i][j]);
			count++;

			// check next step, based on current dir
			switch (dir) {
			case 0x0:
				// current dir right, j++
				//	if next step is out of boundry or next step visited
				if (j + 1 == col || visited[i][j + 1] == true) {
					dir = 0x1;	// change dir to down
					i = i + 1;	// 
					j = j;		//
				}
				else {
					i = i;
					j = j + 1;	// go one step right
				}
				break;
			case 0x1:
				// current dir down, i++
				//	if next step is out of boundry or next step visited
				if (i + 1 == row || visited[i + 1][j] == true) {
					dir = 0x2;	// change dir to left
					i = i;	// 
					j = j - 1;		//
				}
				else {
					i = i + 1;	// go one step down
					j = j;
				}
				break;
			case 0x2:
				// current dir left, j--
				//	if next step is out of boundry or next step visited
				if (j - 1 == -1 || visited[i][j - 1] == true) {
					dir = 0x3;	// change dir to up
					i = i - 1;
					j = j;
				}
				else {
					i = i;	// go one step down
					j = j - 1;
				}
				break;
			case 0x3:
				// current dir up, i--
				//	if next step is out of boundry or next step visited
				if (i - 1 == -1 || visited[i - 1][j] == true) {
					dir = 0x0;	// change dir to right
					i = i;
					j = j + 1;
				}
				else {
					i = i - 1;	// go one step down
					j = j;
				}
				break;
			}

		}
		return ret;
	}
};

int main()
{
	vector<vector<int>> matrix =
	{
		{ 1, 2, 3 },
	{ 4, 5, 6 },
	{ 7, 8, 9 },
	{ 11, 12, 100 }
	};


	Solution s;

	vector<int> ret = s.spiralOrder(matrix);



	system("pause");
	return 0;
}

