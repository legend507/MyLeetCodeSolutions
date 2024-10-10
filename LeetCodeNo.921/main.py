class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        missing_left = 0

        for i in s:
            if i == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                else:
                    missing_left += 1
        return missing_left + len(stack)