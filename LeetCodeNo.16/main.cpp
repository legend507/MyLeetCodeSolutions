/*

Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
*/
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        // input check
        int len = nums.size();

        sort(nums.begin(), nums.end());

        int closest = nums[0] + nums[1] + nums[2];

        for(int i1 = 0; i1 < len-2; i1 ++) {
            int i2 = i1+1;
            int i3 = len-1;

            while(i2 < i3) {
                int result = nums[i1] + nums[i2] + nums[i3];
                if(result == target)    return result;  // bese case scenario, found exact target

                else if(result > target)    i3 --;
                else                        i2 ++;

                if(abs(result - target) < abs(closest-target))  closest = result;
            }
        }

        return closest;
    }
};