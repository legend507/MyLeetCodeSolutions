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
		if (t.empty() || s.empty()) {
			return 0;
		}

		stack<int> possibleAns;
		
		for (int idx = 0; idx < s.size(); idx ++) {
			if (s[idx] == t[0])
				possibleAns.push(idx);
		}

		while (!possibleAns.empty()) {
			int idx = possibleAns.top();
			possibleAns.pop();


		}
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
