class Solution:
    # This solves the problem, but too slow.
    def maximumSubarraySum_slow(self, nums: List[int], k: int) -> int:
        # Find all subarrays [start idx, end idx] that is good.
        sub_arrs = []
        for i in range(0, len(nums)):
            for j in range(i, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    sub_arrs.append([i, j])
        # Calc sum of all possible subarrays.
        sums = []
        for idx in sub_arrs:
            sums.append(sum(nums[idx[0]:idx[1]+1]))
        return max(sums) if sums else 0

    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum, prefix_sum, val_to_min_prefix_sum = -inf, 0, defaultdict(lambda: inf)
        for i, num in enumerate(nums):
            if val_to_min_prefix_sum[num] > prefix_sum:
                val_to_min_prefix_sum[num] = prefix_sum
            prefix_sum += num
            max_sum = max(max_sum, prefix_sum - val_to_min_prefix_sum[num + k], prefix_sum - val_to_min_prefix_sum[num - k])
        return max_sum if max_sum > -inf else 0 