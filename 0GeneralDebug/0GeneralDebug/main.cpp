/*
Given a string containing of ‘0’, ‘1’ and ‘?’ wildcard characters, generate all binary strings that can be formed by replacing each wildcard character by ‘0’ or ‘1’.

Input str = "1??0?101"
Output:
			10000101
			10001101
			10100101
			10101101
			11000101
			11001101
			11100101
			11101101
 */

#include <vector>
#include <iostream>
#include <list>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <sstream>
#include <queue>
#include <algorithm>
#include <functional>
#include <iomanip>
#include <stack>
using namespace std;

// A BST node
//template <typename T>
//struct TreeNode
//{
//    T data;
//	TreeNode* left, *right;
//    
//	TreeNode(T x) : data(x), left(NULL), right(NULL) {}
//};

struct TreeNode
{
	char data;
	TreeNode* left, *right;

	TreeNode(char x) : data(x), left(NULL), right(NULL) {}
};

class StringGenerator {
	

public:
	vector<string> recurseMethod(string str) {
		vector<int> index;
		for (int i = 0; i < str.size(); i++)
			if (str[i] == '?')
				index.push_back(i);

		vector<string> ret;
		recurseMethod(ret, index, str);

		return ret;
	}
	void recurseMethod(vector<string>& ret, vector<int>& index, string str) {

	}
};


int main() {
	TreeNode *root = new TreeNode('A');
	root->left = new TreeNode('B');
	root->right = new TreeNode('C');
	root->left->left = new TreeNode('D');
	root->left->right = new TreeNode('E');
	root->right->right = new TreeNode('B');
	root->right->right->right = new TreeNode('E');
	root->right->right->left = new TreeNode('D');

	root->right->right->right->left = new TreeNode('S');


	system("pause");
    return 0;
}
