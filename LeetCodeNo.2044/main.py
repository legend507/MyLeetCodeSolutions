class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # Create all possible subsets,
        # use a dict to store key = bitwise OR, value = [a subset].

        freq = {}
        # all_subsets = []
        def bitwise_or_of_list(lst):
            result = 0
            for num in lst:
                result |= num  # Apply bitwise OR with each element
            return result
        def backtrack(start, current_subset):
            # all_subsets.append(current_subset)
            bitwise_or = bitwise_or_of_list(current_subset)
            freq[bitwise_or] = freq.get(bitwise_or, 0) + 1
            for i in range(start, len(nums)):
                current_subset.append(nums[i])
                backtrack(i + 1, current_subset)
                current_subset.pop()

        backtrack(0, [])

        max_key = max(freq)
        return freq[max_key]
