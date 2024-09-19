class Solution:
    # My solution, used try-except. but quit slow.
    def twoSum_my(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            to_find = target - numbers[i]
            try:
                idx = numbers.index(to_find, i+1, n)
                return [i+1, idx+1]
            except:
                continue
        return [-1, -1]

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Editorial solution.
        low = 0
        high = len(numbers) - 1
        while low < high:
            sum = numbers[low] + numbers[high]

            if sum == target:
                return [low + 1, high + 1]
            elif sum < target:
                low += 1
            else:
                high -= 1
        # In case there is no solution, return [-1, -1].
        return [-1, -1]