class Solution:
    def minLength(self, s: str) -> int:
        # Use a stack-lie structure, and append char from s one by one.
        # Every time a char is appended, check the last 2 chars if they are AB or CD.
        # If so, pop the last 2.
        ret = ''
        for ch in s:
            ret += ch
            if ret[len(ret)-2:] == 'AB' or ret[len(ret)-2:] == 'CD':
                ret = ret[0:len(ret)-2]
        return len(ret)