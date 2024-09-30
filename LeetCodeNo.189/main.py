# 189. Rotate Array

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        to_right = k % n

        to_move = []
        for i in range(n-to_right, n):
            to_move.append(nums[i])
        
        del nums[n-to_right:]

        for i in range(len(to_move) - 1, -1, -1):
            nums.insert(0, to_move[i])
