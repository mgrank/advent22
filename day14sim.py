import copy
from re import S
from time import process_time

start_point = (500,0)
map_set = set()
max_depth = 0

def timeFunction(f, *arg, **kwarg):
  def wrap(*arg, **kwarg):
    start = process_time()
    res = f(*arg, **kwarg)
    elapsed = process_time() - start
    print(f'{f.__name__} run {elapsed}s')
    return res
  return wrap

def rangeBetween(a, b):
  if a <= b:
    return range(a, b+1)
  return range(a, b-1, -1)

with open('day14.txt') as f:
  for fline in f:
    #tuples are 4-5x times faster than namedtuples
    line = [tuple(map(int, a.split(','))) for a in fline.strip().split(' -> ')]
    for p, p_next in zip(line, line[1:]):
      px, py = p
      px_next, py_next = p_next
      if px == px_next:
        for y in rangeBetween(py, py_next):
          map_set.add( (px, y) )
      elif py == py_next:
        for x in rangeBetween(px, px_next):
          map_set.add( (x, py) )

max_depth = max(map_set, key=lambda p: p[1])[1]

def dropSand(start_point, map_set, floor_offset = 0):
  if start_point in map_set:
    return False

  x, y = start_point
  while y < max_depth + floor_offset:
    if (x, y+1) not in map_set:
      y += 1
      continue
    elif (x-1, y+1) not in map_set:
      y += 1
      x -= 1
      continue
    elif (x+1, y+1) not in map_set:
      y += 1
      x += 1
      continue
    map_set.add((x,y))
    return True

  if floor_offset != 0:
    map_set.add((x,y))
    return True
  else: #part1 with void
    return False

@timeFunction
def fillCave(start_point, map_set, floor_offset=0):
  map_copy = copy.copy(map_set)
  sand_count = 0
  while dropSand(start_point, map_copy, floor_offset):
    sand_count += 1
  return sand_count

#part1
print(fillCave(start_point, map_set))

#part2
print(fillCave(start_point, map_set, floor_offset=1))