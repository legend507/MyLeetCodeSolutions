# 1752. Check if Array Is Sorted and Rotated

class Solution:
    def check(self, nums: list[int]) -> bool:
        # Find the spot where nums[i] < nums[i-1]
        # concate nums[i:], nums[0:i];
        # Check if this is the nums.sort()

        spot = 0
        for i in range(len(nums)):
            if i - 1 >= 0:
                if nums[i-1] > nums[i]:
                    spot = i
                    break

        # nums is sorted.
        if spot == 0:
            return True
        
        nums_concat = nums[spot:] + nums[0:spot]
        print(nums_concat)

        nums_sorted = sorted(nums)

        if nums_concat == nums_sorted:
            return True
        else:
            return False

s = Solution()
s.check([2,1,3,4])