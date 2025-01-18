# A 0-indexed array derived with length n is derived by computing the bitwise XOR (⊕) of adjacent values in a binary array original of length n.

# Specifically, for each index i in the range [0, n - 1]:

# If i = n - 1, then derived[i] = original[i] ⊕ original[0].
# Otherwise, derived[i] = original[i] ⊕ original[i + 1].
# Given an array derived, your task is to determine whether there exists a valid binary array original that could have formed derived.

# Return true if such an array exists or false otherwise.

# A binary array is an array containing only 0's and 1's
 

# Example 1:

# Input: derived = [1,1,0]
# Output: true
# Explanation: A valid original array that gives derived is [0,1,0].
# derived[0] = original[0] ⊕ original[1] = 0 ⊕ 1 = 1 
# derived[1] = original[1] ⊕ original[2] = 1 ⊕ 0 = 1
# derived[2] = original[2] ⊕ original[0] = 0 ⊕ 0 = 0
# Example 2:

# Input: derived = [1,1]
# Output: true
# Explanation: A valid original array that gives derived is [0,1].
# derived[0] = original[0] ⊕ original[1] = 1
# derived[1] = original[1] ⊕ original[0] = 1
# Example 3:

# Input: derived = [1,0]
# Output: false
# Explanation: There is no valid original array that gives derived.

# Approach 1: Simulation
# Intuition
# To determine whether a valid original array can be constructed from the given derived array, we can carefully simulate how the original array would be built.

# From the problem, we know:
# derived[i]=original[i]XORoriginal[i+1]

# Using the inversion property of XOR, we can rewrite this as:
# original[i+1]=derived[i]XORoriginal[i]

# This means that if we know the value of the original[i], we can calculate the next element, original[i+1], using the corresponding value from derived.

# The first element of original, original[0], can be either 0 or 1 (since it’s binary).

# If we assume original[0] = 0, we can calculate the rest of the array.
# Similarly, we can repeat the process assuming original[0] = 1.
# Once we compute all the elements of the original for both starting points, we need to check if they satisfy the circular condition:
# derived[n−1]=original[n−1]XORoriginal[0]

# This ensures that the last element in derived matches the XOR of the first and last elements of original.

# If the circular condition is satisfied for either of the two cases (original[0] = 0 or original[0] = 1), then a valid original array exists, and we return true. Otherwise, we return false.

# Algorithm
# Create an array original initialized with {0}.

# Construct the original array assuming the first element is 0:

# Iterate through the derived array using a loop:
# For each index i, calculate the next element in original as (derived[i] ^ original[i]) and append it to original.
# Check if the first and last elements of original are equal and store the result in checkForZero.

# Create an array original initialized with {1}.

# Construct the original array assuming the first element is 1:

# Iterate through the derived array using a loop:
# For each index i, calculate the next element in original as (derived[i] ^ original[i]) and append it to original.
# Check if the first and last elements of original are equal and store the result in checkForOne.

# Return the logical OR of checkForZero and checkForOne.

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        # Create an original array initialized with 0.
        original = [0]
        for i in range(len(derived)):
            original.append(derived[i] ^ original[i])

        # Store the validation results in checkForZero and checkForOne respectively.
        check_for_zero = original[0] == original[-1]
        original = [1]
        for i in range(len(derived)):
            original.append(derived[i] ^ original[i])
        check_for_one = original[0] == original[-1]

        return check_for_zero or check_for_one
    
# Complexity Analysis
# Let n be the size of the derived array.

# Time Complexity: O(n)

# The algorithm constructs the original array twice, once starting with original[0] = 0 and once with original[0] = 1. Each construction involves iterating through the derived array once, which takes O(n) time. Therefore, the overall time complexity is O(2⋅n)=O(n).

# Space Complexity: O(n)

# The algorithm uses an additional array original to store the intermediate results during its construction. The size of the original array is equal to the size of the derived array, requiring O(n) space. No other significant data structures are used, so the overall space complexity is O(n).