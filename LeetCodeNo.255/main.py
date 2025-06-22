# Algorithm

# Declare an integer minLimit to a small value like negative infinity, and a stack.
# Iterate over preorder. For each num:
#   Clean the stack. While the top of the stack is less than num, pop from it and update minLimit.
#   If num <= minLimit, return false.
#   Push num onto the stack.
# Return true if we get through the whole input.

class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        min_limit = -inf
        stack = []
        
        for num in preorder:
            while stack and stack[-1] < num:
                min_limit = stack.pop()
                
            if num <= min_limit:
                return False
            
            stack.append(num)
        
        return True