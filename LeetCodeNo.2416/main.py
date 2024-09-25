# 2416. Sum of Prefix Scores of Strings

# You are given an array words of size n consisting of non-empty strings.

# We define the score of a string word as the number of strings words[i] such that word is a prefix of words[i].

# For example, if words = ["a", "ab", "abc", "cab"], then the score of "ab" is 2, since "ab" is a prefix of both "ab" and "abc".
# Return an array answer of size n where answer[i] is the sum of scores of every non-empty prefix of words[i].

# Note that a string is considered as a prefix of itself.

# Example 1:

# Input: words = ["abc","ab","bc","b"]
# Output: [5,4,3,2]
# Explanation: The answer for each string is the following:
# - "abc" has 3 prefixes: "a", "ab", and "abc".
# - There are 2 strings with the prefix "a", 2 strings with the prefix "ab", and 1 string with the prefix "abc".
# The total is answer[0] = 2 + 2 + 1 = 5.
# - "ab" has 2 prefixes: "a" and "ab".
# - There are 2 strings with the prefix "a", and 2 strings with the prefix "ab".
# The total is answer[1] = 2 + 2 = 4.
# - "bc" has 2 prefixes: "b" and "bc".
# - There are 2 strings with the prefix "b", and 1 string with the prefix "bc".
# The total is answer[2] = 2 + 1 = 3.
# - "b" has 1 prefix: "b".
# - There are 2 strings with the prefix "b".
# The total is answer[3] = 2.

class trie_node:
    def __init__(self):
        self.next = [None] * 26
        self.cnt = 0

class Solution:
    def sumPrefixScores_tooSlow(self, words: List[str]) -> List[int]:
        # Solves the problem, but too slow.

        # 1. find all possible prefixes among all words.
        prefix = set()
        for word in words:
            for i in range(1, len(word) + 1):
                if word[0:i] not in prefix:
                    prefix.add(word[0:i])
        prefix = list(prefix)
        # print(prefix)
        
        # 2. for all prefix, check their appearance in all the words.
        # the count array should be the # of appearance for each prefix.
        count = []
        for one_prefix in prefix:
            this_count = 0
            for word in words:
                if word.find(one_prefix) == 0:
                    this_count +=1
            count.append(this_count)
        # print(count)
        
        # 3. for each word, check if a certain prefix is this word's prefix, if so, add the mapping count to this word_count.
        ret = []
        for word in words:
            this_word_count = 0
            for i in range(len(prefix)):
                if word.find(prefix[i]) == 0:
                    this_word_count += count[i]
            ret.append(this_word_count)
        return ret
    
    # Editorial solution.
    def __init__(self):
        # Initialize the root node of the trie.
        self.root = trie_node()

    # Insert function for the word.
    def insert(self, word):
        node = self.root
        for c in word:
            # If new prefix, create a new trie node.
            if node.next[ord(c) - ord("a")] is None:
                node.next[ord(c) - ord("a")] = trie_node()
            # Increment the count of the current prefix.
            node.next[ord(c) - ord("a")].cnt += 1
            node = node.next[ord(c) - ord("a")]

    # Calculate the prefix count using this function.
    def count(self, s):
        node = self.root
        ans = 0
        # The ans would store the total sum of counts.
        for c in s:
            ans += node.next[ord(c) - ord("a")].cnt
            node = node.next[ord(c) - ord("a")]
        return ans

    def sumPrefixScores(self, words):
        N = len(words)
        # Insert words in trie.
        for i in range(N):
            self.insert(words[i])
        scores = [0] * N
        for i in range(N):
            # Get the count of all prefixes of given string.
            scores[i] = self.count(words[i])
        return scores
    
