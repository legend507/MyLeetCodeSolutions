class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Try to find pattern,
        # In case of 3 x 3, 
        # [0, 0] -> [0, 2]
        # [0, 1] -> [1, 2]
        # [0, 2] -> [2, 2].
        # So, [0, i] will become [i, 2].

        # That said, [i, j] should become [j, n - i - 1].

        n = len(matrix)
        moved = [[False] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                current_i, current_j = i, j
                current_value = matrix[current_i][current_j]

                while moved[current_i][current_j] == False:
                    moved[current_i][current_j] = True
                    # Find the coordinate to move current i,j to.
                    new_i, new_j = current_j, n - current_i - 1
                    keep_value = matrix[new_i][new_j]
                    matrix[new_i][new_j] = current_value
                    current_i, current_j = new_i, new_j
                    current_value = keep_value


s = Solution()
s.rotate([[1,2,3],[4,5,6],[7,8,9]])