class Solution:
    def getMaximumXor_tooSlow(self, nums: List[int], maximumBit: int) -> List[int]:
        # My solution, time limit exceeded.
        threshold = 2 ** maximumBit
        N = len(nums)

        # 1. Pre calculated xor result of nums[0], nums[1, 2], nums[0, 1, 2, 3] ...
        pre_calc_xor = []
        current_xor = 0
        for i in nums:
            current_xor = current_xor ^ i
            pre_calc_xor.append(current_xor)
        
        # 2. For each, iteration, loop k thru 0->threshold, and find the best k.
        ret = []
        for i in range(N):
            xor = pre_calc_xor[N-1-i]
            max_xor = 0
            k_max = 0
            for k in range(0, threshold):
                cur = xor ^ k
                if cur > max_xor:
                    k_max = k
                    max_xor = cur
            ret.append(k_max)
        return ret
    
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        # Editorial sotluion.
        
        prefix_xor = [0] * len(nums)
        prefix_xor[0] = nums[0]
        for i in range(1, len(nums)):
            prefix_xor[i] = prefix_xor[i - 1] ^ nums[i]
        ans = [0] * len(nums)

        mask = (1 << maximumBit) - 1

        for i in range(len(nums)):
            # find k to maximize value
            current_xor = prefix_xor[len(prefix_xor) - 1 - i]
            ans[i] = current_xor ^ mask

        return ans