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
	// 
	bool canCross(vector<int>& stones, int pos = 0, int k = 0) {
		// loop from next stone, if there is a stone that we can go from pos, jumping k-1, k, or k+1 
		for (int i = pos + 1; i < stones.size(); i++) {
			int gap = stones[i] - stones[pos];	// loop from i, calc gap between i and current pos
			if (gap < k - 1)	continue;		// ...k-1,k,k+1,..., if found next stone, continue until return false or true
			if (gap > k + 1)	return false;	// next stone too far away
			if (canCross(stones, i, gap))	return true;	
		}

		return (pos == stones.size() - 1);
	}

	bool canCross_DP(vector<int>& stones) {
		// To record available last steps to reach current position. Position 0 need 0 step to be reached
		unordered_map<int, unordered_set<int>> steps = { { 0,{ 0 } } };

		for (int pos : stones) {
			for (auto it = steps[pos].begin(); it != steps[pos].end(); it++) {  // record all future reachable positions
				if (*it - 1) { steps[pos + *it - 1].insert(*it - 1); }
				steps[pos + *it].insert(*it);
				steps[pos + *it + 1].insert(*it + 1);
			}
		}

		return steps[stones.back()].size();                                     // check if the last position is reachable
	}


	// the following code yields Time Limit Exceeded error...
	bool canCross_TLEError(vector<int>& stones) {
		int n = stones.size();
		if (n == 0)	return true;
		if (n == 1 && stones[0] == 0)	return true;
		if (n == 2 && stones[0] == 0) {
			if (stones[1] != 1)
				return false;
		}

		return doRecurse(stones, 1, 1);
	}
	bool doRecurse(vector<int>& stones, int curPos, int formerJump) {

		if (curPos < 0 || formerJump <= 0)	return false;

		// if the frog is in a position where another jump can reach stones[n-1]
		int expectedJump = stones[stones.size() - 1] - stones[curPos];
		if (expectedJump == formerJump + 1
			|| expectedJump == formerJump - 1
			|| expectedJump == formerJump)
			return true;

		// recurse case
		int targetElement1 = stones[curPos] + formerJump - 1;
		int targetElement2 = stones[curPos] + formerJump;
		int targetElement3 = stones[curPos] + formerJump + 1;
		bool ret = false;

		// found next formerJump - 1 stone
		auto itr = find(stones.begin(), stones.end(), targetElement1);
		if (itr != stones.end())
			ret = ret || doRecurse(stones, distance(stones.begin(), itr), formerJump - 1);

		// found next formerJump stone
		itr = find(stones.begin(), stones.end(), targetElement2);
		if (itr != stones.end())
			ret = ret || doRecurse(stones, distance(stones.begin(), itr), formerJump);

		// found next formerJump + 1 stone
		itr = find(stones.begin(), stones.end(), targetElement3);
		if (itr != stones.end())
			ret = ret || doRecurse(stones, distance(stones.begin(), itr), formerJump + 1);

		return ret;
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

	vector<int> nums = { 0,2};

	if (sol.canCross(nums))
		cout << "OK";
	else
		cout << "NG";


	system("pause");

	return 0;
}
