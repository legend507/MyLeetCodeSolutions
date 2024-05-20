from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        # 2 choises for each number: 1. included in the subset, 2. not inlucded in the subset.

        # i: index .
        def create_subset(i):
            if i == len(nums):
                # When reach the end of original list, but the current subset to the result.
                # [:] all element in a list.
                res.append(subset[:])
                return
            
            # Create a subset with the current number in the subset.
            subset.append(nums[i])
            create_subset(i+1)

            # Create a subset with the current number not in the subset.
            subset.pop()
            create_subset(i+1)

        create_subset(0)
        return res
    