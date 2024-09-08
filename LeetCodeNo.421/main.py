class Solution:
    def findMaximumXOR(self, nums: list[int]) -> int:
        
        # Erase dups to avoid time out.
        # This still doesn't solve the timeout... Decided to give up solving this one. This is more like a mind twister.
        nums_set = list(set(nums))

        n = len(nums_set)
        max_xor = -999

        for i in range(n):
            for j in range(i, n):
                xor = nums_set[i] ^ nums_set[j]

                if xor > max_xor:
                    max_xor = xor

        return max_xor
    
s = Solution()
s.findMaximumXOR([5,5,5,19,12])
