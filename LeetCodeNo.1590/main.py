class Solution:
    def minSubarray_tooSlow(self, nums: List[int], p: int) -> int:
        # Corner case
        if sum(nums) % p == 0:
            return 0

        # Sum of nums. To figure out the % and //.
        current_sum = sum(nums)
        to_remove = current_sum % p
        divide = current_sum // p
        # A list of all possible sums of sub array to remove from nums.
        all_possible_sub_sums = [to_remove + p*i for i in range(0, divide)]

        n = len(nums)

        # Loop all possible length.
        for current_len in range(n):
            # From i, remove current_len of subarry.
            # Calculate their sum, and check if the sum in all_possible_sub_sums.
            for i in range(n):
                current_sub = sum(nums[i:i+current_len])
                if current_sub in all_possible_sub_sums:
                    return current_len
        return -1
    
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        total_sum = 0

        # Step 1: Calculate total sum and target remainder
        for num in nums:
            total_sum = (total_sum + num) % p

        target = total_sum % p
        if target == 0:
            return 0  # The array is already divisible by p

        # Step 2: Use a dict to track prefix sum mod p
        mod_map = {
            0: -1
        }  # To handle the case where the whole prefix is the answer
        current_sum = 0
        min_len = n

        # Step 3: Iterate over the array
        for i in range(n):
            current_sum = (current_sum + nums[i]) % p

            # Calculate what we need to remove
            needed = (current_sum - target + p) % p

            # If we have seen the needed remainder, we can consider this subarray
            if needed in mod_map:
                min_len = min(min_len, i - mod_map[needed])

            # Store the current remainder and index
            mod_map[current_sum] = i

        # Step 4: Return result
        return -1 if min_len == n else min_len
