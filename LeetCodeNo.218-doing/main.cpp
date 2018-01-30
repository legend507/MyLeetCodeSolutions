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
        multiset<int> highest({0});     // aka, priority queue to trace the highest building
        multiset<int>::iterator it;
        for(auto onePoint:criticalPoints) {

            if(onePoint.second < 0) {
                // if height < 0, meaning this point is a "start" point of a building
                // append this |height| to highest 
                highest.insert(-onePoint.second);

                // after append this height, check if this height is the largest element in highest
                // if YES, this point MUST be part of final result
                if( *(highest.end()) == -onePoint.second) {
                    ret.push_back(make_pair(onePoint.first, -onePoint.second));
                } else {
                    // if NO, do nothing
                }

            } else {
                // height > 0, this point is a "end" point of a building
                // before erase this height from highest, check if it is the largest element in highest
                // if YES, then this point must be on Skyline (but maybe not in return vector)
                if(*(highest.end()) == onePoint.second) {
                    ret.push_back(onePoint);
                } else {
                    // if NO, do nothing
                }

                // erase this |height| from heighest
                highest.erase(onePoint.second);
            }
        }
        // [DEBUG], to output all points in criticalPoints
        for(auto one:ret) {
            cout << one.first << "," << one.second << endl;
        }

        // 3. reconstruct return vector to meet the requirement
        

        return ret;
    }
};

int main() {
    Solution s;

    vector<vector<int> > buildings = { {2,9,10}, {2, 9, 11}, {2, 10, 10}, {3,7,15}, {5,12,12}, {15,20,10}, {19,24,8} };

    s.getSkyline(buildings);

    return 0;
}

