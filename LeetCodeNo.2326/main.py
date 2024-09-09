# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def _next_coordinates(self, x, y, m, n, matrix, direction):
        # x = [0, m-1], y = [0, n - 1]

        # If current direction = left.
        if direction == 'left':
            # Not yet reach end or a filled cell, continue left.
            # Otherwise, go down.
            if y+1<n and matrix[x][y+1] == -1:
                return x, y+1, 'left'
            else:
                return x+1, y, 'down'
        
        # If current direction = down.
        if direction == 'down':
            if x+1<m and matrix[x+1][y] == -1:
                return x+1, y, 'down'
            else:
                return x, y-1, 'right'

        # If current direction = right.
        if direction == 'right':
            if y-1 >=0 and matrix[x][y-1] == -1:
                return x, y-1, 'right'
            else:
                return x-1, y, 'up'

        # If current direciton == up.
        if direction == 'up':
            if x-1>=0 and matrix[x-1][y] == -1:
                return x-1, y, 'up'
            else:
                return x, y+1, 'left'


    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1] * n for _ in range(m)]
        x, y = 0, 0
        direction = 'left'
        pointer = head
        while pointer != None:
            matrix[x][y] = pointer.val
            pointer = pointer.next
            x, y, direction = self._next_coordinates(x, y, m, n, matrix, direction)
        
        return matrix
