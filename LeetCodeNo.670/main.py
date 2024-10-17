class Solution:
    def maximumSwap(self, num: int) -> int:
        # Thoughs:
        # 1. Split the num to each char.
        # 2. 2 for loops, compare if I should swap. If so, swap and save the new num to all_candidates.
        # 3. Find max in the all_candidates list.
        num_str = [i for i in str(num)]
        all_candidates = []

        # Create all possible swaps.
        for i in range(len(num_str)):
            for j in range(i+1, len(num_str)):
                if num_str[i] < num_str[j]:
                    new_num_str = num_str.copy()
                    new_num_str[j] = num_str[i]
                    new_num_str[i] = num_str[j]
                    all_candidates.append(int(''.join(new_num_str)))
        return max(all_candidates) if all_candidates else num
