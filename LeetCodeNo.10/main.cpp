/*
炸看一下没什么头绪的题

GoogleTechDevGuide Q

10. Regular Expression Matching
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.	<- 这个注意，*要和*之前的char一起看
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"			<- 这个例子也要注意，.*可以match一切
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
*/

#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <queue>
#include <string>
#include <stack>
using namespace std;

class Solution {
public:
	/*
	下面方法是别人的，想法是递归，
	先看s和p的第一个char是否match，
	然后再根据p[1]是否是*来判断怎么递归
	Time: O(s^2 + p^2), s and p are length

	*/
	bool isMatch(string s, string p) {
		// base case
		if (p.empty()) return s.empty();	// if p is empty, then s has to be empty to be true

		/* check if 1st char is a match, the following cases are true
			1. s must NOT be empty,
			2. s[0] == s[0]
			3. p[0] is a .		*/
		bool firstChar = (!s.empty() && (s[0] == p[0] || '.' == p[0]));

		/* recurse case
			1. if p= ?*, ? stands for any char
				1. s remains the same, p[0] and p[1] means any number of p[0], so ignore (think of s=aab, p=c*a*b)
				2. firstChar= true, check s[1~end], and p remains the same
			2. else, firstChar must be true, and move on to compare next in both s and p
		*/
		if (p.size() >= 2 && p[1] == '*')
			// 如果想返回true，either s和p[2~end] match, or s[1~end]和pmatch
			return (isMatch(s, p.substr(2, p.size() - 2)) || (firstChar && isMatch(s.substr(1, s.size() - 1), p)));
		else
			// 如果想返回true，则 firstChar must be true
			return (firstChar && isMatch(s.substr(1, s.size() - 1), p.substr(1, p.size() - 1)));
	}

	/*
	Dynamic Programming解法，也是别人的
	Time: O(s*p), beat 100%
	*/
	bool isMatch_DP(string s, string p) {
		int sLen = s.size();
		int pLen = p.size();

		/*
		Definition: dp(i,j) = if s[i:] matches p[j:]
		*/
		vector<vector<bool >> dp(sLen + 1, vector<bool>(pLen + 1, false));
		dp[sLen][pLen] = true;	// 2 empty matches

		// traverse from end, i start from sLen
		for (int i = sLen; i >= 0; i--) {
			// j start from pLen - 1
			for (int j = pLen - 1; j >= 0; j--) {
				// same as above, check the 1st char 
				bool firstChar = (i < sLen &&
					(p[j] == s[i] || p[j] == '.'));

				if (j + 1 < pLen && p[j + 1] == '*') {
					// if ?*, 这一步是核心，理解一下
					dp[i][j] = dp[i][j + 2] || firstChar && dp[i + 1][j];
				}
				else {
					dp[i][j] = firstChar && dp[i + 1][j + 1];
				}
			}
		}
		return dp[0][0];
	}
};

int main()
{
	Solution sol;
	string s = "aab";
	string p = "c*a*b";

	(sol.isMatch_DP(s, p) == true) ? cout << "True" : cout << "False";

	system("pause");
	return 0;
}