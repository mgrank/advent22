with open('day2.txt') as f:
  strategyGuide = f.readlines()

scoreMove = {'X': 1, 'Y': 2, 'Z': 3}
scoreRound = {
  'A': {'X': 3, 'Y': 6, 'Z': 0},
  'B': {'X': 0, 'Y': 3, 'Z': 6},
  'C': {'X': 6, 'Y': 0, 'Z': 3},
}

score = 0
for round in strategyGuide:
  hisMove, myMove = round.split()
  score += scoreMove[myMove]
  score += scoreRound[hisMove][myMove]

print(score)

#part 2
score = 0
resultTable = { 'X': 0, 'Y': 3, 'Z': 6 }
for round in strategyGuide:
  hisMove, roundResult = round.split()
  roundScore = resultTable[roundResult]
  myMoveVariants = scoreRound[hisMove]
  for k, v in myMoveVariants.items():
    if v == roundScore:
      myMove = k
      score += scoreMove[myMove]
      score += roundScore
      break

print(score)

