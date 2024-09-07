# This is too slow. But still solves the problem.
class StockSpannerSLOW:

    def __init__(self):
        self.daily_prices = []
        # Time out is solved by adding the following 2 var to track only the max price.
        self.max_price = 0
        self.max_index = -1

    def next(self, price: int) -> int:
        
        current_price = price
        self.daily_prices.append(price)

        # If current price is larger than all prev prices.
        # This saves a little bit of time in case of current price being the max price.
        if current_price > self.max_price:
            self.max_price = current_price
            self.max_index = len(self.daily_prices) - 1
            return len(self.daily_prices)

        # Else, the stupid way of counting all prev prices.
        n = len(self.daily_prices)

        count = 0
        for i in range(n-1, -1, -1):
            if current_price >= self.daily_prices[i]:
                count += 1
            else:
                break
        return count

# The main problem is Timeout. Need to figure out a way to cache.

# Someone else's solultion.
class StockSpanner:

    def __init__(self):
        # Stores every price and its span.
        self.stack = []

    def next(self, price):
        res = 1

        # Come to think of it, I only need to find the prev price that is nearest (but bigger) than current price.
        #   If new price < prev price, then 1.
        #   if new price >= prev price, then find the more prev price until the prev price is bigger.
        # This stack makes sure that the price in the [price, res] is always ASC.
        while self.stack and self.stack[-1][0] <= price:
            res += self.stack.pop()[1]
        self.stack.append([price, res])
        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)