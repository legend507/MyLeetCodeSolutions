# 1662. Check If Two String Arrays are Equivalent

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word1_str = ''.join(word1)
        word2_str = ''.join(word2)

        return word1_str == word2_str