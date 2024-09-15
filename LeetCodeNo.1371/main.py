class Solution:
    def __init__(self) -> None:
        # Save some time by not re-computing.
        self.records = []
        self.max_length = -1
    def _is_vowel(self, substring):
        if substring in self.records or len(substring) <= self.max_length:
            return False
        self.records.append(substring)
        a = substring.count('a')
        e = substring.count('e')
        i = substring.count('i')
        o = substring.count('o')
        u = substring.count('u')
        if (a == 0 or a % 2 == 0 ) and (e==0 or e%2 == 0) and (i==0 or i%2==0) and (o==0 or o%2==0) and (u==0 or u%2==0):
            self.max_length = len(substring)
            return True
        else:
            return False
    def findTheLongestSubstring_slow(self, s: str) -> int:
        # Simple thought: Generate all possible substrings.
        # For each substring, check if is vowel.
        all_substrings = [s[i:j] for i in range(len(s)) for j in range(len(s), i, -1) 
                          if self._is_vowel(s[i:j])
                          ]
        all_substrings.sort(key=lambda item: len(item), reverse=True)
        return len(all_substrings[0]) if all_substrings else 0
    
    def findTheLongestSubstring(self, s: str) -> int:
        # LeetCode's editorial solution.
        # Algorithm
        # Initialize an integer variable prefixXOR and set it to 0.
        # Initialize a character array characterMap[26] where specific vowel characters ('a', 'e', 'i', 'o', 'u') have unique mask values (1, 2, 4, 8, 16).
        # Initialize an array mp of size 32, where all elements are set to -1. This will store the index of the first occurrence of each prefixXOR value.
        # Initialize an integer variable longestSubstring and set it to 0.
        # Iterate through each character in the string s:
        # Update prefixXOR by XORing it with the mask value of the current character (from characterMap).
        # If the current prefixXOR value is not found in mp and prefixXOR is not 0:
        # Store the current index in mp at the position corresponding to prefixXOR.
        # Update longestSubstring by comparing it with the difference between the current index and mp[prefixXOR].
        # Return longestSubstring as the final result.
        prefixXOR = 0
        characterMap = [0] * 26
        characterMap[ord("a") - ord("a")] = 1
        characterMap[ord("e") - ord("a")] = 2
        characterMap[ord("i") - ord("a")] = 4
        characterMap[ord("o") - ord("a")] = 8
        characterMap[ord("u") - ord("a")] = 16
        mp = [-1] * 32
        longestSubstring = 0
        for i in range(len(s)):
            prefixXOR ^= characterMap[ord(s[i]) - ord("a")]
            if mp[prefixXOR] == -1 and prefixXOR != 0:
                mp[prefixXOR] = i
            longestSubstring = max(longestSubstring, i - mp[prefixXOR])
        return longestSubstring

