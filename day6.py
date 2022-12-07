with open('day6.txt') as f:
  lines = f.readlines()

MARKER_LEN = 4

def asciiIndex(c):
  return ord(c) - ord('a')

def findUnique(s, marker_len):
  #fill the starting MARKER_LEN chars
  repeats = 0
  pos = 0
  letter_count = [0] * 26
  for c in s[:marker_len]:
    if letter_count[asciiIndex(c)] == 1:
      repeats += 1
    letter_count[ asciiIndex(c) ] += 1


  if repeats == 0:
    return marker_len

  while repeats > 0:
    c_quits = s[pos]
    c_enters = s[pos+marker_len]

    letter_count[ asciiIndex(c_quits) ] -= 1
    if letter_count[ asciiIndex(c_quits) ] == 1:
      repeats -= 1

    letter_count[ asciiIndex(c_enters) ] += 1
    if letter_count[ asciiIndex(c_enters) ] == 2:
      repeats += 1

    pos += 1

  return pos + marker_len

for line in lines:
  print(findUnique(line.strip(), 4))

#part2
for line in lines:
  print(findUnique(line.strip(), 14))
