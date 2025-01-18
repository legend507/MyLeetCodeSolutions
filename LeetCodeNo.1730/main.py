# You are starving and you want to eat food as quickly as possible. You want to find the shortest path to arrive at any food cell.

# You are given an m x n character matrix, grid, of these different types of cells:

# '*' is your location. There is exactly one '*' cell.
# '#' is a food cell. There may be multiple food cells.
# 'O' is free space, and you can travel through these cells.
# 'X' is an obstacle, and you cannot travel through these cells.
# You can travel to any adjacent cell north, east, south, or west of your current location if there is not an obstacle.

# Return the length of the shortest path for you to reach any food cell. If there is no path for you to reach food, return -1.

# Approach 1: Breadth-First Search (BFS)
# Intuition
# Our task is to find the distance to the closest food cell from the starting cell among all the food cells present in the grid. Imagine the starting cell as the origin point, with "explorers" sent out to neighboring cells in all four directions: up, down, left, and right. This exploration happens in layers, where each layer represents a step farther from the starting point:

# Layer 0: The starting cell.
# Layer 1: The cells adjacent to the starting cell.
# Layer 2: The cells two steps away, and so on.
# This systematic exploration is called Breadth-First Search (BFS). BFS explores cells layer by layer, so when a food cell is found, it is guaranteed to be the closest one because all cells at shorter distances are processed first. This property makes BFS optimal for finding the shortest path in an unweighted grid. Think of it like ripples spreading out from a stone dropped in water - each ripple represents how far we've searched from the starting point.

# Algorithm
# Initialize a constant array of directions dir representing the possible moves: right (0,1), left (0,-1), up (-1,0), and down (1,0).
# Main method getFood:

# Initialize variables rows and cols to store the dimensions of the input grid.
# Create a start array with -1 values to store the coordinates of the starting position.
# Iterate through the grid to find the cell marked with '*':
# When found, store its coordinates in the start array.
# Initialize a queue data structure to perform BFS traversal.
# Add the start position to the queue.
# Initialize a variable steps to 1 to track the distance traveled.
# Begin the BFS traversal while the queue is not empty:
# Store the current level size of the queue.
# Process all cells at the current level:
# Remove the front position from the queue.
# For each of the four directions:
# Calculate the new coordinates by adding the direction to the current position.
# Check if the new position is valid (within bounds and not blocked):
# If the new position contains food ('#'), return the current steps.
# Otherwise, mark the cell as visited ('X') and add it to the queue.
# Increment the steps counter after processing all cells at the current level.
# If no food is found after the BFS completes, return -1 to indicate no valid path exists.
# Helper method isValid(grid, row, col):

# Check if the given position is:
# Within the grid's row boundaries
# Within the grid's column boundaries
# Not an obstacle ('X')
# Return true if all conditions are met, false otherwise.

# Complexity Analysis
# Let m be the number of rows and n be the number of columns in the grid.

# Time complexity: O(m⋅n)

# The BFS traversal visits each cell at most once. For each visited cell, we perform constant time operations (checking neighbors in four directions). Therefore, the time complexity is O(m⋅n).

# Space complexity: O(m⋅n)

# The queue used for BFS traversal can store at most m×n cells in the worst case, where all cells are free space ('O') and need to be visited. No additional data structures that grow with the input size are used. Therefore, the space complexity is O(m⋅n).

class Solution:
    def getFood(self, grid: list[list[str]]) -> int:
        # Possible moves: right, left, up, down
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        rows, cols = len(grid), len(grid[0])

        # Find starting position marked as '*'
        start = next(
            (i, j)
            for i in range(rows)
            for j in range(cols)
            if grid[i][j] == "*"
        )

        # BFS queue for level-by-level traversal
        queue = deque([start])
        steps = 1

        # BFS traversal
        while queue:
            # Process all cells at current level
            for _ in range(len(queue)):
                row, col = queue.popleft()

                # Try all four directions
                for dx, dy in dirs:
                    new_row, new_col = row + dx, col + dy

                    if self._is_valid(grid, new_row, new_col):
                        # Found food
                        if grid[new_row][new_col] == "#":
                            return steps

                        # Mark as visited and add to queue
                        grid[new_row][new_col] = "X"
                        queue.append((new_row, new_col))
            steps += 1

        # No path found to food
        return -1

    # Check if position is within bounds and not blocked
    def _is_valid(self, grid: list[list[str]], row: int, col: int) -> bool:
        return (
            0 <= row < len(grid)
            and 0 <= col < len(grid[0])
            and grid[row][col] != "X"
        )