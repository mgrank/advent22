from collections import deque

with open('day12.txt') as f:
  map = [list(line.strip()) for line in f]

  for row in range(len(map)):
    for col in range(len(map[row])):
      if map[row][col] == 'S':
        start = (col, row)
        map[row][col] = 'a'
      elif map[row][col] == 'E':
        end = (col, row)
        map[row][col] = 'z'

print(map)
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
  if ord(elev_from) - ord(elev_to) >= -1:
    return True
  return False

def bfs(map, start, end):
  to_visit = deque()
  to_visit.append(start)
  visited = {start}
  come_from = {}

  while len(to_visit) > 0:
    curr = to_visit.popleft()
    if curr == end:
      break
    for n in getNeighbors(map, curr[0], curr[1]):
      if n not in visited:
        if canClimb(map, curr, n):
          to_visit.append(n)
          visited.add(n)
          come_from[n] = curr

  return come_from

come_from = bfs(map, start, end)
print(come_from)
path = []
point = end
while point in come_from:
  path.append(point)
  point = come_from[point]

print(path)
print(len(path))