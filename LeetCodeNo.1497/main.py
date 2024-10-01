# 1497. Check If Array Pairs Are Divisible by k

# Didn't solve this.
# Editorial solution.

class Solution:
    def canArrange(self, arr, k):
        remainder_count = {}

        # Store the count of remainders in a map.
        for i in arr:
            remainder_count[(i % k + k) % k] = (
                remainder_count.get((i % k + k) % k, 0) + 1
            )

        for i in arr:
            rem = (i % k + k) % k

            # If the remainder for an element is 0, then the count of numbers that give this remainder must be even.
            if rem == 0:
                if remainder_count[rem] % 2 == 1:
                    return False

            # If the remainder rem and k-rem do not have the same count then pairs can not be made.
            elif remainder_count[rem] != remainder_count.get(k - rem, 0):
                return False
        return True
    
# Algorithm
# Create a hashmap remainderCount to store the count of remainders when dividing elements of arr by k.
# Iterate through the array arr:
#   For each element i, compute the remainder as (x % k + k) % k to handle both positive and negative values.
#   Increment the count of this remainder in remainderCount.
# Iterate through the array arr again:
#   For each element i, compute the remainder as (i % k + k) % k.
#   If the remainder is 0, check if the count of this remainder in remainderCount is even:
#       If it is odd, return false (no valid pairs).
#   For all other remainders rem, check if the count of rem is equal to the count of k - rem:
#       If they are not equal, return false (no valid pairs).
# If all checks pass, return true (valid pairs can be made).