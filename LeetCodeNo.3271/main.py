class Solution:
    def stringHash(self, s: str, k: int) -> str:
        
        # 1. Divide s into n/k substrings.
        # 2. For each substring,
        #   sum, then % 26, ord then append to result.,

        n = len(s)
        m = n // k # # of substrings
        substrings = []
        results = ''
        for i in range(m):
            start = i * k
            end = start + k
            substrings.append(s[start:end])
        
        for sub in substrings:
            sub_sum = sum([ord(i) - ord('a') for i in sub])
            results += chr(sub_sum % 26 + ord('a'))
        # print(results)
        return results
        
s = Solution()
s.stringHash("ao", 1)
