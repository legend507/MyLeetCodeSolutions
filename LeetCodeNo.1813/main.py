class Solution:
    def areSentencesSimilar_wrongAnswer(self, sentence1: str, sentence2: str) -> bool:
        # I started by attempting string manipulation
        # This has too many cases to consider.
        if len(sentence1) > len(sentence2):
            long = sentence1
            short = sentence2
        else:
            short = sentence1
            long = sentence2
        # Case 1, if short sentence is a one word sentence.
        if short.find(' ') == -1:
            # short appears as the first word in long or short appears as the lost word in long.
            if (long.find(short) == 0 and long[len(short)] == ' ') or (long.find(short) == len(long) - len(short) and long[len(long) - len(short) - 1] == ' '):
                return True
            else:
                return False
        else:
            # Case 2, 
            ptr = 0
            while ptr < len(short):
                if short[ptr] == ' ' or ptr == 0:
                    short_head = short[0:ptr]
                    short_tail = short[ptr:]
                    if long.find(short_head) == 0 and long.find(short_tail) == len(long) - len(short_tail):
                        return True
                ptr += 1
            return False

    def areSentencesSimilar(self, s1: str, s2: str) -> bool:
        # Editorial solution.
        deque1 = list(s1.split())
        deque2 = list(s2.split())
        # Compare the prefixes or beginning of the strings.
        while deque1 and deque2 and deque1[0] == deque2[0]:
            deque1.pop(0)
            deque2.pop(0)
        # Compare the suffixes or ending of the strings.
        while deque1 and deque2 and deque1[-1] == deque2[-1]:
            deque1.pop(-1)
            deque2.pop(-1)
        return not deque1 or not deque2