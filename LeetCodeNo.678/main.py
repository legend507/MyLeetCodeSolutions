class Solution(object):
    def checkValidString_my_solution_wrong(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s[0] == ')':
            return False
        
        left_count = 0
        star_count = 0

        for i in s:
            if i == '(':
                left_count += 1
            elif i == '*':
                star_count += 1
            # i == ')'
            else:
                if left_count > 0:
                    left_count -= 1
                # Use * for '('
                elif star_count > 0:
                    star_count -= 1
                else:
                    return False
                
        if left_count == 0:
            return True
        else:
            return False
        
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1
            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0
        return leftMin == 0
        
input = "((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()"

s = Solution()
s.checkValidString(input)