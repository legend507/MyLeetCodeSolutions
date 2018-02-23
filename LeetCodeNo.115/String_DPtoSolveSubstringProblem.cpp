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
	int numDistinct(string s, string t) {
		/*
		Define dp[i][j] = the # of distinct subsequences of t[0...i-1] in s[0...j-1]	<- when i = 0, means t is empty, if i = 1, t has length of 1
		then we have the following 4 cases:
		1. dp[i][1] = 0		<- s is empty, if t is also empty see case 2, is t is not empty, 0
		2. dp[1][j] = 1		<- t is empty, which is considered to be 1 subsequence
		3. dp[i][j] = dp[i][j-1], if t[i-1] != s[j-1]
		4. dp[i][j] = dp[i][j-1] + dp[i-1][j-1], if t[i-1] == s[j-1]
					  ^^^^^^^^^^   ^^^^^^^^^^^^ <- t[0...i-2] in s[0...j-2], we use s[j-1] to match t[i-1]
						t[0...i-1] in s[0...j-2], we do NOT use s[j-1] to match t[i-1], rather we try to find another char in s[0...j-2] to match t[i-1]
		(4th case is tricky, think this through!!!)

		Based on those 4 cases, we can put up a solution.
		*/
		int tLen = t.size();	// row
		int sLen = s.size();	// col

		// never use dp[0][0], it's meaningless by definition
		vector<vector<int>> dp(tLen+1 /*row size*/, vector<int>(sLen+1 /*col size*/, 0 /*initial value*/));

		// case 1
		for (int i = 0; i < tLen+1; i++)	dp[i][0] = 0;
		// case 2
		for (int j = 0; j < sLen + 1; j++)	dp[0][j] = 1;
		// case 3 & 4 in same loop
		for (int i = 1; i < tLen + 1; i++) {
			for (int j = 1; j < sLen + 1; j ++ ) {
				// case 3
				if (t[i - 1] != s[j - 1])	dp[i][j] = dp[i][j - 1];
				// case 4
				if (t[i - 1] == s[j - 1])	dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1];
			}
		}

		return dp[tLen][sLen];	// t[0...tLen-1] in s[0...sLen-1]
	}
};

int main() {
	Solution sol;

	string s = "b";
	string t = "b";

	cout << sol.numDistinct(s, t);

	system("pause");

	return 0;
}
