
/*
GoogleTechDevGuide Q

280. Wiggle Sort
Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

Example:

Input: nums = [3,5,2,1,6,4]
Output: One possible answer is [3,5,1,6,2,4]
*/

#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <queue>
#include <string>
#include <stack>
#include <algorithm>
using namespace std;

class Solution {
public:
	/*别人的方法，beat了8%...
	想法很简单，最后结果只需要满足	小大小大小大... 这种排列就OK
	Time: O(nlogn), for using sort()	*/
	void wiggleSort(vector<int>& nums) {
		// 1st, sort the vector
		sort(nums.begin(), nums.end());

		// 2nd, swap (2*i+1) and (2*i+2), for i = 0, 1, 2, ...
		for (int i = 0; 2*i+2 < nums.size(); i++) {
			swap(nums[2 * i + 1], nums[2 * i + 2]);
		}
	}

	/*
	也是别人的方法，需要数学证明一下
	*/
	void wiggleSort(vector<int>& nums) {
		bool less = true;

		for (int i = 0; i < nums.size(); i++) {
			if (less) {
				if (nums[i] > nums[i + 1]) swap(nums[i], nums[i + 1]);
			}
			else {
				if (nums[i] < nums[i + 1]) swap(nums[i], nums[i + 1]);
			}
		}
	}

};

int main()
{
	Solution sol;


	system("pause");
	return 0;
}