class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        if x == 0:
            return True
        
        x_str = str(x)

        head, tail = 0, len(x_str) - 1

        while head < tail:
            if x_str[head] == x_str[tail]:
                head += 1
                tail -= 1
            else:
                return False
        
        return True