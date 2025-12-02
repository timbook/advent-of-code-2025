import numpy as np

# PART A ================================================== 

raw = open('data/input.txt', 'r').readlines()

data = [(line[0], int(line.strip()[1:])) for line in raw]

ptr = 50
counter = 0
for d, n in data:
    z = 1 if d == 'R' else -1
    ptr += z*n
    if ptr % 100 == 0:
        counter += 1

print(f"A :: {counter}")

# PART B ================================================== 

ptr = 50
counter = 0
for d, n in data:
    z = 1 if d == 'R' else -1
    for i in range(n):
        ptr += z
        if ptr % 100 == 0:
            counter += 1

print(f"B :: {counter}")
