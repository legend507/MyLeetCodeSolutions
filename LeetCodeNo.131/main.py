from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        n = len(s)

        def IsPalindrome(subs: str) -> bool:
            # Quick way to reverse a string.
            return subs == subs[::-1]

        def backtrack(start: int, path: List[str]):
            if start == len(s):
                result.append(path[:])
                return
            for end in range(start + 1, len(s) + 1):
                current_sub = s[start:end]
                if IsPalindrome(current_sub):
                    path.append(current_sub)
                    backtrack(end, path)
                    path.pop()
        
        result = []
        backtrack(0, [])
        return result

s = "aab"

sol = Solution()

print(sol.partition(s))


# Useful snippet, to get all possible partitions of a string.

# i is starting index (included), j is ending index (not included).
# for i in range(0, n):
#     for j in range(i+1, n + 1):
#         print(i, j, s[i:j])
#         if IsPalindrome(s[i:j]):
#             result.append(s[i:j])
# return result