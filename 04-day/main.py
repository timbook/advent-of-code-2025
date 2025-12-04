import numpy as np
from itertools import product

raw = open('data/input.txt', 'r').readlines()
mx = np.array([list(line.strip()) for line in raw])
R, C = mx.shape

def get_nbs(r, c, R, C):
    nb_candidates = [
        (r - 1, c - 1), (r, c - 1), (r + 1, c - 1),
        (r - 1, c),                 (r + 1, c),
        (r - 1, c + 1), (r, c + 1), (r + 1, c + 1)
    ]

    return [
        (r, c) for r, c in nb_candidates
        if 0 <= r < R and 0 <= c < C
    ]

def get_removables(mx, R, C):
    removables = []
    for r, c in product(range(R), range(C)):
        if mx[r, c] in '.x':
            continue
        nb_ix = get_nbs(r, c, R, C)
        nbs = np.array([mx[r, c] for r, c in nb_ix])
        if np.sum(nbs == '@') < 4:
            removables.append((r, c))

    return removables

# PART A ========================================

accessible = get_removables(mx, R, C)
sol = len(accessible)

print(f"A :: {sol}")

# PART B ========================================

count = 0
removable = [True]
while removable:
    removable = get_removables(mx, R, C)
    count += len(removable)
    for r, c in removable:
        mx[r, c] = 'x'

print(f"B :: {count}")
