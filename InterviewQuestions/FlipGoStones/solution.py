# Q1.
# Reference: https://www.geeksforgeeks.org/maximize-number-0s-flipping-subarray/

# The stupid way is to use 2 loops O(n**2).
# The smart way is to reduce this problem into a
# "largest subarray sum problem".

# This smart solution tries to figure out max 0 we can get by flipping a subarray.
def flip(arr):
  n = len(arr)
  start = 0
  end = 0

  orig_zero_count = 0

  max_diff = 0

  curr_max = 0

  for i in range(n):

    # Count of 0s in the original array.
    if arr[i] == 0:
      orig_zero_count += 1

    # If I flip arr[i], how many 0s we can get.
    # This means I always try to flip arr[i].
    val = 1 if arr[i] == 1 else -1

    # curr_max records all flips so far. It can never < 0.
    # If curr_max reaches 0, it means the flips so far 
    # contributes no extra 0s.
    if val >= curr_max + val:
      this_start = i
    curr_max = max(val, curr_max + val)

    # max_diff records the max of curr_max seen so far.
    if curr_max > max_diff:
      start = this_start
      end = i
    max_diff = max(max_diff, curr_max)

  max_diff = max(0, max_diff)

  # (max_0s, (flip_start, flip_end))
  return (orig_zero_count + max_diff, (start, end))

arr = [ 0, 1, 0, 0, 1, 1, 0 ]
print(flip(arr))


# Q2: Dynamic programming.