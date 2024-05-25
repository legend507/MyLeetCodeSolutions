class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        # nums = [2,4,6]
        # k = 2
        # [], [2], [4], [6], [2, 4], [2, 6], [4, 6], [2, 4, 6]
        # [2], [4], [6], [2, 6] -> 4 ans
        # SOLUTION
        # num - k or n + k

        count = 0
        lenNums = len(nums)

        # Recursive, 
        def explore(index):
            # Needs this to use count var in nested function.
            nonlocal count

            # Reaches the end of nums.
            if lenNums == index:
                count += 1
                return

            # Current num in the recursive.
            num = nums[index]

            # Key of visited dict is the num in nums.
            # If num-k and num+k hasn't been added to the current subset.
            if num - k not in visited and num + k not in visited:
                visited[num] += 1
                # Continue constructing current subset, untill reach end of nums.
                explore(index + 1)
                visited[num] -= 1

                if visited[num] == 0:
                    # Deletes the corresponding key in dict.
                    del visited[num]

            # There is already num-k or num+k in current subset. Move on to next num in nums.
            explore(index + 1)

        # Regular dictionaries: When you try to access a key that doesn't exist in a normal dictionary, you'll get a KeyError. This can disrupt your program's flow.
        # defaultdict:  It provides a way to specify a default value that gets assigned to the key if it's not found in the dictionary. This eliminates KeyError and allows your code to continue smoothly.
        visited = defaultdict(int)
        explore(0)
        return count - 1
    
    
    # My solution, works but way too slow.
    def beautifulSubsets_my(self, nums: List[int], k: int) -> int:
        subset = []
        all_subsets = []
        
        # Creates all possible subsets.
        def create_subset(i):
            if i == len(nums):
                # When reach the end of original list, but the current subset to the result.
                # [:] all element in a list.
                all_subsets.append(subset[:])
                return
            
            # Create a subset with the current number in the subset.
            subset.append(nums[i])
            create_subset(i+1)

            # Create a subset with the current number not in the subset.
            subset.pop()
            create_subset(i+1)

        # Traverse all subsets, check for absolute.
        def count_beautiful():
            result = 0
            for oneset in all_subsets:
                if 0 != len(oneset):
                    valid = True
                    for i in oneset:
                        if (i+k in oneset) or (i-k in oneset):
                            valid = False
                            break
                    if valid:
                        result += 1
            return result
        
        create_subset(0)
        return count_beautiful()
                    




