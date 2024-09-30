# 1903. Largest Odd Number in String

class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)

        for i in range(n, 0, -1):
            subs = num[0:i]
            if int(subs[-1]) % 2 != 0:
                return subs
        return ""
    