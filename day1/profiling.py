from multiset import Multiset
from collections import Counter
import cProfile

def ReadInput():
  input = []
  with open("input.txt") as file:
    for line in file.read().splitlines():
      input.append(line)
  return input

def PartOne(input):
  # Splitting the groups
  first_group = [int(line.split(" ")[0]) for line in input]
  second_group = [int(line.split(" ")[-1]) for line in input]

  # Check minimun an pops it from list
  acc = 0
  for i in range(len(first_group)):
    first_min = min(first_group)
    second_min = min(second_group)
    acc += abs(first_min - second_min)
    first_group.remove(first_min)
    second_group.remove(second_min)
  return acc

def PartOneAlt(input):
  # Splitting the groups
  first_group = [int(line.split(" ")[0]) for line in input]
  second_group = [int(line.split(" ")[-1]) for line in input]

  first_group.sort()
  second_group.sort()
  distance = sum([abs(first_group[i] - second_group[i]) for i in range(len(input))])
  return distance

def PartTwo(input):
  # Store the groups again
  first_group = [int(line.split(" ")[0]) for line in input]
  second_group = [int(line.split(" ")[-1]) for line in input]
  # Convert to multiset to make intersection
  first_set = Multiset(first_group)
  second_set = Multiset(second_group)
  intersection_set = first_set.intersection(second_set)
  acc2 = 0
  for number in intersection_set:
    # Compares with second set because intersection removes duplicates
    acc2 += number * second_set.get(number, default=int)

  return acc2


input = ReadInput()

cProfile.run("PartOne(input)")
cProfile.run("PartOneAlt(input)")
cProfile.run("PartTwo(input)")
