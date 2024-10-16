class Solution:
    def maxKelements_tooSlow(self, nums: List[int], k: int) -> int:
        operations = 0
        score = 0
        while operations < k:
            operations += 1
            max_nums = max(nums)
            max_idx = nums.index(max_nums)
            score += max_nums
            nums[max_idx] = ceil(nums[max_idx] / 3)
        return score

    def maxKelements(self, nums: List[int], k: int) -> int:
        # Editorial solution.
        # By default, heapq is ascending order. To make it descending,
        # I can add a - sign to the number.
        ans = 0
        max_heap = []

        # Add elements one by one into the max-heap
        for num in nums:
            heapq.heappush(max_heap, -num)

        while k > 0:
            k -= 1
            # Retrieve the max element (invert the sign because it's stored as negative)
            max_element = -heapq.heappop(max_heap)
            ans += max_element
            # Add one-third of the max element back to the heap. Rounded up using integer division.
            heapq.heappush(max_heap, -math.ceil(max_element / 3))

        return ans
