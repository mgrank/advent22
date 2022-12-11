trees = []
with open('day8.txt') as f:
  for line in f:
    tree_line = [int(tree) for tree in list(line.strip())]
    trees.append(tree_line)

visibility = [[0 for _ in line] for line in trees] #table that shows if particular tree is visible (1) or not (0)

look_directions = [ (range(len(trees[0])), range(len(trees))), #forward and down
                    (range(len(trees[0])-1,-1,-1), range(len(trees)-1,-1,-1)) ] #backward and up

for x_range, y_range in look_directions:
  max_height_y = [-1] * len(trees)
  max_height_x = [-1] * len(trees[0])
  for x in x_range:
    for y in y_range:
      if trees[y][x] > max_height_y[y]:
        max_height_y[y] = trees[y][x]
        visibility[y][x] = 1
      if trees[y][x] > max_height_x[x]:
        max_height_x[x] = trees[y][x]
        visibility[y][x] = 1

visible = sum([sum(line) for line in visibility])
print(visible)

#part2
def calcScenicScore(trees, x, y):
  my_height = trees[y][x]
  score = 1
  x1 = x
  while x1 < len(trees[0]) - 1:
    x1 += 1
    if trees[y][x1] >= my_height:
      break
  score *= x1 - x

  x1 = x
  while x1 > 0:
    x1 -= 1
    if trees[y][x1] >= my_height:
      break
  score *= x - x1

  y1 = y
  while y1 < len(trees) - 1:
    y1 += 1
    if trees[y1][x] >= my_height:
      break
  score *= y1 - y

  y1 = y
  while y1 > 0:
    y1 -= 1
    if trees[y1][x] >= my_height:
      break
  score *= y - y1

  return score

max_score = 0

for y in range(len(trees)):
  for x in range(len(trees[0])):
    max_score = max(max_score, calcScenicScore(trees, x, y))

print(max_score)
