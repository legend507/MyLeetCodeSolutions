class Solution:
    def uncommonFromSentences_stupid(self, s1: str, s2: str) -> list[str]:
        # My solution, but stupid.
        # I don't need to do all these, just concat s1 and s2, and count occurance.
        # Then find all words that occurend only once.
        s1_words = s1.split(' ')
        s2_words = s2.split(' ')

        s1_dict = {}
        for wo in s1_words:
            s1_dict[wo] = s1_dict.get(wo, 0) + 1
        s2_dict = {}
        for wo in s2_words:
            s2_dict[wo] = s2_dict.get(wo, 0) + 1

        s1_once = []
        for key, value in s1_dict.items():
            if value == 1:
                s1_once.append(key)
        s2_once = []
        for key, value in s2_dict.items():
            if value == 1:
                s2_once.append(key)
        
        ret = []
        for wo in s1_once:
            if wo not in s2_dict:
                ret.append(wo)
        for wo in s2_once:
            if wo not in s1_dict:
                ret.append(wo)
        return ret
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        s1_words = s1.split(' ')
        s2_words = s2.split(' ')

        s = s1_words + s2_words

        dict = {}
        for wo in s:
            dict[wo] = dict.get(wo, 0) + 1
        
        ret = []
        for key, value in dict.items():
            if value == 1:
                ret.append(key)
        return ret
