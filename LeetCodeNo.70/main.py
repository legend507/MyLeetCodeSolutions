from itertools import permutations

class Solution:
    def climbStairs_tooSlow(self, n: int) -> int:
        # Find max number of 2-step I can take.
        # Loop through 0 to max-2-step.
        # Use itertools.permutations to generate all possible ways.
        # Count the len.

        # Corner case.
        if n <= 1:
            return 1
        
        num_two_steps = n // 2

        count = 0
        # How many 2-step I take.
        for i in range(0, num_two_steps+1):
            num_one_step = n - i * 2
            all_steps = [1] * num_one_step + [2] * i
            print(all_steps, num_one_step, i)
            count += len(set(permutations(all_steps)))

        return count
    
    def climbStairs_stillTooSlow(self, n: int) -> int:
        # Editorial solution. But still too slow.
        return self.climb_recursive(0, n)
    
    def climb_recursive(self, now, n):
        # Current position = now.

        if now > n:
            return 0
        # Reached the end, count as 1 way to climb.
        if now == n:
            return 1
        return self.climb_recursive(now+1, n) + self.climb_recursive(now+2, n)
    
    def climbStairs(self, n: int) -> int:
        # DP, dp[i] = number of ways to reach ith step.
        # dp[i] = dp[i-1] + dp[i-2]
        # Think from simple cases, n = 1, 2, 3, 4.
        #                              1, 2, 3, 5.
        if n == 1:
            return 1
        dp = [0 for _ in range(n + 1)]
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]
