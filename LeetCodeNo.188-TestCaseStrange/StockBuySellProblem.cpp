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

class Solution {
public:
	// allow k buy and k sell
	int maxProfit(int k, vector<int>& prices) {
		int size = prices.size();
		int ret = 0;	// max profit

		// 0 or 1 price in prices
		if (size < 2)
			return 0;

		// meaning I can buy/sell everyday, so only pick the price-up days
		if (k > size / 2) {
			for (int i = 1; i < size; i++)
				ret += max(prices[i] - prices[i - 1], 0);
		}

		// Now based on 
		vector<int> maxProfitK(k + 1, 0);				// initialize maxProfit after 1, 2, ..., k sells
		vector<int>	lowestBuyPriceK(k + 1, INT_MAX);	// 

		for (auto iDayPrice : prices) {
			for (int i = k; i >=1; i--) {
				maxProfitK[i] = max(maxProfitK[i], iDayPrice - lowestBuyPriceK[i]);
				lowestBuyPriceK[i] = min(lowestBuyPriceK[i], iDayPrice - maxProfitK[i - 1]);
			}
		}

		return maxProfitK[k];
	}

	// allow 1 buy and 1 sell
	int maxProfit_oneBuyAndSell(vector<int>& prices) {
		int size = prices.size();
		int ret = 0;	// max profit

		int maxProfit = 0;
		int lowestBuyPrice = INT_MAX;

		for (auto iDayPrice : prices) {
			maxProfit = max(maxProfit, iDayPrice - lowestBuyPrice);		// what if I sell today
			lowestBuyPrice = min(lowestBuyPrice, iDayPrice);			// what if I buy today
		}

		return maxProfit;
	}

	// allow 2 buy and 2 sell
	int maxProfit_twoBuyAndSell(vector<int>& prices) {
		int size = prices.size();
		int ret = 0;	// max profit

		int maxProfit1 = 0;					// profit after 1st sell
		int lowestBuyPrice1 = INT_MAX;		// when to buy my 1st buy
		int maxProfit2 = 0;					// profit after 2nd sell
		int lowestBuyPrice2 = INT_MAX;		// when to buy my 2nd buy

		for (auto iDayPrice : prices) {

			// checi if I should buy or sell for my 2nd buy and sell allowance
			maxProfit2 = max(maxProfit2, iDayPrice - lowestBuyPrice2);				// maxProfit2 means profit after 2nd sell
			lowestBuyPrice2 = min(lowestBuyPrice2, iDayPrice - maxProfit1);			// ?? Why iDayPrice - maxProfit1

			// check if I should buy or sell for my 1st buy and sell allowance
			maxProfit1 = max(maxProfit1, iDayPrice - lowestBuyPrice1);				// what if I sell today
			lowestBuyPrice1 = min(lowestBuyPrice1, iDayPrice);						// what if I buy today
		}

		return maxProfit2;
	}
};


int main() {
	Solution sol;
	vector<int>	prices = { 1, 2, 0, 4, 5, 1, 7, 6, 5, 4, 3, 2, 1 };

	cout << sol.maxProfit(3, prices) << endl;

	system("pause");
	return 0;

}
