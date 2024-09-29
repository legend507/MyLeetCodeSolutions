# 125. Valid Palindrome

class Solution:
    def checkPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1

        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False
        return True

    def isPalindrome(self, s: str) -> bool:

        valid_char = ''
        for one_char in s:
            if ord('a') <= ord(one_char.lower()) <= ord('z'):
                valid_char += one_char.lower()
            elif ord('0') <= ord(one_char) <= ord('9'):
                valid_char += one_char
        return self.checkPalindrome(valid_char)
