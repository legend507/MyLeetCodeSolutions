from collections import OrderedDict

class Solution:
    def __init__(self) -> None:
        self.nums_dict = {}
    def find_next_bigger(self, this_key):
        for key, value in self.nums_dict.items():
            if key > this_key and value > 0:
                return key
        return None
    def maximizeGreatness_slow(self, nums: List[int]) -> int:
        # Thoughts:
        # 1. use a dict, key = num in nums, value = times of occurance.
        # 2. for num in nums, find the next bigger key in dict.
        
        # Solves the problem, but time limit exceeded.

        for one_num in nums:
            if one_num in self.nums_dict:
                self.nums_dict[one_num] += 1
            else:
                self.nums_dict[one_num] = 1
        nums.sort()

        # Sort nums_dict by key ASEC.
        self.nums_dict = OrderedDict(sorted(self.nums_dict.items()))
        # print(self.nums_dict)
        ret = 0
        for one_num in nums:
            key = self.find_next_bigger(one_num)
            # print(f'for {one_num}, use {key}')
            if key != None:
                ret += 1
                self.nums_dict[key] -= 1
        return ret

    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        for num in nums:
            # Compare 
            if nums[ans] < num:
                ans += 1
        return ans