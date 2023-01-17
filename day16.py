import re
import time

graph = {}
with open('day16.txt') as f:
  rnames = re.compile('[A-Z]{2,}')
  rrate = re.compile('rate=(\d+)')
  for line in f:
    cur_valve, connected = rnames.findall(line)[0], rnames.findall(line)[1:]
    rate = int(rrate.search(line).group(1))
    graph[cur_valve] = (rate, connected)
    print(cur_valve, connected, rate)

closed_valves = sum([1 for v in graph.values() if v[0] != 0])
print(closed_valves)

def dfs(start_valve: str, graph: dict, time: int, open_valves: set = set(), minute_rate: int = 0, total_rate: int = 0, prev_valve: str = None):
  #print(total_rate, open_valves, minute_rate, total_rate, move_list)
  total_rate += minute_rate
  time -= 1

  if time == 0:
    return total_rate

  possible_moves = []
  if graph[start_valve][0] != 0: #no reason to open valves with 0 pressure
    if start_valve not in open_valves:
      new_open_valves = open_valves.copy()
      new_open_valves.add(start_valve)
      new_minute_rate = minute_rate + graph[start_valve][0]
      possible_moves.append( dfs(start_valve, graph, time, new_open_valves, new_minute_rate, total_rate, start_valve) ) #open valve

  for next_valve in graph[start_valve][1]:
    if next_valve == prev_valve:
      continue
    possible_moves.append( dfs(next_valve, graph, time, open_valves, minute_rate, total_rate, start_valve) ) #move to different valve

  if len(possible_moves) == 0:
    return total_rate + minute_rate * time
  return max(possible_moves)

start = time.process_time()
x = dfs('AA', graph, 25)
elapsed = time.process_time() - start
print(x, elapsed)

