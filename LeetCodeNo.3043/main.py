class Solution:
    def length_of_prefix(self, str1, str2):
        n = min(len(str1), len(str2))
        for i in range(n):
            if str1[i] != str2[i]:
                return i
        return n

    def longestCommonPrefix_tooSlow(self, arr1: list[int], arr2: list[int]) -> int:
        # My solution, but it's too slow.
        # make all int to string, and find their common prefixes.
        arr1.sort()
        arr2.sort()

        arr1_str = [str(i) for i in arr1]
        arr2_str = [str(i) for i in arr2]

        ret = 0
        for i in range(len(arr1_str)):
            for j in range(len(arr2_str)):
                prefix = self.length_of_prefix(arr1_str[i], arr2_str[j])
                ret = max(ret, prefix)
        return ret
    
    def bit_manipulation(self, int1, int2):
        while int1 != int2:
            if int1 > int2:
                int1 = int1 // 10
            else:
                int2 = int2 // 10
        return len(str(int1)) if int1 != 0 else 0
    
    def longestCommonPrefix_evenSlower(self, arr1: list[int], arr2: list[int]) -> int:
        arr1.sort()
        arr2.sort()
        ret = 0
        for i in arr1:
            for j in arr2:
                ret = max(ret, self.bit_manipulation(i, j))
        return ret
    
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        # Editorial solution. O(n+m)

        # 1. Build a set of all possible prefix from arr1.
        arr1_prefix = set()
        for i in arr1:
            while i not in arr1_prefix and i > 0:
                arr1_prefix.add(i)
                i = i // 10

        ret = 0

        # Do the same for arr2.
        for j in arr2:
            while j not in arr1_prefix and j > 0:
                j = j // 10
            # Found a prefix in arr2 that is in arr1_prefix.
            if j > 0:
                ret = max(ret, len(str(j)))
        return ret


s = Solution()
s.longestCommonPrefix([10], [17, 11])