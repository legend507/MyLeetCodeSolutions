class Solution:
    def subarray_generator(self, nums):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)+1):
                yield nums[i:j]
    def maxSubArray_tooMuchMemory(self, nums: List[int]) -> int:
        # First thought: create all possible sub arr from nums.
        # This causes memory limit exceed error.
        n = len(nums)
        all_subarray = [nums[i:j] for i in range(n) for j in range(i+1, n+1)]

        ret = []
        for i in all_subarray:
            ret.append(sum(i))
        return max(ret)
    def maxSubArray_tooSlow(self, nums: List[int]) -> int:
        # Using a generator solved the memory problem, but caused time limit exceed problem.
        ret = float('-inf')
        for i in self.subarray_generator(nums):
            ret = max(ret, sum(i))
        return ret
    def maxSubArray_wrong(self, nums: List[int]) -> int:
        # Use a queue,
        # wrong solution, this doesn't count for max sub array appear in the middle of nums.
        queue = []
        ret = float('-inf')
        current_sum = 0
        for i in range(len(nums)):
            current_sum += nums[i]
            queue.append(nums[i])
            ret = max(ret, current_sum)
        while queue:
            head = queue.pop(0)
            current_sum -= head
            ret = max(ret, current_sum)
        return ret
    def maxSubArray_tooMuchMemory2(self, nums: List[int]) -> int:
        # Use DP, dp[i][j] is the sum of nums[i:j]
        # dp[i][j] = dp[i][j-1] + nums[j].
        # Still memory limit exceeded.
        n=len(nums)
        dp = [[0] * n for _ in range(n)]
        ret = -99999
        for i in range(n):
            for j in range(i, n):
                if i == j:
                    dp[i][j] = nums[i]
                    
                elif j - 1 < i:
                    pass
                else:
                    dp[i][j] = dp[i][j-1] + nums[j]
                ret = max(ret, dp[i][j])
        return ret
    
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize our variables using the first element.
        current_subarray = max_subarray = nums[0]

        # Start with the 2nd element since we already used the first one.
        for num in nums[1:]:
            # If current_subarray is negative, throw it away. Otherwise, keep adding to it.
            current_subarray = max(num, current_subarray + num)
            max_subarray = max(max_subarray, current_subarray)

        return max_subarray