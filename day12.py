from collections import deque

with open('day12.txt') as f:
  map = [list(line.strip()) for line in f]

  for row in range(len(map)):
    for col in range(len(map[row])):
      if map[row][col] == 'S':
        start = (col, row)
      elif map[row][col] == 'E':
        end = (col, row)

print(start, end)

def getNeighbors(map, x, y):
  neighbors = []
  if y < len(map) - 1:
    neighbors.append((x, y+1))
  if y > 0:
    neighbors.append((x, y-1))
  if x < len(map[0]) - 1:
    neighbors.append((x+1, y))
  if x > 0:
    neighbors.append((x-1, y))

  return neighbors

def canClimb(map, point_from, point_to):
  elev_from = map[point_from[1]][point_from[0]]
  elev_to   = map[point_to[1]][point_to[0]]
  if elev_from == 'S':
    elev_from = 'a'
  if elev_from == 'E':
    elev_from = 'z'
  if elev_to == 'S':
    elev_to = 'a'
  if elev_to == 'E':
    elev_to = 'z'
  if ord(elev_from) - ord(elev_to) >= -1:
    return True
  return False

def bfs_descent_until(map, start_coords, target_cell):
  to_visit = deque()
  to_visit.append(start_coords)
  visited = {start_coords}
  come_from = {}

  while len(to_visit) > 0:
    curr = to_visit.popleft()
    if map[curr[1]][curr[0]] == target_cell:
      break
    for n in getNeighbors(map, curr[0], curr[1]):
      if n not in visited:
        if canClimb(map, n, curr):
          to_visit.append(n)
          visited.add(n)
          come_from[n] = curr

  path = []
  point = curr
  while point in come_from:
    path.append(point)
    point = come_from[point]
  return path

#part 1
path = bfs_descent_until(map, end, 'S')
print(len(path))

#part 2
path = bfs_descent_until(map, end, 'a')
print(len(path))