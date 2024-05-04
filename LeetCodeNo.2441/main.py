class Solution(object):
    def findMaxK(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()

        head, tail = 0, len(nums) - 1

        while head < tail:
            if nums[head] + nums[tail] == 0:
                return nums[tail]
            elif nums[head] + nums[tail] > 0:
                tail -= 1
            else:
                head += 1
        
        if nums[head] + nums[tail] == 0:
            return nums[tail]
        else:
            return -1
        
nums = [-1,10,6,7,-7,1]

s = Solution()

s.findMaxK(nums)