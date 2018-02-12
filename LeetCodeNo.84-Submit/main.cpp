#include    <iostream>
#include    <stack>
#include    <vector>
using namespace std;

class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int n = heights.size();
        if(0 == n)  return 0;
        if(1 == n)  return heights[0];


        int area = 0;
        stack<int>  indices;    // to record index whose height is >= current height
        
        heights.push_back(0);
        for(int i = 0; i < n; i++) {
            // keep the height in indices descending
            /*
            1,2,3,4,3,...
                    ^, this is when heights[indices.top()] > height[i]
            
            */
            while( !indices.empty() && heights[indices.top()] > heights[i]) {
                int curIndex = indices.top();
                indices.pop();

                int curArea = (i - curIndex) * heights[curIndex];
                if(curArea > area)
                    area = curArea;
            }
            indices.push(i);
        }

        return area;
    }
};

int main() {
    Solution s;
    vector<int> heights = {2,1,5,6,2,3};
    cout << s.largestRectangleArea(heights) << endl;
    return 0;
}
