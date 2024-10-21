nums = 'stri'
def generate_all_subsets(nums):
    all_subsets = []
    def backtrack(start, current_subset):
        # Need to use copy() here.
        all_subsets.append(current_subset.copy())
        for i in range(start, len(nums)):
            current_subset.append(nums[i])
            backtrack(i + 1, current_subset)
            current_subset.pop()

    backtrack(0, [])
    return all_subsets
print(generate_all_subsets(nums)) # Output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]