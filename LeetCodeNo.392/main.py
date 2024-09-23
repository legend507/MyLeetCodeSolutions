# 392. Is Subsequence

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for a_char in s:
            if a_char not in t:
                return False
            else:
                pos = t.find(a_char)
                t = t[pos+1:]
        return True