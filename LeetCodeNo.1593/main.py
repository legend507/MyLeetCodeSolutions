class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        # Editorial solution.
        # Need to remember the backtrack() function. This is useful when
        # I need to split a string (or a list) to substrings, 
        # without reusing the same element.
        seen = set()

        def backtrack(input, start, seen):
            # End condition.
            if start == len(input):
                return 0
            
            max_count = 0
            for end in range(start+1, len(input) + 1):
                sub_str = input[start:end]
                if sub_str not in seen:
                    seen.add(sub_str)
                    max_count = max(max_count, 1+ backtrack(input, end, seen))
                    seen.remove(sub_str)

            return max_count
        
        return backtrack(s, 0, seen)