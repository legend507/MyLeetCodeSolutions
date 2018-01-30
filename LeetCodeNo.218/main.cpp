#include <vector>
#include <map>
#include <iostream>
#include <climits>
#include <cstdlib>
#include <set>
using namespace std;

/* Initial thinking */
// since the building coordinate is (0, INT_MAX]
// int array[2147483647] = {0};         <- this line will yield an error...



class Solution {
public:
    // input: [x_left, x_right, height]
    vector<pair<int, int> > getSkyline(vector<vector<int> >& buildings) {

        pair<int, int> currentPoint (-1, 0);
        vector<pair<int, int> > ret;

        // multiset automatically sorts all input (ascending by default)
        multiset<pair<int, int> > criticalPoints;

        // 1. traverse buildings, find the "critical points", namely [x_left, height] and [x_right, height], and insert the 2 points to criticalPoints
        // before insert, check if the same 2 points already exist
        for(auto oneBuilding:buildings) {
            if(
                criticalPoints.find(make_pair(oneBuilding[0], -oneBuilding[2])) == criticalPoints.end() &&
                criticalPoints.find(make_pair(oneBuilding[1],  oneBuilding[2])) == criticalPoints.end()
                ) {
                    // [x_left, -height], why -height? because we know the point is the left point of a building
                    criticalPoints.emplace(make_pair(oneBuilding[0], -oneBuilding[2]));
                    // [x_right, height]
                    criticalPoints.emplace(make_pair(oneBuilding[1],  oneBuilding[2]));  
                }  
        }


        // [DEBUG], print all points in criticalPoints
        for(auto onePoint:criticalPoints) {
            cout << onePoint.first << "," << onePoint.second << endl;
        }
        cout << "---------------" << endl;                

        // 2. traverse all "critical points" to draw skyline
        multiset<int> height({0});     // aka, priority queue to trace the highest building
        for(auto onePoint:criticalPoints) {
            if(onePoint.second < 0) {
                // found a "start" point of a new building, record its height
                height.insert(-onePoint.second);
            } else {
                // found a "end" point of a buidling, erase it from height
                height.erase(height.find(onePoint.second));     // Tricky!!, if use height.erase(3), all duplicated 3s in height will be erased
            }

            // now, check 
            //  if insert a new building, check if it is the only highest (= last element of height && unique)
            //  if erase an old building, a little complicated
            //      check if it WAS the highest (> last element of height)
            if( -onePoint.second == *(--height.end()) && -onePoint.second > *(----height.end()) ) {
                ret.push_back(make_pair(onePoint.first, -onePoint.second));
            } else if (onePoint.second > *(--height.end())) {
                ret.push_back(make_pair(onePoint.first, *(--height.end())));
            } 
        }

        // [DEBUG], to output all points in criticalPoints
        for(auto one:ret) {
            cout << one.first << "," << one.second << endl;
        }
        cout << "---------------" << endl;                


        return ret;
    }
};

int main() {
    Solution s;

    vector<vector<int> > buildings = { {2,9,10}, {2, 9, 11}, {2, 10, 10}, {3,7,15}, {5,12,12}, {15,20,10}, {15,20,10}, {19,24,8} };
    //vector<vector<int> > buildings = { {2,9,10},{3,7,15},{5,12,12},{15,20,10},{19,24,8} };
    //vector<vector<int> > buildings = { {0,2,3}, {2,5,3} };

    s.getSkyline(buildings);

    return 0;
}

