#include <vector>
#include <map>
#include <iostream>
#include <climits>
using namespace std;

/* Initial thinking */
// since the building coordinate is (0, INT_MAX]
// int array[2147483647] = {0};         <- this line will yield an error...



class Solution {
public:
    vector<pair<int, int>> getSkyline(vector<vector<int>>& buildings) {
        vector<pair<int, int>> ret;

        return ret;
    }
};

int main() {
    Solution s;
    vector<vector<int>> buildings = { {2,9,10}, {3,7,15}, {5,12,12}, {15,20,10}, {19,24,8} };

    s.getSkyline(buildings);

    cout << INT_MAX << endl;
    return 0;
}

