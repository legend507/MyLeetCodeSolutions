/*
Dungeon Game
*/

#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <set>
#include <queue>
using namespace std;

class Solution {
protected:
	struct cell{
		int curHP;
		int toGo_i;
		int toGo_j;
		cell() :curHP(INT_MAX), toGo_i(-1), toGo_j(-1) {}
	};

public:
	/*
	start	: (0,0)
	end		: (size-1, size-1)
	*/
	int calculateMinimumHP(vector<vector<int>>& dungeon) {
		int ROW = dungeon.size() - 1;
		int COL = dungeon[0].size() - 1;
		vector<vector<cell>> matrix(ROW + 1, vector<cell>(COL + 1));

		if (dungeon[ROW][COL] <= 0)
			matrix[ROW][COL].curHP = abs(dungeon[ROW][COL]) + 1;
		else
			matrix[ROW][COL].curHP = 1;

		queue<pair<int, int>> toGo;
		toGo.push({ ROW,COL });

		while (!toGo.empty()) {
			pair<int, int> curCell = toGo.front();
			toGo.pop();

			int nextI;
			int nextJ;
			// go right
			nextI = curCell.first;
			nextJ = curCell.second - 1;
			if (nextI >= 0 && nextJ >= 0) {
				int newHP;
				// check dungeon[nextI][nextJ] is negative or positive
				if (dungeon[nextI][nextJ] > 0) {
					if (dungeon[nextI][nextJ] >= matrix[curCell.first][curCell.second].curHP) newHP = 1;
					else newHP = matrix[curCell.first][curCell.second].curHP - dungeon[nextI][nextJ];
				}
				else newHP = matrix[curCell.first][curCell.second].curHP + abs(dungeon[nextI][nextJ]);

				if (newHP < matrix[nextI][nextJ].curHP) {
					matrix[nextI][nextJ].curHP = newHP;
					matrix[nextI][nextJ].toGo_i = curCell.first;
					matrix[nextI][nextJ].toGo_j = curCell.second;

					toGo.push({ nextI, nextJ });
				}

			}
			// go up
			nextI = curCell.first - 1;
			nextJ = curCell.second;
			if (nextI >= 0 && nextJ >= 0) {
				int newHP;
				// check dungeon[nextI][nextJ] is negative or positive
				if (dungeon[nextI][nextJ] > 0) {
					if (dungeon[nextI][nextJ] >= matrix[curCell.first][curCell.second].curHP) newHP = 1;
					else newHP = matrix[curCell.first][curCell.second].curHP - dungeon[nextI][nextJ];
				}
				else newHP = matrix[curCell.first][curCell.second].curHP + abs(dungeon[nextI][nextJ]);

				if (newHP < matrix[nextI][nextJ].curHP) {
					matrix[nextI][nextJ].curHP = newHP;
					matrix[nextI][nextJ].toGo_i = curCell.first;
					matrix[nextI][nextJ].toGo_j = curCell.second;

					toGo.push({ nextI, nextJ });

				}

			}
		}
		int ret = matrix[0][0].curHP;
		return ret;
	}
};

int main()
{
	vector<vector<int>> dungeon = { {1, -2, 3},{2, -2, -2} };

	Solution s;
	s.calculateMinimumHP(dungeon);

	system("pause");
	return 0;
}