# Given a string s and an integer k, return the number of substrings in s of length k with no repeated characters.

# Example 1:

# Input: s = "havefunonleetcode", k = 5
# Output: 6
# Explanation: There are 6 substrings they are: 'havef','avefu','vefun','efuno','etcod','tcode'.
# Example 2:

# Input: s = "home", k = 5
# Output: 0
# Explanation: Notice k can be larger than the length of s. In this case, it is not possible to find any substring.
 
class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        # Thoughts:
        # 1. for every char in s, try to create a string from that char, using i to track how many chars are in so far.
        answers = []
        for start in range(0, len(s)):
            answer = ''
            for i in range(k):
                if start + i < len(s):
                    current_char = s[start + i]
                    if current_char in answer:
                        break
                    else:
                        answer += current_char
                else:
                    break
            if len(answer) == k:
                answers.append(answer)
        print(answers)
        return len(answers)
