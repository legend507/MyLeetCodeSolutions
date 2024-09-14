class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # This problem boils down to find the longest subarry, where all values in
        # this subarry is the max(nums).
        nums_max = max(nums)
        ret = []
        counter = 0
        for i in nums:
            if i == nums_max:
                counter += 1
            else:
                ret.append(counter)
                counter = 0
        ret.append(counter)
        return max(ret)