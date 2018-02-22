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
		Define dp[i][j] = the # of distinct subsequences of t[0...i-1] in s[0...j-1]
		then we have the following 4 cases:
		1. dp[i][0] = 0
		2. dp[0][j] = 1		<- t is empty, which is considered to be 1 subsequence
		3. dp[i][j] = dp[i][j-1], if t[i-1] != s[j-1]
		4. dp[i][j] = dp[i][j-1] + dp[i-1][j-1], if t[i-1] == s[j-1]
					  ^^^^^^^^^^   ^^^^^^^^^^^^ <- t[0...i-2] in s[0...j-2], we use s[j-1] to match t[i-1]
					  t[0...i-1] in s[0...j-2], we do NOT use s[j-1] to match t[i-1], rather we try to find another char in s[0...j-2] to match t[i-1]
		(4th case is actually tricky, think this through!!!)

		Based on those 4 cases, we can put up a solution.
		*/
	}
};

int main() {
	Solution sol;

	string s = "bccbcdcabadabddbccaddcbabbaaacdba";
	string t = "bccbbdc";

	cout << sol.numDistinct(s, t);

	system("pause");

	return 0;
}
