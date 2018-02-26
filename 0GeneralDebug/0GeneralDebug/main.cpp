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
	// LeetCodeNo.514
	int findRotateSteps(string ring, string key) {
		int keyLen = key.size();
		int ringLen = ring.size();

		// dp[i][j] = min action to find key[0,...,i] in ring, with pointer pointing to ring[j]
		vector<vector<int>>	dp(keyLen, vector<int>(ringLen, INT_MAX));

		// i== 0, find key[0] ins ring
		//	dp[0][j]	= found key[0] at ring[j], need to act dp[0][j] times
		for (int j = 0; j < ringLen; j++) {
			if (ring[j] == key[0]) {
				dp[0][j] = minRotate(ring, 0, j);
			}
		}

		/*
		the for loop above filled 1st row (dp[0][-])
		the for loop below will check from dp[1][-], if found j where ring[j] == key[1],
			check dp[0][-] again, calc the minimum steps needed
		*/
		for (int i = 1; i < keyLen; i++) {
			for (int j = 0; j < ringLen; j++) {
				
				if (ring[j] == key[i]) {
					for (int k = 0; k < ringLen; k++) {
						if(dp[i-1][k] != INT_MAX)	dp[i][j] = min(dp[i][j], dp[i-1][k] + minRotate(ring, k, j));
					}
				}
			}
		}

		int ret = INT_MAX;
		for (auto i : dp[keyLen - 1])
			ret = min(ret, i);

		return ret + key.size();
	}

	int minRotate(const string &ring, const int startPos, const int endPos) {
		int toRight;
		int toLeft;
		if (endPos >= startPos) {
			toRight = endPos - startPos;
			toLeft = startPos + (ring.size() - endPos);
		}
		else {
			// endPos < startPos
			toLeft = startPos - endPos;
			toRight = (ring.size() - startPos) + endPos;
		}

		return (toRight > toLeft ? toLeft : toRight);
	}
};

int main() {
	Solution sol;

	string ring = "godding";
	string t = "gd";

	cout << sol.findRotateSteps(ring, t);

	system("pause");

	return 0;
}
