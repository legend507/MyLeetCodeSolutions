""" 
Using DFS on a 2D array is the idea. 
Starting from every cell that is land, conduct DFS, then find the largest count.

Points to remember:
  - Python fn parameters are always pass-by-reference.
  - Traversing a matrix usually involves using the used_cells to remember traversed cells.
"""


def IsWater(map, x, y):
  # If x,y is 1 step away from the boarder.
  if (x >= -1 and x <= len(map)) and (y >= -1 and y <= len(map[0])):
    # If x,y is within the boarder.
    if (x >= 0 and x <= len(map)) and (y >= 0 and y <= len(map[0])):
      return (map[x][y] == 0)
    return True
  return True

def IsInMap(the_map, x, y):
  return (x >= 0 and x < len(the_map[0])) and (y >= 0 and y < len(the_map))


def WaterStep(the_map, x, y, used_cells):
  """ Put all water cells into used_cells. """
  for x in range(len(the_map)):
    for y in range(len(the_map)):
  
      if IsWater(the_map, x, y) and (x, y) not in used_cells:
        used_cells.add((x, y))


def ContinentStepDFS(the_map, x, y, used_cells, count):
  # Terminate condiation.
  if not IsInMap(the_map, x, y) or (x, y) in used_cells:
    return
  
  print('({}, {})'.format(x, y))
  
  used_cells.add((x, y))
  count[0] += 1
  # I can only move horizontally or vertically.
  for d_x, d_y in ((-1, 0), (0, 1), (1, 0), (0, -1)):
    new_x = x + d_x
    new_y = y + d_y
    ContinentStepDFS(the_map, new_x, new_y, used_cells, count)


def LargestLandlockedArea(the_map):
  """Returns the sqare of the contitent with the largest landlocked area.

  Args:
    the_map: A matrix of ints, 0 = water, 1 = land
  
  Returns:
    An integer area, in a number of cells.
  """
  # Pass1. Finding a boundary water.
  used_cells = set()
  # Start from (-1, -1), a virtual area out of the map bounds which is
  # a water
  WaterStep(the_map, -1, -1, used_cells)
  # Pass 2. Finding continents with area computations.
  max_count = 0
  for x in range(len(the_map)):
    for y in range(len(the_map[x])):
      if (x, y) in used_cells:
        continue
      # Not a boundary water.
      count = [0]
      ContinentStepDFS(the_map, x, y, used_cells, count)
      print('------------- {}'.format(count[0]))
      if count[0] > max_count:
        max_count = count[0]
  return max_count


the_map = [
           [0, 1, 1, 1, 0],
           [0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 1, 1, 1, 0],
           [0, 0, 1, 0, 0],
]

print(LargestLandlockedArea(the_map))


