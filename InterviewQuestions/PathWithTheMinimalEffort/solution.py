grid = [
  [0,1,1,3,4],
  [3,4,2,0,1],
  [2,2,2,4,3],
  [1,3,4,3,1],
  [1,2,1,1,0]]

from collections import deque

def wfs(grid: 'List[List[int]]') -> int:
  dirs = [
    (1, 0), # Right.
    (-1, 0), # Left.
    (0, 1), # Down.
    (0, -1), # Up.
  ]
  n = len(grid)
  m = len(grid[0])

  # A good example of creating default max matrix in Python.
  efforts = [[float('inf')] * m for _ in range(n)]
  efforts[0][0] = 0
  path = [[()] * m for _ in range(n)]

  q = deque()
  q.append(((0, 0), 0)) # (row, col), effort.

  while q:
    (pos, effort) = q.popleft()
    # If pos is reached before and the effort is smaller.
    if effort > efforts[pos[0]][pos[1]]:
      continue
    # Otherwise, from pos move towards the 4 directions.
    for dir in dirs:
      newPos = (pos[0] + dir[0], pos[1] + dir[1])
      # Validate newPos.
      if newPos[0] < 0 or newPos[0] >= n or newPos[1] < 0 or newPos[1] >= m:
        continue

      newEffort = effort + abs(grid[newPos[0]][newPos[1]] - grid[pos[0]][pos[1]])

      # If newEffort is smaller, then we found a better path.
      if newEffort < efforts[newPos[0]][newPos[1]]:
        efforts[newPos[0]][newPos[1]] = newEffort
        path[newPos[0]][newPos[1]] = pos
        q.append((newPos, newEffort))
  
  print(path)
  print(efforts)
  return efforts[n-1][m-1]

print(wfs(grid))