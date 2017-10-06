#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

class solution {
public:
    int maximumGap(vector<int>& nums) {
        if(nums.size() < 2) {
            return 0;
        }
        vector<int> gaps;
        // sort vector
        sort(nums.begin(), nums.end());
        //
        for(int i = 1; i < nums.size(); i++) {
            gaps.push_back(nums[i] - nums[i-1]);
        }
        return *max_element(gaps.begin(), gaps.end());
    }

};
int main() {
    solution s;
    vector<int> nums{1,2,3,4,67,8,3};

    cout << s.maximumGap(nums);
    return 0;
}