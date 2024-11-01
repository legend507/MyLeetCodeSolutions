class Solution:
    def coinChange_tooSlow(self, coins: list[int], amount: int) -> int:
        # Recursive way to solve the problem. Time limit exceed.
        if amount == 0:
            return 0
        
        def recursive(current_amount):
            # Base case, 1 coin to represent current_ammount.
            if current_amount in coins:
                return 1
            
            coins_needed = float('inf')
            for one_coin in coins:
                if current_amount - one_coin > 0:
                    coins_needed = min(coins_needed, 1 + recursive(current_amount - one_coin))
            
            return coins_needed

        ret = recursive(amount)

        return ret if ret != float('inf') else -1
    
    def coinChange(self, coins: list[int], amount: int) -> int:
        # Editorial solution.
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1 
    
s = Solution()
print(s.coinChange([1,2,5], 100))