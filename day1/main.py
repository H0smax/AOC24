from multiset import Multiset
from collections import Counter

# Storing the lines
input = []
with open("input.txt") as file:
  for line in file.read().splitlines():
    input.append(line)

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

print("First part:", acc)


# Second part:
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

print("Second part:", acc2)
