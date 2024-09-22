import re
import math

class Solution:
    def least_common_multiple(self, x, y):
        return (x*y) // math.gcd(x, y)
    
    def lcm_of_list(self, nums):
        result = nums[0]
        for i in range(1, len(nums)):
            result = self.least_common_multiple(result, nums[i])
        return result

    def fractionAddition(self, expression: str) -> str:
        # Solved this on my own, but with tons of google.


        numerators = []
        denominators = []
        signs = []
        for i in expression:
            if i == '-' or i == '+':
                signs.append(i)
        if expression[0] != '-':
            signs = ['+'] + signs

        # get all numbers from expression, by spliting based on multiple deliminators.
        numbers = re.split('\+|\-|\/', expression)
        if '' in numbers:
            numbers.remove('')

        for i, value in enumerate(numbers):
            if i % 2 == 0:
                numerators.append(int(value))
            else:
                denominators.append(int(value))

        lcm = self.lcm_of_list(denominators)

        for i in range(len(numerators)):
            numerators[i] = int(numerators[i] * lcm / denominators[i])
        
        print(numerators, denominators, signs)

        n = len(numerators)
        up = 0
        down = 0
        for i in range(n):
            if signs[i] == '-':
                up -= numerators[i]
            else:
                up += numerators[i]
        gcd = math.gcd(up, lcm)
        return str(int(up / gcd)) + '/' + str(int(lcm / gcd))

s = Solution()

print(s.fractionAddition('1/3-1/2'))