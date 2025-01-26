# You are given a 0-indexed matrix grid of order n * n. Each cell in this matrix has a value grid[i][j], which is either a positive integer or -1 representing a blocked cell.

# You can move from a non-blocked cell to any non-blocked cell that shares an edge.

# For any cell (i, j), we represent its remoteness as R[i][j] which is defined as the following:

# If the cell (i, j) is a non-blocked cell, R[i][j] is the sum of the values grid[x][y] such that there is no path from the non-blocked cell (x, y) to the cell (i, j).
# For blocked cells, R[i][j] == 0.
# Return the sum of R[i][j] over all cells.

# Solution
# Overview
# The problem requires calculating the remoteness for each cell in a grid. The remoteness of a cell is defined as the sum of all values in the grid that are not reachable from that cell. Finally, we need to compute the total remoteness of all cells in the grid.

# There are two main observations we can make from the remoteness and not reachable criteria, as shown below:

# Reachable vs. Unreachable Cells

# The sum of all cells reachable from a given cell is simply the total sum of all cells in the grid minus the sum of all unreachable cells. Thus, for any cell, its remoteness can be expressed as: remoteness=total_sum−reachable_sum

# Isolated Islands in the Grid

# The grid can be thought of as containing multiple "islands" of connected cells, separated by blocked cells (-1). Within each island, all cells are mutually reachable. As a result, the remoteness for all cells in the same island will be identical because they share the same set of reachable and unreachable cells.

# Thus, from these observations, we can conclude that instead of calculating the remoteness for each cell individually, we only need to compute it once per connected component (island).

# Approach 1: Depth-First Search (DFS)
# Intuition
# First, we need to find the sum of cells within each connected component. For that, we need to figure out a way to traverse over an entire component and keep track of its size and sum of values simultaneously.

# A very popular algorithm to traverse over a grid is the Depth-First Search (DFS) 🔗 algorithm. DFS works by starting at one cell and exploring as far as possible along each branch before backtracking.

# Let's define a recursive Depth-First Search function dfs. In DFS we need to calculate two key pieces of information for each component:

# The sum of all cell values in the component.
# The count of reachable cells in the component.
# To find this, we'll use a helper array arr where arr[0] stores the sum of the values of the cells visited during the DFS traversal and arr[1] stores the number of cells visited, i.e., the size of the connected component.

# During each recursive call, we update arr by adding the current cell's value and increasing the cell count. To prevent revisiting cells, we mark each explored cell as visited by changing its value to -1. The function then recursively calls itself to explore all valid neighboring cells that are neither blocked nor previously visited.

# Once DFS completes for a connected component, we can calculate the remoteness for all cells in that component using the formula: remoteness=(sum of all grid cells)−(sum of cells in the current component)

# This gives us the remoteness of each cell in the component. Since all cells in the component share the same set of reachable and unreachable cells, we multiply the remoteness by the number of cells in that component to get the total remoteness contribution of that component.

# Once we've explored the entire grid and called DFS on all connected components, the result will contain the final sum of remoteness values for all cells in the grid.

# Algorithm
# Initialize a direction array dir containing four pairs of integers to represent the four possible movement directions, right: (0,1), left: (0,-1), down: (1,0), up: (-1,0).
# Main Method sumRemoteness:

# Initialize a variable:

# n to store the length of the grid (assuming it's a square grid).
# totalSum to 0 for accumulating the sum of all non-blocked cells.
# Iterate through each cell in the grid:

# If the cell value is not -1 (not blocked), add its value to totalSum.
# Initialize a variable result to 0 that will store the final sum of all remoteness values.

# For each cell (row, col) in the grid:

# Check if its value is greater than 0 (indicating it is a valid, non-blocked cell). If so:
# Create an array arr of size 2 to store:
# arr[0]: Running sum of all cells reachable from the current cell.
# arr[1]: Count of how many cells are reachable from the current cell.
# Perform DFS starting from this cell to populate arr.
# Calculate the unreachable sum as totalSum - arr[0].
# Multiply the unreachable sum by the count of reachable cells (arr[1]) and add this value to result.
# Return the final result.

# Helper method dfs(grid, row, col, arr):

# Add the current cell's value to the running sum in arr[0].
# Increment the reachable cells counter in arr[1].
# Mark the current cell as visited by changing its value to -1.
# For each of the four possible directions:
# Calculate the new coordinates by adding the direction offsets.
# If the new coordinates are valid (using the isValid function), recursively call dfs on them.
# Helper method isValid(grid, row, col):

# Return true if:
# The row index row is between 0 and n - 1 (inclusive).
# The column index col is between 0 and n - 1 (inclusive).
# The cell at (row, col) has a value greater than 0 (not blocked or visited).

class Solution:
    def sumRemoteness(self, grid: list[list[int]]) -> int:
        # Direction arrays for moving up, down, left, right
        self.dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        n = len(grid)

        # Calculate total sum of all non-blocked cells
        total_sum = sum(val for row in grid for val in row if val != -1)

        # Calculate remoteness for each non-blocked cell
        result = 0
        for row in range(n):
            for col in range(n):
                if grid[row][col] > 0:
                    # arr[0] = sum of reachable cells
                    # arr[1] = count of reachable cells
                    arr = [0, 0]
                    self._dfs(grid, row, col, arr)
                    result += (total_sum - arr[0]) * arr[1]

        return result

    # DFS to find sum and count of all cells reachable from (row, col)
    def _dfs(
        self, grid: list[list[int]], row: int, col: int, arr: list
    ) -> None:
        arr[0] += grid[row][col]  # Add current cell value to sum
        arr[1] += 1  # Increment reachable cells count
        grid[row][col] = -1  # Mark as visited

        # Explore all 4 directions
        for di, dj in self.dir:
            new_row, new_col = row + di, col + dj
            if self._is_valid(grid, new_row, new_col):
                self._dfs(grid, new_row, new_col, arr)

    # Checks if cell (row, col) is within grid bounds and not blocked/visited
    def _is_valid(self, grid: list[list[int]], row: int, col: int) -> bool:
        n = len(grid)
        return 0 <= row < n and 0 <= col < n and grid[row][col] > 0