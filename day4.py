tasks = []
with open('day4.txt') as f:
  for line in f:
    tasks.append( [ list(map(int, elfTask.split('-'))) for elfTask in line.strip().split(',')] )

redundantCount = 0
for elfPair in tasks:
  f, s = elfPair[0], elfPair[1]
  if (f[0] <= s[0] and f[1] >= s[1]) or (f[0] >= s[0] and f[1] <= s[1]):
    redundantCount += 1

print(redundantCount)

#part2

redundantCount = 0
for elfPair in tasks:
  f, s = elfPair[0], elfPair[1]
  if not (f[0] > s[1] or s[0] > f[1]):
    redundantCount += 1

print(redundantCount)