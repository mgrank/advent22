import re
import time

graph = {}
with open('day16.txt') as f:
  rnames = re.compile('[A-Z]{2,}')
  rrate = re.compile('rate=(\d+)')
  for line in f:
    cur_valve, connected = rnames.findall(line)[0], rnames.findall(line)[1:]
    connected = {target: 1 for target in connected}
    rate = int(rrate.search(line).group(1))
    graph[cur_valve] = (rate, connected)

print(len(graph))

#optimize graph
zero_valves = [valve for valve in graph if graph[valve][0] == 0]
for v_cur in zero_valves:
  if v_cur == 'AA':
    continue

  connections = list(graph[v_cur][1])
  for i in range(len(connections)):
    for j in range(i+1, len(connections)):
      v_from, v_to = connections[i], connections[j]
      total_cost = graph[v_cur][1][v_to] + graph[v_from][1][v_cur]

      if v_to in graph[v_from][1]:
        if total_cost < graph[v_from][1][v_to]:
          graph[v_from][1][v_to] = total_cost
      else:
        graph[v_from][1][v_to] = total_cost

      if v_from in graph[v_to][1]:
        if total_cost < graph[v_to][1][v_from]:
          graph[v_to][1][v_from] = total_cost
      else:
        graph[v_to][1][v_from] = total_cost

  for c in connections:
    del graph[c][1][v_cur]
  del graph[v_cur]

print(len(graph))


closed_valves = sum([1 for v in graph.values() if v[0] != 0])

def dfs(start_valve: str, graph: dict, time: int, open_valves: set = set(), minute_rate: int = 0, total_rate: int = 0, prev_valve: str = None, length: int = 1):
  #print(total_rate, open_valves, minute_rate, total_rate, move_list)
  if time - length < 0:
    length = time
  total_rate += minute_rate * length
  time -= length

  if time == 0:
    return total_rate

  possible_moves = []
  if graph[start_valve][0] != 0: #no reason to open valves with 0 pressure
    if start_valve not in open_valves:
      new_open_valves = open_valves.copy()
      new_open_valves.add(start_valve)
      new_minute_rate = minute_rate + graph[start_valve][0]
      possible_moves.append( dfs(start_valve, graph, time, new_open_valves, new_minute_rate, total_rate, start_valve) ) #open valve

  for next_valve, cost in graph[start_valve][1].items():
    if next_valve == prev_valve:
      continue
    possible_moves.append( dfs(next_valve, graph, time, open_valves, minute_rate, total_rate, start_valve, cost) ) #move to different valve

  if len(possible_moves) == 0:
    return total_rate + minute_rate * time
  return max(possible_moves)

start = time.process_time()
x = dfs('AA', graph, 30)
elapsed = time.process_time() - start
print(x, elapsed)

