# 540. Single Element in a Sorted Array
# Medium
# Topics
# Companies
# You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

# Return the single element that appears only once.

# Your solution must run in O(log n) time and O(1) space.

 

# Example 1:

# Input: nums = [1,1,2,3,3,4,4,8,8]
# Output: 2
# Example 2:

# Input: nums = [3,3,7,7,10,11,11]
# Output: 10
 

# Constraints:

# 1 <= nums.length <= 105
# 0 <= nums[i] <= 105

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] != nums[mid + 1]:
                right = mid
            else:
                left = mid + 2
        return nums[left]
    
    def stupidSolution(self, nums):
        if len(nums) == 1:
            return nums[0]

        skip = None
        for i in range(len(nums)):
            if i == len(nums) - 1:
                return nums[-1]
            if skip:
                skip = None
                pass
            else:
                if nums[i] == nums[i+1]:
                    skip = True
                else:
                    return nums[i]
            
nums = [3,3,7,7,10,11,11]
s = Solution()
print(s.stupidSolution(nums))