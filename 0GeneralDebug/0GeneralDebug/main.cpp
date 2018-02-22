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
	vector<int> postorderTraversal(TreeNode* root) {
		vector<int> onePath;

		if (root == NULL)
			return onePath;


		stack<TreeNode*> dfsStack;

		dfsStack.push(root);

		while(!dfsStack.empty()) {
			TreeNode* oneNode = dfsStack.top();
			dfsStack.pop();

			onePath.push_back(oneNode->val);

			// if has left child
			if (oneNode->left != NULL) {
				dfsStack.push(oneNode->left);
			}

			if (oneNode->right != NULL) {
				dfsStack.push(oneNode->right);
			}

		}

		reverse(onePath.begin(), onePath.end());

		return onePath;
	}

	// find the longest path from oneEndNode to root
	vector<int> printTheLongestPath(TreeNode* root) {
		vector<int> onePath;

		if (root == NULL)
			return onePath;


		priority_queue<pair<int, vector<int>>> record;

		stack<TreeNode*> dfsStack;

		dfsStack.push(root);

		while (!dfsStack.empty()) {
			TreeNode* oneNode = dfsStack.top();
			dfsStack.pop();

			onePath.push_back(oneNode->val);

			// if has left child
			if (oneNode->left != NULL) {
				dfsStack.push(oneNode->left);
			}

			if (oneNode->right != NULL) {
				dfsStack.push(oneNode->right);
			}


			// when reach an end node
			if (oneNode->left == NULL && oneNode->right == NULL) {
				record.emplace(make_pair(onePath.size(), onePath));
				onePath.clear();
			}

		}

		vector<int> ret = (record.top()).second;

		reverse(ret.begin(), ret.end());

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

	TreeNode root(1);

	root.left = new TreeNode(2);
	root.left->right = new TreeNode(100);

	root.right = new TreeNode(3);
	root.right->left = new TreeNode(4);
	root.right->right = new TreeNode(5);
	root.right->right->right = new TreeNode(1000);

	vector<int> result = s.postorderTraversal(&root);

	for (auto oneElement : result)
		cout << oneElement << endl;


	system("pause");
	return 0;
}
