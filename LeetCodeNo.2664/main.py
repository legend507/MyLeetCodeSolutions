# Given two positive integers m and n which are the height and width of a 0-indexed 2D-array board, a pair of positive integers (r, c) which is the starting position of the knight on the board.

# Your task is to find an order of movements for the knight, in a manner that every cell of the board gets visited exactly once (the starting cell is considered visited and you shouldn't visit it again).

# Return the array board in which the cells' values show the order of visiting the cell starting from 0 (the initial place of the knight).

# Note that a knight can move from cell (r1, c1) to cell (r2, c2) if 0 <= r2 <= m - 1 and 0 <= c2 <= n - 1 and min(abs(r1 - r2), abs(c1 - c2)) = 1 and max(abs(r1 - r2), abs(c1 - c2)) = 2.

 

# Example 1:

# Input: m = 1, n = 1, r = 0, c = 0
# Output: [[0]]
# Explanation: There is only 1 cell and the knight is initially on it so there is only a 0 inside the 1x1 grid.
# Example 2:

# Input: m = 3, n = 4, r = 0, c = 0
# Output: [[0,3,6,9],[11,8,1,4],[2,5,10,7]]
# Explanation: By the following order of movements we can visit the entire board.
# (0,0)->(1,2)->(2,0)->(0,1)->(1,3)->(2,1)->(0,2)->(2,3)->(1,1)->(0,3)->(2,2)->(1,0)

class Solution_wront:
    def tourOfKnight(self, m: int, n: int, r: int, c: int) -> List[List[int]]:
        # My solution.
        # This doesn't work, as this is a knight tour problem.
        board = [[-1] * n for _ in range(m)]
        
        current_step = 0
        next_move = [r, c]

        def find_next_move(now):
            x, y = now[0], now[1]
            # +1, +2
            if 0<=x+1<m and 0<=y+2<n and board[x+1][y+2] == -1:
                return [x+1, y+2]
            # +1, -2
            elif 0<=x+1<m and 0<=y-2<n and board[x+1][y-2] == -1:
                return [x+1, y-2]
            # -1, +2
            elif 0<=x-1<m and 0<=y+2<n and board[x-1][y+2] == -1:
                return [x-1, y+2]
            # -1, -2
            elif 0<=x-1<m and 0<=y-2<n and board[x-1][y-2] == -1:
                return [x-1, y-2]
            # +2, +1
            elif 0<=x+2<m and 0<=y+1<n and board[x+2][y+1] == -1:
                return [x+2, y+1]
            # +2, -1
            elif 0<=x+2<m and 0<=y-1<n and board[x+2][y-1] == -1:
                return [x+2, y-1]
            # -2, +1
            elif 0<=x-2<m and 0<=y+1<n and board[x-2][y+1] == -1:
                return [x-2, y+1]
            # -2, -1
            elif 0<=x-2<m and 0<=y-1<n and board[x-2][y-1] == -1:
                return [x-2, y-1]
            else:
                return None



        while next_move:
            board[next_move[0]][next_move[1]] = current_step
            current_step += 1

            next_move = find_next_move(next_move)

        return board


class Solution:
    def tourOfKnight(self, m, n, r, c):
        # Precompute possible knight moves
        moves = [
            (2, 1),
            (2, -1),
            (-2, 1),
            (-2, -1),
            (1, 2),
            (1, -2),
            (-1, 2),
            (-1, -2),
        ]

        def _is_valid_move(to_row, to_col):
            return (
                0 <= to_row < m
                and 0 <= to_col < n
                and chessboard[to_row][to_col] == -1
            )

        def _solve_knights_tour(current_row, current_col, move_count):
            # Base case: if all cells have been visited, we've found a solution
            if move_count == m * n:
                return True

            # Try all possible knight moves
            for move_r, move_c in moves:
                new_row, new_col = current_row + move_r, current_col + move_c
                # Check if the move is valid
                if _is_valid_move(new_row, new_col):
                    chessboard[new_row][new_col] = move_count

                    # Recursively try to solve from this new position
                    if _solve_knights_tour(new_row, new_col, move_count + 1):
                        return True

                    # If the move doesn't lead to a solution, backtrack
                    chessboard[new_row][new_col] = -1

            # If no solution is found from the current position
            return False

        chessboard = [[-1] * n for _ in range(m)]

        chessboard[r][c] = 0

        # Start the recursive solving process
        _solve_knights_tour(r, c, 1)

        return chessboard