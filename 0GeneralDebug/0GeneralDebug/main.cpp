#include    <iostream>
#include    <queue>
#include	<functional>
#include	<stack>
#include	<string>
#include	<iostream>
#include	<unordered_set>
#include	<sstream>			// istringstream and ostringstream
#include	<set>
using namespace std;


struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;

	// Constructor
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
	int maxProfit(int k, vector<int>& prices) {
		int size = prices.size();
		queue<int>	peakIndex;
		queue<int> valleyIndex;

		// try to find all adjacent peak, valley
		//	put 0~size-1 to peakIndex or valleyIndex
		prices[0] > prices[1] ? peakIndex.push(0) : valleyIndex.push(0);
		for (int i = 1; i < prices.size() - 1; i++) {
			// i-1 < i > i+1
			if (prices[i-1] < prices[i]	
				&& prices[i] > prices[i+1]) {

				peakIndex.push(i);
			}
			// i-1 > i < i+1
			else if (prices[i-1] > prices[i]
				&& prices[i] < prices[i+1]){

				valleyIndex.push(i);
			}
		}
		prices[size - 2] > prices[size - 1] ? valleyIndex.push(size - 1) : peakIndex.push(size - 1);



	}
};


int main() {

	system("pause");
	return 0;

}
