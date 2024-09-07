# Didn't solve this one on my own.
# I was initially thinking about using DP, but could get it right.

class Solution:

    # This answer is from Gemini, which originates from someone's github repo.
    def dailyTemperatures(self, temperatures):

        n = len(temperatures)
        answer = [0] * n
        stack = []

        # Create index of day, and the associated temperature.
        enum_temperatures = enumerate(temperatures)

        for i, temp in enum_temperatures:
            # Stack stores index of day. Top -> botton always DESC order by temperature.
            # If current day's temp is higher than stack top, meaning
            # that we found # of days to wait since the stack top index.
            while stack and temperatures[stack[-1]] < temp:
                prev_index = stack.pop() # Pop the very end element of the list.
                answer[prev_index] = i - prev_index
            stack.append(i)

        return answer

    def dailyTemperaturesDP(self, temperatures):
        # This doesn't work.
        # Attempted to solve this using DP, but don't think this coud work.
        n = len(temperatures)
        dp = [0] * n

        for i in range(n - 1, 1, -1):
            # Prev day temp is lower. Then # of days to wait from prev day is 1.
            # If prev day temp is equal or higher....
            # THIS IS THE PROBLEM, as 
            if temperatures[i - 1] < temperatures[i]:
                dp[i - 1] = 1
            else:
                # If there's no warmer day ahead, dp[i] should be 0
                dp[i -1] = dp[i] + 1 if dp[i] > 0 else 0
        print(dp)
        return dp


s = Solution()
s.dailyTemperaturesDP([73,74,75,71,69,72,76,73])
