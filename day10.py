with open('day10.txt') as f:
  instructions = [line.strip().split() for line in f]

print(instructions)

prevX = X = 1
cycle = 0
interesting_cycles = (g for g in [20, 60, 100, 140, 180, 220])
next_interesting = next(interesting_cycles)
sum_signal = 0

for i in instructions:
  if i[0] == 'noop':
    cycle += 1
  elif i[0] == 'addx':
    dx = int(i[1])
    cycle += 2
    prevX = X
    X += dx

  if cycle >= next_interesting:
    sum_signal += next_interesting * prevX
    try:
      next_interesting = next(interesting_cycles)
    except:
      break

print(sum_signal)

#part2
crt = []
X = 1
i = iter(instructions)
ilen = 1
instr = None
for cycle in range(240):
  ilen -= 1
  if ilen == 0:
    if instr and instr[0] == 'addx':
      dx = int(instr[1])
      X += dx

    instr = next(i)
    if instr[0] == 'noop':
      ilen = 1
    elif instr[0] == 'addx':
      ilen = 2

  if abs(cycle % 40 - X) <= 1:
    crt.append('#')
  else:
    crt.append('.')

print(crt)
print(''.join(crt[:40]))
print(''.join(crt[40:80]))
print(''.join(crt[80:120]))
print(''.join(crt[120:160]))
print(''.join(crt[160:200]))
print(''.join(crt[200:]))
