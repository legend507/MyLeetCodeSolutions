class Solution:
    def compressedString(self, word: str) -> str:
        n = len(word)
        if n == 0:
            return ''
        ret = ''
        current_letter = word[0]
        count = 1
        for i in range(1, len(word)):
            letter = word[i]
            if current_letter == letter:
                count += 1
                # Deal with max=9.
                if count == 10:
                    ret += '9'+current_letter
                    count = 1
            else:
                ret += str(count)+current_letter
                count = 1
                current_letter = letter
        ret += str(count)+current_letter

        return ret