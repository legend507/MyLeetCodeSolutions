/*
一下Class实装 MyBST中insert func
*/

#include <vector>
#include <iostream>
#include <list>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <sstream>
#include <queue>
#include <set>
#include <algorithm>
#include <functional>
#include <iomanip>
#include <stack>
using namespace std;

struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;

	// Constructor
	TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class MyBST {
	TreeNode* root;
public:
	MyBST(): root(NULL) {}

	/*
	插入新element*/
	int insert(int element) {
		// 插第一个node
		if (root == NULL) {
			root = new TreeNode(element);
			return 0x00;
		}

		TreeNode* curRoot = root;
		TreeNode* nextNode = curRoot;

		/*
		一下while找到一个既存node，
		通过比较val和element的大小决定插坐还是插右*/
		while (nextNode != NULL) {
			curRoot = nextNode;
			// element too small, go left
			if (curRoot->val >= element) {
				nextNode = curRoot->left;
			}
			// element big, go right
			else {
				nextNode = curRoot->right;
			}
		}

		(curRoot->val >= element) ? curRoot->left = new TreeNode(element) : curRoot->right = new TreeNode(element);

		return 0x00;
	}

	TreeNode* returnMinNode() {
		TreeNode* curRoot = root;
		while (curRoot->left != NULL)	curRoot = curRoot->left;

		return curRoot;
	}

	int deleteNode(int element) {
		if (root == NULL)	return 0x01;	// error code

		TreeNode* father = root;
		TreeNode* deleteMe = root;
		while (deleteMe != NULL) {

			// element too small, go left
			if (deleteMe->val > element) { father = deleteMe; deleteMe = deleteMe->left; }
			// element too big, go right
			else if (deleteMe->val < element) { father = deleteMe; deleteMe = deleteMe->right; }
			// found deleteMe
			else								break;
		}

		// NOT found, return error code
		if (deleteMe == NULL)	return 0x01;

		// found node to delete, check how many children it has
		/// deleteMe has NO child
		if (deleteMe->left == NULL && deleteMe->right == NULL) {
			if (father->left == deleteMe)	father->left = NULL;
			else							father->right = NULL;
			delete deleteMe;
		}
		/// deleteMe has RIGHT child
		else if (deleteMe->right != NULL) {

		}
		/// deleteMe has LEFT child
		else if (deleteMe->left != NULL) {

		}
		/// deleteMe has BOTH child
		else {

		}

		return 0x00;
	}

};


int main() {
	MyBST myBST;

	myBST.insert(50);
	myBST.insert(30);
	myBST.insert(20);
	myBST.insert(40);
	myBST.insert(70);
	myBST.insert(60);
	myBST.insert(80);
	myBST.insert(71);

	myBST.deleteNode(80);

	system("pause");
	return 0;
}

