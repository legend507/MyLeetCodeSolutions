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

	/*
	Dynamic Programming的想法很重要，
	下面的Func的想法是：把input nums分成substring来考虑
	以substring的长度为loop基准，取substring
		再以《最后》burst哪个ballon为loop基准，
		construct dp matrix
	！！
	我的那个not working 函数失败的原因可能是因为我的dp matrix的construct方法有问题，
	就经验来看，dp的方法总是只需要返回一个值，而我是要比较dp matrix最后一行所有值大小，返回最大的那个。。。
	*/
	int maxCoins(vector<int>& nums) {
		int n = nums.size();
		// 1 | n1, n2, ..., nn | 1
		nums.insert(nums.begin(),	1);
		nums.insert(nums.end(),		1);

		// dp[i][j] = max coin by bursting ballon from ni to nj
		vector<vector<int>> dp(n + 2, vector<int> (n + 2, 0));

		// loop based on substring len, namely len=j-i+1;
		for (int len = 1; len <= n; len++) {
			// loop based on starting of substring,
			for (int start = 1; start <= n - len + 1; start++) {
				int end = start + len - 1;
				int maxCoin = 0;

				// we decided start, len and len, 
				//	next we loop based on the last ballon to pop
				for (int pop = start; pop <= end; pop++) {
					int coin =
						dp[start][pop - 1]
						+ dp[pop + 1][end]
						+ nums[start - 1] * nums[pop] * nums[end + 1];
					maxCoin = max(maxCoin, coin);
				}
				dp[start][end] = maxCoin;
			}
		}

		return dp[1][n];

	}
	int maxCoins_2(vector<int>& nums) {
		int N = nums.size();
		nums.insert(nums.begin(), 1);
		nums.insert(nums.end(), 1);

		// rangeValues[i][j] is the maximum # of coins that can be obtained
		// by popping balloons only in the range [i,j]
		vector<vector<int>> rangeValues(nums.size(), vector<int>(nums.size(), 0));

		// build up from shorter ranges to longer ranges
		for (int len = 1; len <= N; ++len) {
			for (int start = 1; start <= N - len + 1; ++start) {
				int end = start + len - 1;
				// calculate the max # of coins that can be obtained by
				// popping balloons only in the range [start,end].
				// consider all possible choices of final balloon to pop
				int bestCoins = 0;
				for (int final = start; final <= end; ++final) {
					int coins = rangeValues[start][final - 1] + rangeValues[final + 1][end]; // coins from popping subranges
					coins += nums[start - 1] * nums[final] * nums[end + 1]; // coins from final pop
					if (coins > bestCoins) bestCoins = coins;
				}
				rangeValues[start][end] = bestCoins;
			}
		}
		return rangeValues[1][N];
	}

	int maxCoins_notWorking(vector<int>& nums) {
		// shoot numOfBallon times(start from 1 -> [1, 2, 3..., numOfBallon + 1]),
		//	counting 2 ends, there are numOfBallon + 2 ballons
		int numOfBallon = nums.size();

		/*
		1, b1, b2, b3, ..., bn, 1	<- adding 1 to both end,
		and the valid ballon is labelled from 1 to n
		*/
		nums.push_back(1);
		nums.insert(nums.begin(), 1);

		// dynamic programming matrix
		//	dp[i][j]: the max coin if I burst bj on ith shoot
		//	scan every column in a row, then move to next row
		vector<vector<pair<int, unordered_set<int>>>> dp(numOfBallon + 1,
			vector<pair<int, unordered_set<int>>>(numOfBallon + 1, make_pair(0, unordered_set<int>()))
		);

		// 1st shoot - 1st row
		for (int j = 1; j < numOfBallon + 1; j++) {
			dp[1][j].first = nums[j - 1] * nums[j] * nums[j + 1];
			dp[1][j].second.insert(j);
		}

		for (int i = 2; i < numOfBallon + 1; i++) {	// start from 2nd row
			for (int j = 1; j < numOfBallon + 1; j++) {

				// check fomer row
				int maxCoin = 0;

				for (int k = 1; k < numOfBallon + 1; k++) {
					if (k == j)
						continue;

					pair<int, unordered_set<int>> oneEle = dp[i - 1][k];

					int howMuch = oneEle.first + takeShoot(oneEle.second, nums, j);
					if (maxCoin < howMuch) {
						maxCoin = howMuch;
						dp[i][j] = dp[i - 1][k];
					}
				}
				dp[i][j].first = maxCoin;
				dp[i][j].second.insert(j);

			}
		}

		int ret = 0;
		int whichOne = 0;
		for (int j = 1; j < numOfBallon + 1; j++) {
			ret = max(ret, dp[numOfBallon][j].first);
			if (ret == dp[numOfBallon][j].first)
				whichOne = j;
		}

		for (auto i : dp[numOfBallon][whichOne].second) {
			cout << i << endl;
		}

		return ret;
	}
	// calc coin earned after take shoot
	int takeShoot(unordered_set<int> isBursted, vector<int>& nums, int target) {

		// already bursted
		if (isBursted.find(target) != isBursted.end())
			return 0;

		isBursted.insert(target);

		int beforeTarget = target - 1;
		int afterTarget = target + 1;
		// find neightbor before target
		while (isBursted.find(beforeTarget) != isBursted.end())	beforeTarget--;
		// find neightbor after target
		while (isBursted.find(afterTarget) != isBursted.end())	afterTarget++;

		return nums[beforeTarget] * nums[target] * nums[afterTarget];

	}
};

int main() {
	Solution sol;

	string s = "b";
	string t = "b";
	vector<int> boxes = { 2,3,7,9,1,8,2 };

	cout << sol.maxCoins(boxes);

	system("pause");

	return 0;
}
