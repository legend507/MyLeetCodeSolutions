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
	bool isInterleave(string s1, string s2, string s3) {
		int s1Len = s1.size();
		int s2Len = s2.size();
		int s3Len = s3.size();

		if (s1Len ==0 && s2Len == 0 && s3Len == 0)
			return true;

		if (s1Len + s2Len != s3Len)
			return false;

		return doCheck(0, 0, 0, s1, s2, s3);

	}

	bool doCheck(int s1Idx, int s2Idx, int s3Idx, 
		const string &s1, 
		const string &s2,
		const string &s3) {

		// recurse case
		for (; s3Idx < s3.size(); s3Idx++) {
			if (s3[s3Idx] == s1[s1Idx] && s3[s3Idx] == s2[s2Idx]) {
				return (doCheck(s1Idx + 1, s2Idx, s3Idx + 1, s1, s2, s3) || doCheck(s1Idx, s2Idx + 1, s3Idx + 1, s1, s2, s3));
			}
			else if (s3[s3Idx] == s1[s1Idx]) {
				s1Idx += 1;
			}
			else if (s3[s3Idx] == s2[s2Idx]) {
				s2Idx += 1;
			}
			else {
				return false;
			}
		}

		// base case
		if (s1Idx == s1.size() && s2Idx == s2.size() && s3Idx == s3.size()) {
			return true;
		}
		else
			return false;
	}

};

int main() {
	string s1 = "aa";
	string s2 = "ab";
	string s3 = "aaba";

	Solution sol;

	if (sol.isInterleave(s1, s2, s3))
		cout << "YES" << endl;
	else
		cout << "NO" << endl;
	
	system("pause");
	return 0;
}
