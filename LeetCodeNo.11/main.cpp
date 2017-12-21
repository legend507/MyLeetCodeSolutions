#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxArea(vector<int>& height) {
        int area = 0;
        int ret = 0;
        int ptrLeft = 0;
        int ptrRight = height.size() - 1;

        while(ptrLeft < ptrRight) {
            area = (ptrRight - ptrLeft) * min(height[ptrLeft], height[ptrRight]);
            ret = ((ret < area) ? area:ret);
            (height[ptrLeft] < height[ptrRight]) ? (ptrLeft++) : (ptrRight--);
        }

        return ret;
    }
};

int main() {
    Solution s;
    vector<int> input = {1, 1};

    cout << s.maxArea(input) << endl;

    return 0;
}
