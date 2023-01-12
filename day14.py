from collections import namedtuple, defaultdict
from bisect import bisect, insort
from typing import Callable, Tuple
from sortedcontainers import SortedList
from time import process_time
from copy import deepcopy

Point = namedtuple("Point", 'x y')

def timeFunction(f, *arg, **kwarg):
  def wrap(*arg, **kwarg):
    start = process_time()
    res = f(*arg, **kwarg)
    elapsed = process_time() - start
    print(f'{f.__name__} run {elapsed}s')
    return res
  return wrap

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

sand_start = Point(500, 0)

def createColumnStruct(lines: list[list[Point]], dir_constr: Callable) -> dict:
  columns = defaultdict(dir_constr)

  def rangeBetween(a, b):
    if a <= b:
      return range(a, b+1)
    return range(a, b-1, -1)

  for figure in lines:
    for i in range(len(figure)-1):
      p1, p2 = figure[i], figure[i+1]
      if p1.x == p2.x:
        columns[p1.x].extend( rangeBetween(p1.y, p2.y) )
      elif p1.y == p2.y:
        for x in rangeBetween(p1.x, p2.x):
          columns[x].append(p1.y)

  #deduplicate and sort columns
  for x, col in columns.items():
    columns[x] = sorted(list(set(col)))
  return columns

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

@timeFunction
def fillCave(columns: dict[list],  start_point: Point) -> tuple[int, dict[list]]:
  columns_copy = deepcopy(columns)
  sand_count = 0
  while dropSand(columns_copy, start_point):
    sand_count += 1
  return (sand_count, columns_copy)

#part1
part1map = createColumnStruct(lines, list)
sand_count, filled_map = fillCave(part1map, sand_start)
print(sand_count)

#part2
bottom = findBottom(lines) + 2
part2map = createColumnStruct(lines, lambda: list([bottom]))
sand_count, filled_map = fillCave(part2map, sand_start)
print(sand_count)
