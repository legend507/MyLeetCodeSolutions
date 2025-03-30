# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part. For example, the string "ababcc" can be partitioned into ["abab", "cc"], but partitions such as ["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.

# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

# Return a list of integers representing the size of these parts.

 

# Example 1:

# Input: s = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
# Explanation:
# The partition is "ababcbaca", "defegde", "hijhklij".
# This is a partition so that each letter appears in at most one part.
# A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
# Example 2:

# Input: s = "eccbbbbdec"
# Output: [10]

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Stores the last index of each character in 's'
        last_occurrence = [0] * 26
        for i, char in enumerate(s):
            last_occurrence[ord(char) - ord("a")] = i

        partition_end = 0
        partition_start = 0
        partition_sizes = []

        for i, char in enumerate(s):
            partition_end = max(
                partition_end, last_occurrence[ord(char) - ord("a")]
            )
            # End of the current partition
            if i == partition_end:
                partition_sizes.append(i - partition_start + 1)
                partition_start = i + 1

        return partition_sizes
    
# Algorithm
# Create an array lastOccurrence of size 26 to store the last index of each character in s.

# Iterate through s and update lastOccurrence to record the last position of each character.

# Initialize partitionStart and partitionEnd to 0 to track the start and end of the current partition, respectively.

# Create a list partitionSizes to store the sizes of partitions.

# Iterate through s:

# Update partitionEnd to the maximum of its current value and the last occurrence of the current character.
# If the current index i reaches partitionEnd, it means the partition is complete:
# Compute the partition size (i - partitionStart + 1) and add it to partitionSizes.
# Update partitionStart to i + 1 for the next partition.
# Return partitionSizes containing the sizes of all partitions.