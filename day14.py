from collections import namedtuple, defaultdict
from bisect import bisect, bisect_left, insort
from copy import deepcopy

Point = namedtuple("Point", 'x y')

with open('day14.txt') as f:
  def listStrToInt(lstr: list[str]) -> list[int]:
    lint = []
    for ls in lstr:
      xstr, ystr = ls.split(',')
      lint.append( Point(int(xstr), int(ystr)) )
    return lint

  lines = [listStrToInt(line.strip().split('->')) for line in f]

def findBottom(figures: list[list[int]]) -> int:
  bottom = 0
  for figure in figures:
    for point in figure:
      if point.y > bottom:
        bottom = point.y
  return bottom

bottom = findBottom(lines) + 2

sand_start = Point(500, 0)

columns = defaultdict(list)
columns2 = defaultdict(lambda: list([bottom]))

def rangeBetween(a, b):
  if a <= b:
    return range(a, b+1)
  return range(a, b-1, -1)

for figure in lines:
  for i in range(len(figure)-1):
    p1, p2 = figure[i], figure[i+1]
    if p1.x == p2.x:
      columns[p1.x].extend( rangeBetween(p1.y, p2.y) )
      columns2[p1.x].extend( rangeBetween(p1.y, p2.y) )
    elif p1.y == p2.y:
      for x in rangeBetween(p1.x, p2.x):
        columns[x].append(p1.y)
        columns2[x].append(p1.y)

#sort columns
for x, col in columns.items():
  columns[x] = sorted(list(set(col)))

for x, col in columns2.items():
  columns2[x] = sorted(list(set(col)))

def dropSand(columns: dict[list],  start_point: Point) -> bool:
  x = start_point.x
  y = start_point.y
  col = columns[x]
  if y in col:
    return False

  while True:
    col = columns[x]
    i = bisect(col, y)
    if i == len(col):
      return False #falls in void
    next_stop = col[i] - 1
    #check left and right sliding
    if next_stop + 1 not in columns[x-1]:
      x = x - 1
      y = next_stop + 1
    elif next_stop + 1 not in columns[x+1]:
      x = x + 1
      y = next_stop + 1
    else:
      #came to stop
      insort(col, next_stop)
      return True

def fillCave(columns: dict[list],  start_point: Point) -> int:
  sand_count = 0
  columns = deepcopy(columns)
  while dropSand(columns, sand_start):
    sand_count += 1
  return sand_count

#part1
print(fillCave(columns, sand_start))

#part2

print(fillCave(columns2, sand_start))




