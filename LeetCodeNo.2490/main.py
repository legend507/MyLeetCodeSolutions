class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        # Corner cases.
        if sentence[0] == ' ' or sentence[-1] == ' ':
            return False
        
        words = sentence.split(' ')
        n = len(words)
        for ptr in range(0, n-1):
            word1 = words[ptr]
            word2 = words[ptr+1]

            if word1[-1] != word2[0]:
                return False
            
        # Check first and last word.
        if words[0][0] != words[-1][-1]:
            return False
        else:
            return True