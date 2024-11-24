# You are given an m x n integer matrix grid containing distinct positive integers.

# You have to replace each integer in the matrix with a positive integer satisfying the following conditions:

# The relative order of every two elements that are in the same row or column should stay the same after the replacements.
# The maximum number in the matrix after the replacements should be as small as possible.
# The relative order stays the same if for all pairs of elements in the original matrix such that grid[r1][c1] > grid[r2][c2] where either r1 == r2 or c1 == c2, then it must be true that grid[r1][c1] > grid[r2][c2] after the replacements.

# For example, if grid = [[2, 4, 5], [7, 3, 9]] then a good replacement could be either grid = [[1, 2, 3], [2, 1, 4]] or grid = [[1, 2, 3], [3, 1, 4]].

# Return the resulting matrix. If there are multiple answers, return any of them.

class Solution:
    def minScore(self, grid: List[List[int]]) -> List[List[int]]:
        row, col = len(grid), len(grid[0])

        nums = []
        # Create rows and cols to store the minimum values for every row and column.
        rows = [1 for i in range(row)]
        cols = [1 for i in range(col)]

        # Create a matrix nums that stores the values of the matrix and their indices.
        for i in range(row):
            for j in range(col):
                nums.append((grid[i][j], i, j))

        nums.sort()
        for tup in nums:
            _, i, j = tup
            # Find the maximum value of rows[i] and cols[j] till now and assign it to val.
            val = max(rows[i], cols[j])
            grid[i][j] = val
            # Update the new maximum value in rows[i] and cols[j].
            rows[i], cols[j] = val + 1, val + 1
        return grid
    