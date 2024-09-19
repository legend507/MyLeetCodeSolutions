import numpy as np
class Solution:
    # My solution, too slow.
    def threeSum_slow(self, nums: List[int]) -> List[List[int]]:
        # Sort nums first.
        ret = []
        nums.sort()
        n=len(nums)

        # For every num in nums, cal 2 sum = 0 - nums[i]
        # I need to find from nums[i:] that such numbers pair.
        for i, this_num in enumerate(nums):
            to_find_sum = 0 - this_num

            start, end = i+1, n-1
            while start < end and start > i and end < n:
                this_sum = nums[start] + nums[end]
                if this_sum == to_find_sum:
                    ret.append([this_num, nums[start], nums[end]])
                    # There might be other possible candidates, move start and end
                    # at the same time.
                    start += 1
                    end -= 1
                elif this_sum > to_find_sum:
                    end -= 1
                else:
                    start += 1
        # Example of removing dups from a list of lists.        
        return np.unique(np.array(ret), axis=0).tolist()

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Editorial solution.
        res = []
        nums.sort()
        for i in range(len(nums)):
            # Since nums is sorted,
            # and I'll try to find a soution from i+1 to n-1,
            # so if nums[i] > 0, then I can never find a solution.
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSumII(nums, i, res)
        return res

    def twoSumII(self, nums: List[int], i: int, res: List[List[int]]):
        lo, hi = i + 1, len(nums) - 1
        # Keep i not moved, move lo, hi based on current sum.
        while lo < hi:
            sum = nums[i] + nums[lo] + nums[hi]
            if sum < 0:
                lo += 1
            elif sum > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1
