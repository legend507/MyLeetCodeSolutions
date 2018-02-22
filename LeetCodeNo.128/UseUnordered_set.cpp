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
	int longestConsecutive(vector<int>& nums) {
		if (nums.size() == 0)
			return 0;

		// construct hashtable using nums
		unordered_set<int> record(nums.begin(), nums.end());

		int ret = 1;

		// traverse nums
		for (auto oneNum : nums) {
			// if not found, this means already erased from former process
			if (record.find(oneNum) == record.end())	continue;

			// if found, then process this oneNum by going toward 0 and going towards +infinity 
			record.erase(oneNum);

			int preNum = oneNum - 1;
			int postNum = oneNum + 1;

			// go toward 0
			while (record.find(preNum) != record.end()) {
				record.erase(preNum);
				preNum--;
			}
			// go toward +inifinity
			while (record.find(postNum) != record.end()) {
				record.erase(postNum);
				postNum++;
			}

			ret = max(ret, postNum - preNum -1);	// think why -1

		}
		return ret;
	}
};

int main() {
	Solution s;
	/* matrix[row][col] */
	vector<vector<char>> matrix = {
		{ '1','0','1','0','0' },
		{ '1','0','1','1','1' },
		{ '1','1','1','0','1' },
		{ '1','0','0','1','1' }
	};
	vector<int> nums = { 100,4,200,1,3,2 };
	cout << s.longestConsecutive(nums) << endl;


	system("pause");
	return 0;
}
