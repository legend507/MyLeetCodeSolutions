# You're given an array of integers. Please find the length of the longest contiguous non-decreasing subarray.

# For example, the array could be: [1, 7, 7, 2, 3, 6, 7, 0, 8, 2, 4, 9, 8, -20]. And the longest contiguous non-decreasing subarray is [2, 3, 6, 7]

# Follow Up Question #1: Can substituting value at a single point
# Now, you can choice a single point on the original array and change the number of that point to any value you want.

# For example, the array could be: [2, 3, 4, 7, 0, 8, 2, 4, 9, 6]. If you change the 8 number (at index 6) to 1, you can create a contiguous non-decreasing subarray like [0, 1, 2, 4, 9] with length of 5.

# But is this the maximum length?

# Follow Up Question #2: Can substituting all elements of a specific value to another value in existence
# This time, you're allowed to perform one operation to substituting all elements of a specific value to another value in existence.

# For example, change All 8s to 0s.

# Then [7, 0, 8, 2, 4, 7, 8, -20] can become [7, 0, 0, 2, 4, 7, 0, -20] and you will get a contiguous non-decreasing subarray like [0, 0, 2, 4, 7]






# Main question
# Ask TC to provide some examples to make sure they really understand what we want.

# It shouldn't take too much time to solve once TC understand the goal.

# Follow up question 1
# With a brief observation, TC should be able to identify that the key point is where the numbers start decreasing, but how to properly maintain these points is challenging. This problem is a great test of programming, if TC can come up with an elegant and simple solution, it would be a great signal.

# This question doesn't require advanced data structures or algorithms.

# When using an algorithm or data structure, one should always ask what the benefit is vs a naive solution. Depending on what you're optimizing, it should either make the code more efficient or more readable and maintainable.

# If candidates start using data structures and algorithms simply because they assume nothing else is possible, that's not ideal.

# Follow up question 2
# Since changing a value will affect multiple places, it will be a little tricky to see how to choose the correct number to substitute.

# If TC said it's almost the same as follow up question 1. Let them try test case [1,2,1,2,1,2,1,2] and [1,3,3,2,2,4]

# The brute-force solution is try every possible substitution, in that case, if we have M different values, it will be O(M^2) pairs to try and each take O(N) to check. The overall time complexity will be (N*M^2) or O(N^3).

# With careful observation, we can define the place where value drop as breakpoint. For example [1,3,5,2,8,9,1,10] have two breakpoints at index 3 and 6.

# It should become clear that the substitution pair we need to try are only the number at breakpoint and the one left. For above example, it will be [5,2], [2,5] and [9,1], [1,9]

# This reduces the possibilities of substitution to O(M), and overall time complexity to O(N*M) or O(N^2). The correctness of this approach is worth discussing thoroughly. If TC can provide a good explanation, this implementation is actually easier than follow-up question 1. A good challenge will be try to solve it with only O(1) extra space.

# If TC is good and still have lots of time here, we go to the actual interesting (and difficult) part of the problem. How can we solve this question better than O(N^2) time complexity?

# The core idea is try to expand the possible subarray for each breakpoint, and during the expansion, if it already cover some other breakpoints, record them properly or delete them from the list to try. In that case, we can assume that we will only search each possible interval one time, at most twice.

# There are several different ways to achieve this (e.g. sliding window), but all of them are hard to implementation correctly. And prove the runtime is O(N) could also be challenging. I didn't anticipate candidate to actually solve it that way.

# Another good approach is using binary search to find the maximum possible subarray length. Because we can guarantee that if there exists a non-decreasing contiguous subarray of length K, then all non-decreasing contiguous subarrays of lengths smaller than K must also exist. Therefore, we can attempt a binary search on this length.

# For each length candidate, we can perform a fixed-length sliding window operation, and handle it based on how many breakpoints exist within this window. If none exist, we return True, and if there is more than one type of breakpoints, we return False. For cases with only one type of breakpoint, we check if it can be resolved through substitution to make it True.

# This way, the time complexity will be O(NlogN) instead of O(N), but still much better than O(N^2). The implementation is relatively easier and has a chance of being completed during an interview, although it's still quite challenging.

# Python

"""
Sample solution of main question
"""
def main_question(arr):
  """No substitution."""

  cnt = 0
  cur = -math.inf
  ans = 0
  for i in range(len(arr)):
    if arr[i] >= cur:
      cnt += 1
    else:
      cnt = 1

    ans = max(ans, cnt)
    cur = arr[i]

  return ans

"""
Sample solution of follow-up question 1
"""
def follow_up_1(arr):
  """Can substitution at one point."""

  breakpoints = [0]
  for i in range(1, len(arr)):
    if arr[i] < arr[i - 1]:
      breakpoints.append(i)
  breakpoints.append(len(arr))

  # If there are no break points in the middle of array, it means the array is
  # already non-decreasing, just return the answer of main question.
  if len(breakpoints) == 2:
    return main_question(arr)

  ans = 0
  for bp_id in range(1, len(breakpoints) - 1):
    bp = breakpoints[bp_id]
    left_len = breakpoints[bp_id] - breakpoints[bp_id - 1]
    right_len = breakpoints[bp_id + 1] - breakpoints[bp_id]

    def can_merge(arr, i):
      if i != 0 and i != len(arr) - 1:
        return arr[i - 1] <= arr[i + 1]
      return False

    # If change the single elemant at point bp or bp - 1 can make the left
    # and right segment merge together, then we can return the sum of left and
    # right segment.
    if can_merge(arr, bp) or can_merge(arr, bp - 1):
      ans = max(ans, left_len + right_len)

    # If we can't merge the two segments together, but we can still substitute
    # one element in the left or right segment to add one more element.
    # Note that if there is only one element in the original arr, it means
    # we don't have any break point at all and this case should already be
    # handled above by the solution of main question.
    ans = max(ans, left_len + 1, right_len + 1)

  return ans

"""
Sample solution of follow-up question 2
"""

def follow_up_2(arr):
  """Substitute all elements with a specific value to another value.

  Here we provide a solution with O(N^2) time complexity. For O(N) and O(NlogN)
  solution
  """

  swaps = []
  for i in range(1, len(arr)):
    if arr[i] < arr[i - 1]:
      swaps.append((arr[i], arr[i - 1]))
      swaps.append((arr[i - 1], arr[i]))

  if not swaps:
    return main_question(arr)

  # It's basically the main question with an additional value swap requirement.
  def helper(arr, swap):
    """Longest non-decreasing subsequence."""
    cnt = 0
    cur = -math.inf
    ans = 0
    for i in range(len(arr)):
      # swap value if needed
      num = arr[i]
      if num == swap[0]:
        num = swap[1]

      if num >= cur:
        cnt += 1
      else:
        cnt = 1

      ans = max(ans, cnt)
      cur = num

    return ans

  ans = 0
  for swap in swaps:
    ans = max(ans, helper(arr, swap))

  return ans