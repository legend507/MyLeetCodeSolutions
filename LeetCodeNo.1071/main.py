class Solution:

    def _is_dividable(self, denominator: str, numerator: str) -> bool:
        if not denominator or len(numerator) % len(denominator) != 0:
            return False
        
        concate_t = denominator * (len(numerator) // len(denominator))
        return concate_t == numerator


    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Start from str1, find all possible divisor substrings, put them in a list.
        # Sort by their length desc.
        # Check one by one in the sorted list, return the first (longest) divisor. If reach end, return none.

        possible_answer = []
        for i in range(len(str1) + 1):
            substr = str1[0:i]
            if self._is_dividable(substr, str1):
                possible_answer.append(substr)
        
        sorted_possible_answer = sorted(possible_answer, key=len, reverse = True)
        print(sorted_possible_answer)

        for one_substr in sorted_possible_answer:
            if self._is_dividable(one_substr, str2):
                return one_substr
        return ""