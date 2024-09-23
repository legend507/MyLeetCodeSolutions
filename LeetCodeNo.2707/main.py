# 2707. Extra Characters in a String

# Remove words in a dictionary from a string, return min # of char left after removal.

class Solution:
    def minExtraChar_wrongAnswer(self, s: str, dictionary: list[str]) -> int:
        # Iter keys in dict, try to find their locations in s.
        # replace key in s with ' ' (since ' ' is not a valid input).
        # remove the ' ' and count length of the remining s.

        dictionary.sort(key=lambda item: len(item), reverse=True)
        for key in dictionary:
            while s.find(key) != -1:
                s = s.replace(key, ' ')
                print(s)
        s = s.replace(' ', '')
        return len(s)
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # Editorial solution.
        # 
        n = len(s)
        dictionary_set = set(dictionary)
        dp = [0] * (len(s) + 1)

        for start in range(n - 1, -1, -1):
            dp[start] = 1 + dp[start + 1]
            for end in range(start, n):
                curr = s[start: end + 1]
                if curr in dictionary_set:
                    dp[start] = min(dp[start], dp[end + 1])

        return dp[0]

s = Solution()
s.minExtraChar(s = "leetscode", dictionary = ["leet","code","leetcode"])