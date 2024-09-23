class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Sort nums, 
        nums.sort()
        n = len(nums)
        dict = {}
        for i in range(n):
            dict[nums[i]] = dict.get(nums[i], 0) + 1
            if dict[nums[i]] >= n//2+1:
                return nums[i]
