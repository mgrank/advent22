with open('day10.txt') as f:
  #turn 'noop' instruction into [0] and 'addx N' instruction into [0, N]
  instructions = []
  for line in f:
    instructions.append(0)
    if line[0] == 'a':
      instructions.append( int(line[5:-1]) )

X = 1
crt_line = []
interesting_cycles = iter([20, 60, 100, 140, 180, 220, 999])
next_interesting = next(interesting_cycles)
signal_str = 0
for cycle in range(len(instructions)):
  #part1
  if cycle == next_interesting - 1:
    signal_str += next_interesting * X
    next_interesting = next(interesting_cycles)

  #part2
  crt_pos = cycle % 40
  if abs(crt_pos - X) <= 1:
    crt_line.append('#')
  else:
    crt_line.append('.')

  if crt_pos == 39: #crt line complete
    print(''.join(crt_line))
    crt_line = []

  X += instructions[cycle]

print(signal_str)

