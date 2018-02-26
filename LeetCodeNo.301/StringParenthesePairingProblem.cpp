/* ATTENTION!!!!!!!!!!!
// 如果碰到（和）配对的问题，先用一下Code判断有多少个（ 和多少个）不能被配对

		for (auto oneChar : s) {
			// assume no ) will be found later, remove this (
			if (oneChar == '(') {
				leftP2Remove++;
			}
			// found a ), pair this ) with former (; if no former (, remove this )
			else if (oneChar == ')') {
				if (leftP2Remove != 0)
					leftP2Remove--;		// this ) has a former ( to match with
				else
					rightP2Remove++;	// no former (, remove this )
			}
		}

*/

#include    <iostream>
#include    <queue>
#include	<functional>
#include	<stack>
#include	<string>
#include	<iostream>
#include	<unordered_set>
using namespace std;

/*
To build a priority queue,
with a pointer to median
*/
class Solution {
public:
	vector<string> removeInvalidParentheses(string s) {
		unordered_set<string> ret1;

		string oneRet;
		stack<char> leftParenthese;

		int leftP2Remove = 0, rightP2Remove = 0;
		for (auto oneChar : s) {
			// assume no ) will be found later, remove this (
			if (oneChar == '(') {
				leftP2Remove++;
			}
			// found a ), pair this ) with former (; if no former (, remove this )
			else if (oneChar == ')') {
				if (leftP2Remove != 0)
					leftP2Remove--;
				else
					rightP2Remove++;
			}
		}

		recurseRemove(ret1, oneRet, s, leftParenthese, leftP2Remove, rightP2Remove);

		//	2nd, check all possible rets, 
		vector<string> ret(ret1.begin(), ret1.end());
		for (auto oneStr : ret) {
			cout << oneStr << endl;
		}

		for (vector<string>::iterator itr = ret.begin(); itr != ret.end(); /*no itr++*/) {
			stack<char> leftParenthesesTracker;

			for (auto oneChar : (*itr)) {
				if (oneChar == '(')
					leftParenthesesTracker.push('(');
				if (oneChar == ')')
					leftParenthesesTracker.pop();
			}
			if (!leftParenthesesTracker.empty())
				itr = ret.erase(itr);
			else
				itr++;
		}

		if (!ret.empty())
			return ret;
		else {
			vector<string> empty = { "" };
			return empty;
		}
	}

	void recurseRemove(unordered_set<string> & ret, 
		string oneRet, string s, 
		stack<char> leftParenthese, 
		int leftP2Remove, 
		int rightP2Remove) {

		// traverse the input string
		for (int i = 0; i < s.size(); i++) {

			// if not ( and not ), append
			if (s[i] != '(' && s[i] != ')') {
				oneRet += s[i];
			}
			// if (
			else if (s[i] == '(') {
				// 1. not put current ( into one ret
				if(leftP2Remove > 0)
					recurseRemove(ret, oneRet, s.substr(i + 1, s.size() - i), leftParenthese, leftP2Remove-1, rightP2Remove);

				// 2. put current ( into one ret
				leftParenthese.push(s[i]);
				oneRet += s[i];
			}
			// if ) and there is former (, 
			else if (s[i] == ')') {
				if (leftParenthese.empty()) {
					rightP2Remove--;
					continue;
				}

				// 1. not put current ) in final answer
				if(rightP2Remove > 0)
					recurseRemove(ret, oneRet, s.substr(i + 1, s.size() - i), leftParenthese, leftP2Remove, rightP2Remove-1);

				// 2. put current ) in final answer
				leftParenthese.pop();
				oneRet += s[i];
			}
		}

		if(leftP2Remove ==0 && rightP2Remove==0)
			ret.insert(oneRet);
	}

};

/**
* Your MedianFinder object will be instantiated and called as such:
* MedianFinder obj = new MedianFinder();
* obj.addNum(num);
* double param_2 = obj.findMedian();
*/

int main() {
	Solution sol;

	string input = { ")(f" };

	vector<string> ret;

	ret = sol.removeInvalidParentheses(input);

	for (auto oneStr : ret) {
		cout << oneStr << endl;
	}

	system("pause");
	return 0;

}

