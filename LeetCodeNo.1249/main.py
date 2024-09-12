class Solution:
    # Use a stack to store (, when encounter ), pop from the stack.
    # If stack empty when encounter ), remove this.
    # If reach end but stack not empty, meaning we need to remove the ( stored in the stack.
    def minRemoveToMakeValid(self, s: str) -> str:
        record = []
        to_remove = []

        for i in range(len(s)):
            if s[i] == '(':
                record.append(i)
            if s[i] == ')':
                if len(record) > 0:
                    record.pop()
                else:
                    to_remove.append(i)
        to_remove = record + to_remove

        ret = ''

        for i in range(len(s)):
            if i not in to_remove:
                ret += s[i]
        return ret

