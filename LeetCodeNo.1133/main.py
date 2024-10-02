# 1133. Largest Unique Number

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        store = {}
        for num in nums:
            store[num] = store.get(num, 0) + 1
        
        ret = -1
        for key, value in store.items():
            if value == 1:
                ret = max(ret, key)
        return ret


