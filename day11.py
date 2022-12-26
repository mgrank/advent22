from dataclasses import dataclass
from typing import Callable
from functools import reduce
@dataclass
class Monkey:
    items : list[int]
    operation : Callable[[int], int]
    test : Callable[[int], bool]
    throw_true : int
    throw_false : int
    inspections: int = 0

    def whoThrowTo(self, worry: int) -> int:
      if self.test(worry):
        return self.throw_true
      return self.throw_false

monkeys : list[Monkey] = []
supermod : int = 1

def strOper(s: str) -> Callable[[int], int]:
  return lambda old: eval(s)

def createTest(test_val: int) -> Callable[[int], bool]:
  return lambda worry: worry % test_val == 0

with open('day11.txt') as f:
  while True:
    monkey_lines = [f.readline().strip() for _ in range(6)]
    start_items = [int(item) for item in monkey_lines[1].split(':')[-1].split(',')]
    operation = monkey_lines[2].split('=')[-1]
    test = int(monkey_lines[3].split(' ')[-1])
    supermod *= test
    throw_true = int(monkey_lines[4].split(' ')[-1])
    throw_false = int(monkey_lines[5].split(' ')[-1])
    new_monkey = Monkey(start_items, strOper(operation), createTest(test), throw_true, throw_false)
    monkeys.append(new_monkey)
    delimiter = f.readline()
    if not delimiter:
      break

for round in range(10000):
  for monkey in monkeys:
    for item in monkey.items[:]:
      monkey.inspections += 1
      new_worry = monkey.operation(item) % supermod
      who_throw_to = monkey.whoThrowTo(new_worry)
      monkey.items.remove(item)
      monkeys[who_throw_to].items.append(new_worry)

top2 = sorted(monkeys, key=lambda monkey: monkey.inspections)[-2:]
print(top2[0].inspections * top2[1].inspections)
