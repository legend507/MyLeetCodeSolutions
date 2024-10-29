# My solution. works but time limit exceed.
# Thoughts:
# Try all path recursively.
class Solution_tooSlow:
    def move(self, current_location, former_score, r, c, grid):
        # Base conditions.
        # Check boundaries.
        current_r, current_c = current_location[0], current_location[1]
        if 0 > current_r or current_r >= r or 0 > current_c or current_c >= c:
            return 0
        # Check score.
        current_score = grid[current_r][current_c]
        if current_score <= former_score:
            return 0
        
        # Recursively try all moves.
        return max(
            1 + self.move([current_r - 1, current_c + 1], current_score, r, c, grid),
            1 + self.move([current_r, current_c + 1], current_score, r, c, grid),
            1 + self.move([current_r + 1, current_c + 1], current_score, r, c, grid))

    def maxMoves(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])

        ret = 0
        # Try to start from all cells in the first column.
        for row in range(r):
            ret = max(ret, self.move([row, 0], 0, r, c, grid))
        
        return ret - 1

# Editorial solution.
# Need to read this and figure out how this is done.
class Solution:
    # The three possible directions for the next column.
    dirs = [-1, 0, 1]

    def maxMoves(self, grid):
        M, N = len(grid), len(grid[0])

        q = deque()
        vis = [[False] * N for _ in range(M)]

        # Enqueue the cells in the first column.
        for i in range(M):
            vis[i][0] = True
            q.append((i, 0, 0))

        max_moves = 0
        while q:
            sz = len(q)

            for _ in range(sz):
                row, col, count = q.popleft()

                # Update the maximum moves made so far.
                max_moves = max(max_moves, count)

                for dir in self.dirs:
                    # Next cell after the move.
                    new_row, new_col = row + dir, col + 1

                    # If the next cell isn't visited yet and is greater than
                    # the current cell value, add it to the queue with the
                    # incremented move count.
                    if (
                        0 <= new_row < M
                        and 0 <= new_col < N
                        and not vis[new_row][new_col]
                        and grid[row][col] < grid[new_row][new_col]
                    ):
                        vis[new_row][new_col] = True
                        q.append((new_row, new_col, count + 1))

        return max_moves