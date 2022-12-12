with open('day9.txt') as f:
  def parseInstruction(ins):
    dirs = {'U': (0, 1), 'D': (0,-1), 'L': (-1,0), 'R': (1,0)}
    return (dirs[ins[0]], int(ins[2:]))
  instructions = [parseInstruction(line.strip()) for line in f.readlines()]

def manhDist(p1, p2):
  return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def sign(n):
  if n > 0: return 1
  if n < 0: return -1
  return 0

def moveRope(rope_length, instructions):
  tail_visited = set()
  rope = [ [0,0] for _ in range(rope_length) ]

  for i in instructions:
    dir, steps = i
    head_dx, head_dy = dir
    for _ in range(steps):
      rope[0][0] += head_dx
      rope[0][1] += head_dy
      for rope_i in range(rope_length-1):
        head = rope[rope_i]
        tail = rope[rope_i+1]

        if manhDist(head, tail) <= 1:
          break

        if manhDist(head, tail) >= 2:
          dx = head[0] - tail[0]
          dy = head[1] - tail[1]

          if abs(dx) == 1 and abs(dy) == 1: #diagonal is ok, no need to move tail
            break

          tail[0] += sign(dx)
          tail[1] += sign(dy)

      tail_visited.add( tuple(rope[-1]) )
  return len(tail_visited)

print(moveRope(2, instructions))
print(moveRope(10, instructions))

