class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def reverse(s):
            return s[::-1]
        
        # Easy way to invert a string of 0 and 1.
        def invert(s):
            return ''.join('1' if char == '0' else '0' for char in s)
        s = '0'

        if n > 0:
            for _ in range(n):
                s = s + '1' + reverse(invert(s))
            
        return s[k-1]