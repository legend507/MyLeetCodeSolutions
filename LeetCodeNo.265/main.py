# There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.

# The cost of painting each house with a certain color is represented by an n x k cost matrix costs.

# For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on...
# Return the minimum cost to paint all houses.

 

# Example 1:

# Input: costs = [[1,5,3],[2,9,4]]
# Output: 5
# Explanation:
# Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5; 
# Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5.
# Example 2:

# Input: costs = [[1,3],[2,4]]
# Output: 5

# Editorial solution.
# It's a hard problem, don't even want to attemp it.
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        # Start by defining n and k to make the following code cleaner.
        n = len(costs)
        if n == 0: return 0 # No houses is a valid test case!
        k = len(costs[0])

        # If you're not familiar with lru_cache, look it up in the docs as it's
        # essential to know about.
        @lru_cache(maxsize=None)
        def memo_solve(house_num, color):

            # Base case.
            if house_num == n - 1:
                return costs[house_num][color]

            # Recursive case.
            cost = math.inf
            for next_color in range(k):
                if next_color == color:
                    continue # Can't paint adjacent houses the same color!
                cost = min(cost, memo_solve(house_num + 1, next_color))
            return costs[house_num][color] + cost

        # Consider all options for painting house 0 and find the minimum.
        cost = math.inf
        for color in range(k):
            cost = min(cost, memo_solve(0, color))
        return cost