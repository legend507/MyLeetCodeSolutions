#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int expect = 1;
        sort(nums.begin(), nums.end());

        for(int i = 0; i < nums.size(); i++) {
            if(nums[i] > 0 ) {
                if(expect == nums[i]) {
                    expect ++;
                } else if(expect < nums[i]) {
                    return expect;
                } else {
                    // expect > nums[i]. do nothing
                }
            }
        }
        return expect;
    }
};

int main() {
    Solution s;
    vector<int> nums = {0, 2, 2, 1, 1};

    cout << s.firstMissingPositive(nums) << endl;

    return 0;
}

