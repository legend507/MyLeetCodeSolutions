class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        idx = word.find(ch)
        if idx != -1:
            # string[:i] is a substring from 0 to i (not include string[i]).
            # string[i:] is a substring from i to end (include string[i]).
            # string[::-1] reverses a string.
            return word[:idx+1][::-1] + word[idx+1:]
        return word
        

s = Solution()

word = 'abcdefd'
ch = 'd'

print(s.reversePrefix(word, ch))
