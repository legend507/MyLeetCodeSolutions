from functools import cmp_to_key

def compare(x:str, y:str):
    # Define my own sort function.
    if x[0] > y[0]:
        return 1
    elif x[0] < y[0]:
        return -1
    else:
        # x[0] == y [0]
        # convert back to int, and try xy and yx, see which one is bigger.
        if int(x+y) > int(y+x):
            return 1
        else:
            return -1

class Solution:
   
    def largestNumber(self, nums: List[int]) -> str:
        # str all nums, then order them desc, then concate everything.
        # reason being, str when ordered desc, '9' should always comes first.
        nums_str = [str(i) for i in nums]
        nums_str = sorted(nums_str, reverse=True, key=cmp_to_key(compare))
        print(nums_str)
        
        ret = ''
        for i in nums_str:
            ret += i
        return str(int(ret))