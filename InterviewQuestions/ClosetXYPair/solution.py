grid = [['X', '0', '0'], 
        ['X', '0', '0'], 
        ['0', 'Y', 'Y']]

# List-like container with fast append and pop on either end.
from collections import deque

def wfs(grid: 'List[List[char]]') -> int:
	n, m = len(grid), len(grid[0])
	q, visited = deque(), set()
	dirs = [
		(1, 0), # Move left.
		(-1, 0), # Move right.
		(0, 1), # Move up.
		(0, -1), # Move down.
	]

	# Find all X and append to queue.
	for i in range(n):
		for j in range(m):
			if grid[i][j] == 'X':
				# (Position, distance).
				q.append(((i, j), 0))
				visited.add((i, j))

	while q:
		(row, col), dist = q.popleft()

		# The first Y I found will always be the shorted XY pair.
		if grid[row][col] == 'Y':
			return ((row, col), dist)

		# dist is sorted ascendly.
		for dir in dirs:
			newPos = (row + dir[0], col + dir[1])

			if newPos[0] <0 or newPos[0] >= len(grid) or newPos[1] < 0 or newPos[1] >= len(grid[0]) or (newPos in visited):
				continue
			q.append((newPos, dist + 1))
			visited.add(newPos)

	# Can't reach Y.
	return -1

print(wfs(grid))
