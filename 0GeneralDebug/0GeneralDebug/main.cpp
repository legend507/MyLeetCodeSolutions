/*
Given weights and values of n items, 
put these items in a knapsack of capacity W to get the maximum total value in the knapsack. 
In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items respectively. 
Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. 
You cannot break an item, either pick the complete item, or don’t pick it (0-1 property).

就是已知背包重量W，
物品价值和物品重量，
选择物品放入背包，问价值最大的放法
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
//    TreeNode* left, *right;
//
//    TreeNode(T x) : data(x), left(NULL), right(NULL) {}
//};

struct TreeNode
{
    char data;
    TreeNode* left, *right;
    
    TreeNode(char x) : data(x), left(NULL), right(NULL) {}
};

class KnapsackProblem {
    
public:
	/*
	递归方法，简单来说就是试一下所有情况，
	In the following recursion tree, K() refers to knapSack().  The two 
	parameters indicated in the following recursion tree are n and W.  
	The recursion tree is for following sample inputs.
	wt[] = {1, 1, 1}, W = 2, val[] = {10, 20, 30}

						   K(3, 2)         ---------> K(n, W)
					   /            \ 
					 /                \               
				K(2,2)                  K(2,1)
			  /       \                  /    \ 
			/           \              /        \
		   K(1,2)      K(1,1)        K(1,1)     K(1,0)
		   /  \         /   \          /   \
		 /      \     /       \      /       \
	K(0,2)  K(0,1)  K(0,1)  K(0,0)  K(0,1)   K(0,0)
	Recursion tree for Knapsack capacity 2 units and 3 items of 1 unit weight.
	*/
	int method1_recurse(int maxW, vector<int>& value, vector<int>& weight) {
		int checkWhich = 0;

		int result = doRecurse(maxW, value, weight, checkWhich);

		return result;

	}
	/*可以将这个递归func理解为，他总能返回
	在maxW的情况下，遍历item 0～n，挑选最大的
	*/
	int doRecurse(int maxW, vector<int>& value, vector<int>& weight, int index) {
		// base case - when maxW reaches 0, or checked all items
		if (maxW == 0 || index == value.size()) {
			return 0;
		}

		if (weight[index] > maxW) {
			// current item too heavy for current maxW
			return doRecurse(maxW, value, weight, index + 1);
		}
		else {

			// check the following cases, take bigger one
			//	1. if put current item into Knapsack
			//	2. if NOT put current item into Knapsack
			return max(
				value[index] + doRecurse(maxW - weight[index], value, weight, index+1),		/*Put current item in*/
				doRecurse(maxW, value, weight, index + 1)									/*Do not put current item in*/
			);
		}
	}


	int method2_dp(int maxW, vector<int>& value, vector<int>& weight) {
		int len = value.size();

		/*
		dp[i][j]=可以放i个item，最大重量是j的情况下，可得到的最大value
		*/
		vector<vector<int>> dp(len+1, vector<int>(maxW+1, 0));

		/*
		dp matrix有以下几个case，
		case 1：dp[0][w]=0，允许放0个item的时候最大value总是0
		case 2：dp[?][0]=0，maxW为0的情况下，最大value总是0
		case 3：（这个认真想一下）
			1. 如果item i 的重量wi > j，则现在的item不用考虑
				dp[i][j]=dp[i-1][j]
			2. 如果wi <= j，则考虑放和不放的情况
				dp[i][j]=max(
								dp[i-1][j],			// 不放当前item
								vi+dp[i-1][j-wi]	// 放当前item
							)
		*/
		for (int i = 0; i < len+1; i++) {
			for (int j = 0; j < maxW+1; j++) {
				if (i == 0) {dp[0][j] = 0; continue;}	// case 1
				if (j == 0) {dp[i][0] = 0; continue;}	// case 2

				// case 3
				if (weight[i-1] > j)		dp[i][j] = dp[i - 1][j];
				else	dp[i][j] = max(dp[i - 1][j], value[i-1] + dp[i - 1][j - weight[i-1]]);

			}
		}

		return dp[len][maxW];

	}

};


int main() {
	/*
	不能只看value per weight！！！
	看一下以下的例子，
	3个item的 value per weight分别是 60， 50， 40
	如果只看vpw的话，我应该先选重量10（剩下50-10=40）；再选20（剩下40-20=20）；然后就选不了了。。。最大value=60+100
	然而最大取值应该是选20和30的，最大value=100+120
	*/
	vector<int> value = { 60, 100, 120 };
	vector<int> weight = { 10, 20, 30 };
	int maxW = 50;

	KnapsackProblem ks;

	cout << ks.method2_dp(maxW, value, weight) << endl;

    system("pause");
    return 0;
}

