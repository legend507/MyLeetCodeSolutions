class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # 10 = 1010
        # 7  = 0111
        # Want 1101

        # Bin gives an int's binary representation in string format.
        start_bin = bin(start)[2:]
        goal_bin = bin(goal)[2:]
        print(start_bin, goal_bin)
        start_ptr, goal_ptr = len(start_bin) - 1, len(goal_bin) - 1
        flip = 0
        while start_ptr >= 0 and goal_ptr >= 0:
            if start_bin[start_ptr] != goal_bin[goal_ptr]:
                flip += 1
            start_ptr -= 1
            goal_ptr -= 1
        # Need to flip more bit on the left from 0 -> 1 to match with goal.
        if start_ptr < 0 and goal_ptr >=0:
            while goal_ptr >= 0:
                if goal_bin[goal_ptr] == "1":
                    flip += 1
                goal_ptr -= 1
        elif start_ptr >= 0 and goal_ptr < 0:
            # Need to flip bit on the left from 1 to 0.
            while start_ptr >= 0:
                if start_bin[start_ptr] == "1":
                    flip += 1
                start_ptr -= 1
        return flip
    
    def minBitFlips_Better(self, start: int, goal: int) -> int:
        count = 0
        while start > 0 or goal > 0:
            # Increment count if the current bits differ
            if (start & 1) != (goal & 1):
                count += 1
            # Shift both numbers to the right to check the next bits
            start >>= 1
            goal >>= 1
        return count



s = Solution()
s.minBitFlips(10, 7)