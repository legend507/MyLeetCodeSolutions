class Solution:
    def sameEndSubstringCount_tooSlow(self, s: str, queries: List[List[int]]) -> List[int]:
        # Check how many same-end substrings are in each query_answer.
        # This is too slow.
        def count_same_end_string(subs):
            count = 0
            for i in range(len(subs)):
                for j in range(i+1, len(subs)):
                    if subs[i] == subs[j]:
                        count += 1
            return count + len(subs)
        
        # x * (x+1) / 2.
        # E.g. a then 1, aa then 3, aaa then 6, aaaa then 10, ...
        # Still too slow...
        def count_same_end_string_maths(subs):
            freq = {}
            for i in subs:
                freq[i] = freq.get(i, 0) + 1

            ret = 0
            for key, value in freq.items():
                ret += value * (value + 1) // 2
            return ret

        ret = []
        for query in queries:
            query_answer = (s[query[0]:query[1]+1])
            ret.append(count_same_end_string_maths(query_answer))
        return ret
    
    def sameEndSubstringCount(self, s: str, queries: List[List[int]]) -> List[int]:
        # Editorial solution.
        
        n = len(s)
        # 2D list to store prefix sum of character frequencies for each character 'a' to 'z'
        char_freq_prefix_sum = [[0] * n for _ in range(26)]

        # Fill the frequency array
        for i, char in enumerate(s):
            char_freq_prefix_sum[ord(char) - ord("a")][i] += 1

        # Convert the frequency array into a prefix sum array
        for freq in char_freq_prefix_sum:
            for j in range(1, n):
                freq[j] += freq[j - 1]

        results = []

        # Process each query
        for left_index, right_index in queries:
            count_same_end_substrings = 0

            # For each character, calculate the frequency of occurrences within the query range
            for freq in char_freq_prefix_sum:
                left_freq = 0 if left_index == 0 else freq[left_index - 1]
                right_freq = freq[right_index]
                frequency_in_range = right_freq - left_freq

                # Calculate the number of same-end substrings for this character
                count_same_end_substrings += (
                    frequency_in_range * (frequency_in_range + 1) // 2
                )

            results.append(count_same_end_substrings)

        return results
