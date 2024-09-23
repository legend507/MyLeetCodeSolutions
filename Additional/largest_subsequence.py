# Given a sequence S of N digits, find a subsequence of K digits such that the number formed by these K digits (in order) is the largest.

# Examples

# S = 4902, K = 2, answer = 92
# S = 4902, K = 3, answer = 902
# S = 142857, K = 1, answer = 8
# S = 142857, K = 2, answer = 87
# S = 142857, K = 4, answer = 4857

# Key Idea:
# Traverse the digits of S one by one.
# Use a stack to keep the largest subsequence possible.
# If a smaller digit is in the stack and a larger digit comes later (and we still have enough digits left), pop the smaller digit.
# Continue this process until we have selected exactly K digits.

def largest_subsequence(S, K):
    # Convert the sequence S to a string to handle digits easily
    S = str(S)
    stack = []
    n = len(S)
    to_remove = n - K  # The number of digits we can remove to keep K digits

    for digit in S:
        # Ensure we have the largest possible digits in the stack
        while to_remove > 0 and stack and stack[-1] < digit:
            stack.pop()  # Remove the smaller digits
            to_remove -= 1
        stack.append(digit)

    # The result is the first K digits from the stack
    return ''.join(stack[:K])

# Example usage:
S1 = 4902
K1 = 2
print(largest_subsequence(S1, K1))  # Output: "92"

S2 = 4902
K2 = 3
print(largest_subsequence(S2, K2))  # Output: "902"

S3 = 142857
K3 = 1
print(largest_subsequence(S3, K3))  # Output: "8"

S4 = 142857
K4 = 2
print(largest_subsequence(S4, K4))  # Output: "87"

S5 = 142857
K5 = 4
print(largest_subsequence(S5, K5))  # Output: "4857"
