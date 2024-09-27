# 35. Search Insert Position

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for idx, val in enumerate(nums):
            if val == target:
                return idx
            elif val > target:
                return idx 
        return len(nums)