class Solution:
    def minimumSteps(self, s: str) -> int:
        # Editorial solution. Need to understand this.
        white_position = 0
        total_swaps = 0

        # Iterate through each ball in the string
        for current_pos, char in enumerate(s):
            if char == "0":
                # Calculate the number of swaps needed
                total_swaps += current_pos - white_position

                # Move the next available position for a white ball one step to the right
                white_position += 1

        return total_swaps