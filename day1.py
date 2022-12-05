from functools import reduce

f = open('day1.txt')
lines = f.read()

elfCalories = [s.split() for s in lines.split('\n\n')]
elfCalories = [sum(map(int, elf)) for elf in elfCalories]
print(max(elfCalories))

elfCalories.sort()
print(sum(elfCalories[-3:]))