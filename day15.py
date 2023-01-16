import re
from collections import defaultdict

r = re.compile('\-?\d+')
sensors = []
beacons = defaultdict(set)
with open('day15.txt') as f:
  for line in f:
    x_sens, y_sens, x_beac, y_beac = [int(n) for n in r.findall(line)]
    R = abs(x_sens - x_beac) + abs(y_sens - y_beac)
    sensors.append({'x': x_sens, 'y': y_sens, 'R': R})
    beacons[y_beac].add(x_beac)
    beacons[y_sens].add(x_sens)

def segmentOnLine(sensor, line_y) -> tuple[int,int] | None:
  if line_y > sensor['y'] + sensor['R'] or line_y < sensor['y'] - sensor['R']:
    return None
  dy = sensor['R'] - abs(sensor['y'] - line_y)
  return (sensor['x'] - dy, sensor['x'] + dy)

def intersects(s1: tuple, s2: tuple) -> bool:
  if s1[1] + 1 < s2[0] or s1[0] > s2[1] + 1:
    return False
  return True

def segmentIntersect(s1: tuple, s2: tuple) -> tuple:
  newx1 = min(s1[0], s2[0])
  newx2 = max(s1[1], s2[1])
  return (newx1, newx2)

def intersect(s1: tuple, s2: tuple) -> tuple:
  newx1 = max(s1[0], s2[0])
  newx2 = min(s1[1], s2[1])
  return (newx1, newx2)

def addSegment(segment_list: list[tuple[int,int]], new_segment: tuple[int, int]):
  intersect_candidates = []
  for i in range(len(segment_list)):
    if intersects(segment_list[i], new_segment):
      intersect_candidates.append(i)

  for i in intersect_candidates:
    new_segment = segmentIntersect(segment_list[i], new_segment)
    segment_list[i] = None
  for i in intersect_candidates:
    segment_list.remove(None)
  segment_list.append(new_segment)

slist = []
line_y = 2000000
for s in sensors:
  s_segment = segmentOnLine(s, line_y)
  if s_segment:
    addSegment(slist, s_segment)

print(slist)

s_sum = sum([abs(x1-x0)+1 for x0, x1 in slist]) - len(beacons[line_y])
print(s_sum)

#part2
max_coord = 4000000

for line_y in range(max_coord + 1):
  slist = []
  for s in sensors:
    s_segment = segmentOnLine(s, line_y)
    if s_segment:
      addSegment(slist, s_segment)
  if len(slist) > 1:
    print(slist[0][1]+1, line_y)
    xt = slist[0][1]+1
    freq = xt * 4000000 + line_y
    print(freq)