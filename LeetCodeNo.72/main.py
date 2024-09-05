# The idea is to build a 2D matrix dp where dp[i][j] represents the minimum number of operations required to transform 
# the substring word1[0...i-1] into the substring word2[0...j-1].

# THe solution boils down to constructing this dp metrix.

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1_len = len(word1)
        word2_len = len(word2)

        dp = [[0] * (word2_len + 1) for _ in range(word1_len + 1)]

        # Base cases,
        # dp[i][0] = i: transforming word1[0...i-1] into an empty string requires i deletions.
        for i in range(1, word1_len + 1):
            dp[i][0] = i
        
        # dp[0][j] = j: transforming an empty string into word2[0...j-1] requires j insertions.
        for j in range(1, word2_len + 1):
            dp[0][j] = j

        # Based on base cases,
        for i in range(1, word1_len + 1):
            for j in range(1, word2_len + 1):
                # If word1[i-1] == word2[j-1], then dp[i][j] = dp[i-1][j-1]. 
                # That is, no operation is required because the characters at positions i-1 and j-1 are already the same.
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # Otherwise, dp[i][j] is the minimum of the following three values:
                    # dp[i-1][j-1] + 1: replace the character at position i-1 in word1 with the character at position j-1 in word2.
                    # dp[i-1][j] + 1: delete the character at position i-1 in word1.
                    # dp[i][j-1] + 1: insert the character at position j-1 in word2 into word1 at position i.
                    dp[i][j] = min({
                        dp[i - 1][j - 1], # Replace
                        dp[i - 1][j], # Delete
                        dp[i][j - 1] # Insert
                        }) + 1

        print(dp)
        return dp[word1_len][word2_len]
