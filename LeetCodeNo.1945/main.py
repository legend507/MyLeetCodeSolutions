# 1945. Sum of Digits of String After Convert

# The key here is to use ord() to change a char to int.

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        # Convert.
        convert = ''
        for i in s:
            convert += str(ord(i) - ord('a') + 1)
        # print(convert)
        
        # Transform.
        while k > 0:
            transform = 0
            for i in convert:
                transform += int(i)
            convert = str(transform)
            # print(convert)
            k -= 1
        return int(convert)
