import sys
import random

numbers = []
file = open('numbers.txt', 'r')
lines = file.readlines()
file.close()

for line in lines:
    clean = line.strip()
    numbers.append(int(clean))

print(numbers)

def is_sorted(values):
    for index in range(len(values) - 1):
        if values[index] > values[index + 1]:
            return False
    return True

def bogo_sort(values):
    attemp = 0
    while not is_sorted(values):
        print(attemp)
        random.shuffle(values)
        attemp += 1
    return values

print(bogo_sort(numbers))