# Given a string s, return true if a permutation of the string could form a palindrome and false otherwise.

 

# Example 1:

# Input: s = "code"
# Output: false
# Example 2:

# Input: s = "aab"
# Output: true
# Example 3:

# Input: s = "carerac"
# Output: true

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        # Thoughts: go through string once, and record how many chars have even and odd.

        from collections import Counter
        ret = Counter(s)

        even = 0
        odd = 0
        for key, value in ret.items():
            if value % 2 == 0:
                even +=1
            else:
                odd += 1
        
        if odd < 2:
            return True
        else:
            return False
