f = open('day3.txt')
lines = [line.strip() for line in f]
priorities = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
def findPriority(letter):
  return priorities.find(letter) + 1

sumPriorities = 0

for rucksack in lines:
  mid = len(rucksack) // 2
  firstHalfItems = set(rucksack[:mid])
  commonItem = ''
  for item in rucksack[mid:]:
    if item in firstHalfItems:
      commonItem = item
      break

  if commonItem:
    sumPriorities += findPriority(commonItem)

print(sumPriorities)

#part 2

sumPriorities = 0

for groupN in range(0, len(lines), 3):
  group = lines[groupN: groupN + 3]
  commonItems = set(group[0])
  for rucksack in group[1:]:
    items = set(rucksack)
    commonItems = commonItems.intersection(items)
  item = commonItems.pop()
  sumPriorities += findPriority(item)

print(sumPriorities)