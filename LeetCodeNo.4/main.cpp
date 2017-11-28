#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int totalSize = nums1.size() + nums2.size();
    
        for(int i = 0; i < nums1.size(); i++) {
            int j = totalSize / 2 - i;
            if( (nums1[i-1] < nums2[j]) && (nums1[i] > nums2[j-1]) ) {
                return (double)(max(nums1[i-1], nums2[j-1]) + min(nums1[i], nums2[j]))  /   2;
            }
        }
    }
};

double median(vector<int> vec)
{
        typedef vector<int>::size_type vec_sz;

        vec_sz size = vec.size();
        if (size == 0)
            throw domain_error("median of an empty vector");

        sort(vec.begin(), vec.end());

        vec_sz mid = size/2;

        return size % 2 == 0 ? (double)(vec[mid] + vec[mid-1]) / 2 : vec[mid];
}

int main() {
    Solution s;
    vector<int> nums1 = {1, 2, 3, 4, 5, 6, 8, 9, 14};
    vector<int> nums2 = {4, 6, 7, 9, 11, 12, 45, 67, 89, 90};

    cout << s.findMedianSortedArrays(nums1, nums2) << endl;

    // test - can also be used as a lousy way to solve the problem, this method costs too much time
    vector<int> merge;
    merge.reserve(nums1.size() + nums2.size());
    merge.insert(merge.end(), nums1.begin(), nums1.end());
    merge.insert(merge.end(), nums2.begin(), nums2.end());  
    sort(merge.begin(), merge.end());
    cout << median(merge);

    return 0;
}