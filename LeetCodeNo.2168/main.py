# Medium
# Topics
# Companies
# Hint
# Given a digit string s, return the number of unique substrings of s where every digit appears the same number of times.
 

# Example 1:

# Input: s = "1212"
# Output: 5
# Explanation: The substrings that meet the requirements are "1", "2", "12", "21", "1212".
# Note that although the substring "12" appears twice, it is only counted once.
# Example 2:

# Input: s = "12321"
# Output: 9
# Explanation: The substrings that meet the requirements are "1", "2", "3", "12", "23", "32", "21", "123", "321".

class Solution_slow:
    # My solution, with help of Gemini. Too slow.
    def _qualify(self, subs: str) -> bool:
        from collections import Counter
        # This returns a dict with key = char, value = # of occurance.
        char_counter = Counter(subs)
        first_value = next(iter(char_counter.values()))  # Get the first value
        return all(value == first_value for value in char_counter.values())

    def equalDigitFrequency(self, s: str) -> int:
        # 1. Generate all possible substrings, no dups.
        all_substrings = [s[i:j] for i in range(len(s)) for j in range(i+1, len(s) + 1)]
        # print(all_substrings)
        # 2. For each substring, count the occurance of each digit.
        qualified_substrings = [x for x in all_substrings if self._qualify(x)]
        # print(qualified_substrings)
        return len(set(qualified_substrings))

# Approach 1: Optimized Brute Force
# Intuition
# In the brute-force approach, we would iterate over all substrings of s, calculate the frequency of all characters for each substring, and increment a counter if the substring has the desired property. To avoid counting duplicates, we would use a set to track unique substrings.

# However, this process is inefficient. For example, if we already know the frequency of all characters in the substring s[0:4], there is no need to recalculate these frequencies when considering the substring s[0:5]. Instead, we can maintain an array to store the character frequencies for substrings starting at the same position and simply update this array as we extend the substring by moving its endpoint to the right.
# Algorithm
# Initialize n to the size of the string s.
# Initialize an empty set, validSubstrings.
# Iterate over s with start from 0 to n - 1:
# Initialize a frequency table digitFrequency of size 10 to store the frequency of each digit in the substring s[start:end].
# Loop with end from start to n - 1:
# Add s[end] to the substring by incrementing digitFrequency[s[end] - '0'] by 1.
# Check whether all frequencies in substring s[start: end] are the same:
# Initialize commonFrequency to 0 and a boolean variable isValid to true.
# Iterate over digitFrequency with i from 0 to 9:
# If the current digit does not appear in the substring (i.e. digitFrequency[i] == 0), skip it.
# If this is the first digit that appears in the substring (i.e. commonFrequency == 0), set commonFrequency to digitFrequency[i].
# If the current element has a different frequency than commonFrequency, set isValid to false.
# If the substring is valid, insert it into the validSubstrings set.
# Return the size of validSubstrings.
# Complexity Analysis
# Let n be the size of the string s.

# Time complexity: O(n 
# 3
#  )

# The algorithm uses two nested loops to iterate over all possible substrings of s. For each substring, we perform two operations:

# Extracting the substring, which takes O(k) time, where k is the length of the substring.
# Inserting the substring into a set, which also takes O(k) time because it involves hashing the substring.
# In the worst case, k can be as large as n. Therefore, the total time complexity is O(n 
# 3
#  ).

# Space complexity: O(n 
# 3
#  )

# The algorithm creates a set to store all valid substrings of the input string s. There are roughly O(n 
# 2
#  ) substrings. Each substring could have a maximum length of up to n, so the set requires space proportional to O(n 
# 3
#  ). You could attempt to prove that the space complexity is actually more than just O(n 
# 2
#  ) as an extra challenge!

# Other parts of the algorithm use data structures like variables and a fixed-size frequency array (digitFrequency), which don’t grow with the size of the input. Therefore, these don’t contribute to increasing the space complexity.
class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        n = len(s)
        # Set to store unique substrings with equal digit frequency
        valid_substrings = set()

        # Iterate over each possible starting position of a substring
        for start in range(n):
            digit_frequency = [0] * 10  # Frequency array for digits 0-9

            # Extend the substring from 'start' to different end positions
            for end in range(start, n):
                digit_frequency[ord(s[end]) - ord("0")] += 1

                # Variable to store the frequency all digits must match
                common_frequency = 0
                is_valid = True

                for count in digit_frequency:
                    if count == 0:
                        continue  # Skip digits not in the substring
                    if common_frequency == 0:
                        # First digit found, set common_frequency
                        common_frequency = count
                    if common_frequency != count:
                        # Mismatch in frequency, mark as invalid
                        is_valid = False
                        break

                # If the substring is valid, add it to the set
                if is_valid:
                    substring = s[start : end + 1]
                    valid_substrings.add(substring)

        # Return the number of unique valid substrings
        return len(valid_substrings)