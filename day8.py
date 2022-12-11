trees = []
with open('day8test.txt') as f:
  for line in f:
    tree_line = [int(tree) for tree in list(line.strip())]
    trees.append(tree_line)


visibility = [[0 for _ in line] for line in trees]
visible = 0

x_index = [range(len(trees[0])), range(len(trees[0])-1,-1,-1)] #forward and backward

max_height = [-1] * len(trees)
for x in range(len(trees[0])):
  for y in range(len(trees)):
    if trees[y][x] > max_height[y]:
      max_height[y] = trees[y][x]
      visibility[y][x] = 1

max_height = [-1] * len(trees)
for x in range(len(trees[0])-1,-1,-1):
  for y in range(len(trees)):
    if trees[y][x] > max_height[y]:
      max_height[y] = trees[y][x]
      visibility[y][x] = 1

max_height = [-1] * len(trees[0])
for x in range(len(trees[0])):
  for y in range(len(trees)):
    if trees[y][x] > max_height[x]:
      max_height[x] = trees[y][x]
      visibility[y][x] = 1

max_height = [-1] * len(trees[0])
for x in range(len(trees[0])):
  for y in range(len(trees)-1,-1,-1):
    if trees[y][x] > max_height[x]:
      max_height[x] = trees[y][x]
      visibility[y][x] = 1

visible = sum([sum(line) for line in visibility])
print(visible)