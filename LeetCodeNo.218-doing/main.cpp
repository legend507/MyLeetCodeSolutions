#include <vector>
#include <map>
#include <iostream>
#include <climits>
#include <set>
using namespace std;

/* Initial thinking */
// since the building coordinate is (0, INT_MAX]
// int array[2147483647] = {0};         <- this line will yield an error...



class Solution {
public:
    // input: [x_left, x_right, height]
    vector<pair<int, int> > getSkyline(vector<vector<int> >& buildings) {
        vector<pair<int, int> > ret;

        // multiset automatically sorts all input (ascending by default)
        multiset<pair<int, int> > criticalPoints;

        // 1. traverse buildings, find the "critical points", namely [x_left, height] and [x_right, height]
        for(auto oneBuilding:buildings) {
            // [x_left, -height], why -height? because we know the point is the left point of a building
            criticalPoints.emplace(make_pair(oneBuilding[0], -oneBuilding[2]));
            // [x_right, height]
            criticalPoints.emplace(make_pair(oneBuilding[1],  oneBuilding[2]));            
        }

        // 2. traverse all "critical points" to draw skyline
        multiset<int> highest({0});

        return ret;
    }
};

int main() {
    Solution s;

    vector<vector<int> > buildings = { {2,9,10}, {3,7,15}, {5,12,12}, {15,20,10}, {19,24,8} };

    s.getSkyline(buildings);

    cout << INT_MAX << endl;
    return 0;
}

