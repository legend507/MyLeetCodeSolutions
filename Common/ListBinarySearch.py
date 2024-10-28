# Binary search helper function to efficiently find a value in the sorted array.
# Time complexity: O(log n).
# list.sort() has complexity of O(nlogn).
# quick search works on un-sorted array too, and has complexity of O(n).

def binary_search(nums: list[int], target: int) -> bool:
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return True
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False