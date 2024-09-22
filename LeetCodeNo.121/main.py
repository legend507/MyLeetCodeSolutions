class Solution:
    def maxProfit_tooSlow(self, prices: List[int]) -> int:
        # Thoughts: loop prices, for i, find max in i+1...n-1, and calculate max - prices[i]
        ret = []
        n = len(prices)

        if n <2:
            return 0

        for i in range(n-1):
            max_price = max(prices[i+1:])
            ret.append(max_price - prices[i])
        ret.sort(reverse=True)
        return ret[0] if ret[0] > 0 else 0

    def maxProfit(self, prices: List[int]) -> int:
        # Editorial solution.

        min_price = float("inf")
        max_profit = 0
        for i in range(len(prices)):
            # For each day, check current price is smaller than min price.
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                # If current day price is not min price, check profit if I sell
                max_profit = prices[i] - min_price

        return max_profit
