import functools

#there is ast.literal_eval to parse strings more safely than simple eval
#but writing small parser was fun :)
def parseList(list_str: str) -> list:
  if list_str[0] != '[':
    return int(list_str)

  real_list = []
  list_str = list_str[1:-1]
  list_tokens = []
  bracket_level = 0
  last_comma_pos = -1
  for i in range(len(list_str)):
    if list_str[i] == '[':
      bracket_level += 1
    elif list_str[i] == ']':
      bracket_level -= 1

    if list_str[i] == ',' and bracket_level == 0:
      list_tokens.append( list_str[last_comma_pos+1:i] )
      last_comma_pos = i

  list_tokens.append( list_str[last_comma_pos+1:] )

  if list_tokens != ['']:
    for token in list_tokens:
      real_list.append(parseList(token))

  return real_list

def checkPairOrder(pair1, pair2) -> int: #-1 not right, 0 equal, 1 right
  for i in range( min(len(pair1), len(pair2)) ):
    p1 = pair1[i]
    p2 = pair2[i]
    if type(p1) == int and type(p2) == int:
      if p1 == p2:
        continue
      if p1 < p2: return -1
      if p1 > p2: return 1

    if type(p1) == int:
      p1 = [p1]
    if type(p2) == int:
      p2 = [p2]

    #compare lists
    res = checkPairOrder(p1, p2)
    if res != 0:
      return res

  if len(pair1) < len(pair2): return -1
  elif len(pair1) > len(pair2): return 1
  return 0

with open('day13.txt') as f:
  pair_index = 1
  sum = 0
  while True:
    pair1 = parseList( f.readline().strip() )
    pair2 = parseList( f.readline().strip() )
    if checkPairOrder(pair1, pair2) == -1:
      sum += pair_index

    delimiter = f.readline()
    if delimiter == '':
      break

    pair_index += 1
  print(sum)

#part2
with open('day13.txt') as f:
  packets = [ parseList(line.strip()) for line in f if line != '\n']
  div1, div2 = [[2]], [[6]]
  packets.extend([div1, div2])
  packets.sort(key=functools.cmp_to_key(checkPairOrder))
  decoder_key = 1
  for i in range(len(packets)):
    if packets[i] == div1 or packets[i] == div2:
      decoder_key *= i+1
  print(decoder_key)

assert parseList('9') == 9
assert parseList('999') == 999
assert parseList('[]') == []
assert parseList('[9]') == [9]
assert parseList('[9,8,7,6]') == [9,8,7,6]
assert parseList('[[9],[8,7,6]]') == [[9],[8,7,6]]
assert parseList('[1,[2,[3,[4,[5,6,7]]]],8,9]') == [1,[2,[3,[4,[5,6,7]]]],8,9]
assert parseList('[[[[]]],[[]]]') == [[[[]]],[[]]]