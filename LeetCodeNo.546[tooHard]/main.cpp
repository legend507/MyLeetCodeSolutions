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
	int removeBoxes(vector<int>& boxes) {
	
	}

protected:
/* The following recursive method yield Time Limit Exceed error... */
	int removeBoxes(vector<int>& boxes) {

		vector<pair<int,int>> processedBox;
		int curColor = boxes[0];
		int count = 0;
		unordered_map<int, int> umCountColor;

		for (auto oneEle : boxes) {
			umCountColor[oneEle] ++;	// to count how many times a color appears

			if (oneEle != curColor) {
				processedBox.push_back(make_pair(curColor, count));
				curColor = oneEle;
				count = 1;
			} 
			else {
				count++;
			}
		}
		processedBox.push_back(make_pair(curColor, count));	// for last element

		unordered_set<int> colorToDelete;
		for (auto onePair : umCountColor) {
			if (onePair.second == 1)
				colorToDelete.insert(onePair.first);
		}
		for (vector<pair<int, int>>::iterator itr = processedBox.begin(); itr != processedBox.end();) {
			if (colorToDelete.find(itr->first) != colorToDelete.end()) {
				itr = processedBox.erase(itr);
			}
			else {
				itr++;
			}
		}

		int oneResult = colorToDelete.size();
		int max = oneResult;

		doRecurse(processedBox, oneResult, max);

		return max;
	}
	void process(vector<pair<int,int>>& processedBox) {
		int curColor = -1;
		int num = 0;

		for (vector<pair<int, int>>::iterator itr = processedBox.begin(); itr != processedBox.end(); itr++) {

			if (itr->first == curColor) {
				itr->second += num;
				itr--;
				itr = processedBox.erase(itr);
				num = itr->second;
			}
			else {
				curColor = itr->first;
				num = itr->second;
			}
		}

		//for (auto onePair : processedBox) {
		//	cout << onePair.first << " : " << onePair.second << " | ";
		//}
		//cout << endl;

	}
	void doRecurse(vector<pair<int, int>> processedBox, int oneResult, int &max) {
		process(processedBox);

		// base case
		if (processedBox.size() == 1) {
			oneResult += processedBox[0].second * processedBox[0].second;
			max = (oneResult > max ? oneResult : max);
		}

		// recurse case
		for (vector<pair<int, int>>::iterator itr = processedBox.begin(); itr != processedBox.end(); itr++) {
			pair<int, int> deletedElement = *itr;
			
			oneResult += deletedElement.second * deletedElement.second;

			itr = processedBox.erase(itr);
			doRecurse(processedBox, oneResult, max);
			itr = processedBox.insert(itr, deletedElement);

			oneResult -= deletedElement.second * deletedElement.second;
		}
	}
};

int main() {
	Solution sol;

	string s = "b";
	string t = "b";
	vector<int> boxes = { 1,3,2,2,2,3,4,3,1 };

	cout << sol.removeBoxes(boxes);

	system("pause");

	return 0;
}
