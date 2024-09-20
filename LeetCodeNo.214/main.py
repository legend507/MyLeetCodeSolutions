class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # Editorial solution.
        # Need to figure out the logic here.

        length = len(s)
        reversed_string = s[::-1]  # Reverse the string

        # Iterate through the string to find the longest palindromic prefix
        for i in range(length):
            # E.g. abcd, becomes bcda when reversed,
            # dcbaa              aabcd
            # I need to find which part of reverse_string's tail and s's head overlap.
            # Remove that overlap, then concate reverse_string's head to s.
            if s[: length - i] == reversed_string[i:]:
                return reversed_string[:i] + s
        return ""
