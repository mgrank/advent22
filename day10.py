with open('day10.txt') as f:
  #turn 'noop' instruction into [0] and 'addx N' instruction into [0, N]
  instructions = []
  for line in f:
    instructions.append(0)
    if line[0] == 'a':
      instructions.append( int(line[5:-1]) )

X = [1] #value of X after Nth cycle. X[0] - after 0 cycle i.e. initial, X[1] after 1st cycle completes etc
crt_line = []
for cycle in range(len(instructions)):
  X.append( X[-1] + instructions[cycle] )

  crt_pos = cycle % 40
  if abs(crt_pos - X[cycle]) <= 1:
    crt_line.append('#')
  else:
    crt_line.append('.')

  if crt_pos == 39: #crt line complete
    print(''.join(crt_line))
    crt_line = []

interesting_cycles = [20, 60, 100, 140, 180, 220]
signal_str = 0
for i in interesting_cycles:
  signal_str += X[i-1] * i
print(signal_str)

