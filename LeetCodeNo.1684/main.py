class Solution:
    def all_char_in(self, str1: str, str2: str) -> bool:
        for char in str1:
            if char not in str2:
                return False
        return True
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        count = 0
        for word in words:
            word_distinct_sorted = ''.join(sorted(list(set(word))))
            if self.all_char_in(word_distinct_sorted, allowed):
                count += 1
        return count

s = Solution()

s.countConsistentStrings("abc", ["a","b","c","ab","ac","bc","abc"])