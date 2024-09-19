class Solution:
    def spread(self, spread, i, j, rows, cols, min, grid):
        # Recursive.

        # End condition: coordiantes not valid.
        if i <= -1 or i >= rows or j <= -1 or j >= cols:
            return
        # End condition: if current cell is empty.
        if grid[i][j] == 0:
            return
        # End condition: If current cell is fresh orange, but has smaller spread.
        if -1 < spread[i][j] < min:
            return

        # Update the current cell with min, if the cell has never been spreaded to or take longer than current spread.
        spread[i][j] = min
        # Spread to 4 directions.
        self.spread(spread, i+1, j, rows, cols, min+1, grid)
        self.spread(spread, i-1, j, rows, cols, min+1, grid)
        self.spread(spread, i, j+1, rows, cols, min+1, grid)
        self.spread(spread, i, j-1, rows, cols, min+1, grid)


    def orangesRotting(self, grid: list[list[int]]) -> int:
        # from each rotten, traverse all matrix
        # Use another matrix of the same size to decide how long each orange goes rotten.
        rows = len(grid)
        cols = len(grid[0])

        # spread[i][j] means how long does it take for the rotten to reach this cell.
        spread = [[-1] * cols for _ in range(rows)]

        # Traverse grid, and spread from each rotten orange.
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    # Found a rotten orange, update the spread matrix.
                    self.spread(spread, i, j, rows, cols, 0, grid)

        # Traverse grid again, check each orange, decide return.
        # print(spread)
        max_turns = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    if spread[i][j] == -1:
                        return -1
                    else:
                        max_turns = max(max_turns, spread[i][j])
        return max_turns
    
grid = [[2,1,1],[1,1,0],[0,1,1]]
s = Solution()
s.orangesRotting(grid)
