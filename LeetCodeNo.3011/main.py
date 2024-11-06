class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)
        # Check if nums is already sorted.
        if sorted(nums) == nums:
            return True

        # Traverse all num in nums, record each num's set bits.
        record = []
        for num in nums:
            binary = bin(num)
            count_1s = binary.count('1')
            record.append(count_1s)
        # print(record)
        # Split nums in to subgroups based on their set bits.
        nums_split = []
        current_set_bit = record[0]
        current_split = []
        for i in range(n):
            if current_set_bit == record[i]:
                current_split.append(nums[i])
            else:
                nums_split.append(current_split.copy())
                current_set_bit = record[i]
                current_split = [nums[i]]
        if current_split:
            nums_split.append(current_split)
        
        # For each subgroup, check max / min.
        former_max = max(nums_split[0])
        for i in range(1, len(nums_split)):
            current_max = max(nums_split[i])
            current_min = min(nums_split[i])
            if former_max > current_min:
                return False
            former_max = current_max
        return True
