/*
Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.

*/

#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <set>
#include <queue>
using namespace std;

class Solution {
public:
	/** 下面的解法是错误的，
	string largestNumber(vector<int>& nums) {
	string ret;
	int size = nums.size();
	if(size == 0)   return ret;

	multiset<int> ms;
	for(int i=0; i < size; i++) {
	ms.insert(nums[i]);
	}

	for(auto itr = ms.begin(); itr != ms.end(); itr++) {
	ret += to_string(*itr);
	}
	return ret;
	}
	*/


/** 下面的myCompare跟屎一样
	static bool myCompare(const int i1, const int i2) {
		string s1 = to_string(i1);   int size1 = s1.size();	int ptr1 = 0;
		string s2 = to_string(i2);   int size2 = s2.size(); int ptr2 = 0;

		while (ptr1 < size1 && ptr2 <size2) {
			if (s1[ptr1] > s2[ptr2])        return true;
			else if (s1[ptr1] < s2[ptr2])  return false;

			ptr1++;
			ptr2++;
		}

		if (ptr1 == size1) {
			// check s2[ptr2] and s2[ptr2-1]
			if (s2[ptr2] > s2[ptr2 - 1])	return false;
			return true;
		}
		if (ptr2 == size2) {
			// check s1
			if (s1[ptr1] > s1[ptr1 - 1])	return true;
			return false;
		}

	}
	*/

	static bool myCompare(const int i1, const int i2) {
		string s1 = to_string(i1);
		string s2 = to_string(i2);

		if (stol(s1 + s2) > stol(s2 + s1))	return true;
		else return false;
	}

	string largestNumber(vector<int>& nums) {
		string ret;
		int size = nums.size();
		if (size == 0)   return ret;

		// deal with 0
		int zeros = 0;
		for (auto iter = nums.begin(); iter != nums.end(); /*no iter++*/) {
			if (*iter == 0) {
				iter = nums.erase(iter);	// must have this "iter ="
				zeros++;
			}
			else
				iter++;
		}
		if (nums.empty()) {
			ret = "0";
			return ret;
		}


		sort(nums.begin(), nums.end(), myCompare);

		for (auto const& value : nums)    ret += to_string(value);

		while (zeros != 0) {
			ret += "0";
			zeros--;
		}

		return ret;
	}
};

int main() {
	Solution s;

	vector<int> nums = {1,2,3,4,5,6,7,8,9,0};
	cout << s.largestNumber(nums) << endl;

	system("pause");

	return 0;
}