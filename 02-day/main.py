import numpy as np

raw = open('data/input.txt', 'r').read().split(',')

class Interval:
    def __init__(self, data):
        a, b = data.strip().split('-')
        self.a = int(a)
        self.b = int(b)

    def sum_invalid(self, x):
        which_invalid = (self.a <= x) & (x <= self.b)
        return np.sum(x[which_invalid])

maxlen = (max(len(i.strip()) for i in raw) - 1) // 2
intervals = [Interval(i) for i in raw]

# PART A ==================================================

bad_ids = np.array([int(str(n)*2) for n in range(1, 10**(maxlen // 2 + 1))])

sol = sum(i.sum_invalid(bad_ids) for i in intervals)
print(f"A :: {sol}")

# PART B ==================================================

bad1 = [1111111*n for n in range(1, 9)]
bad2 = [int(str(n)*2) for n in range(1, 10**(maxlen // 2 + 1))]
bad3 = [int(str(n)*3) for n in range(1, 10**(maxlen // 3 + 1))]
bad4 = [int(str(n)*4) for n in range(1, 10**(maxlen // 4 + 1))]
bad5 = [int(str(n)*5) for n in range(1, 10**(maxlen // 5 + 1))]
bad_ids = np.array(list(set(bad1 + bad2 + bad3 + bad4 + bad5)))

sol = sum(i.sum_invalid(bad_ids) for i in intervals)
print(f"B :: {sol}")
