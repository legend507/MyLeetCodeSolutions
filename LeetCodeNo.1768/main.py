class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # 2 pointers, 
        p1, p2 = 0, 0
        ret = ''
        while p1 < len(word1) and p2<len(word2):
            ret = ret + word1[p1] + word2[p2]
            p1 += 1
            p2 += 1
        
        if p1 == len(word1):
            ret += word2[p2:]
        if p2 == len(word2):
            ret += word1[p1:]
        return ret
    