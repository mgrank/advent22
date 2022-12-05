from copy import deepcopy
import re

with open('day5.txt') as f:
  lines = [line[:-1] for line in f]

empty_line = lines.index('')
stacks_str = lines[:empty_line]
moves_str = lines[empty_line+1:]

n_stacks = int(stacks_str[-1].strip()[-1]) #last line contains number of stacks
stacks = [ [] for _ in range(n_stacks) ]
for lnum in range(len(stacks_str)-2, -1, -1):
  line = stacks_str[lnum]
  for cnum in range(0, n_stacks):
    c = 1 + 4*cnum
    if c > len(line):
      break
    if line[c] != ' ':
      stacks[cnum].append(line[c])

stacks2 = deepcopy(stacks)

for move in moves_str:
  res = re.search('move (\d+) from (\d+) to (\d+)', move)
  if res:
    amount, frm, to = [int(n) for n in res.groups()]
    frm -= 1
    to -= 1
    stacks[to].extend(reversed(stacks[frm][-amount:]))
    stacks[frm] = stacks[frm][:-amount]


res = ''.join([s[-1] for s in stacks])
print(res)

#part2
stacks = stacks2
for move in moves_str:
  res = re.search('move (\d+) from (\d+) to (\d+)', move)
  if res:
    amount, frm, to = [int(n) for n in res.groups()]
    frm -= 1
    to -= 1
    stacks[to].extend(stacks[frm][-amount:]) #don't reverse stacked crates
    stacks[frm] = stacks[frm][:-amount]

res = ''.join([s[-1] for s in stacks])
print(res)


