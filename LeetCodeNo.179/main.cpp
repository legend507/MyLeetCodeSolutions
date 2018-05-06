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


   static bool myCompare(const int i1, const int i2) {
       string s1 = to_string(i1);   int size1 = s1.size();
       string s2 = to_string(i2);   int size2 = s2.size();

       while(size1 > 0 && size2 > 0) {
           if(s1[size1-1] > s2[size2-1])        return true;
           else if (s1[size1-1] < s2[size2-1])  return false;

           size1 --;
           size2 --;
       }

       if(size1 == 0)   return true;
       else             return false;

   }

    string largestNumber(vector<int>& nums) {
        string ret;
        int size = nums.size();
        if(size == 0)   return ret;


        sort(nums.begin(), nums.end(), myCompare);

        for(auto const& value: nums)    cout << value << endl;

        return ret;
    }   
};

int main() {
    Solution s;

    vector<int> nums = {3,30,34,5,9};
    s.largestNumber(nums);

    return 0;
}