from functools import reduce

raw = open('data/input.txt', 'r').readlines()
int_raw = [line.strip() for line in raw if '-' in line]
food = {int(line) for line in raw if line.strip().isdigit()}

class Interval:
    def __init__(self, a, b):
        self.a, self.b = int(a), int(b)

    @property
    def width(self):
        return self.b - self.a + 1

    def contains(self, x):
        return self.a <= x <= self.b

    def has_overlap(self, other):
        return (self.a <= other.a <= self.b) or (self.a <= other.b <= self.b)

    def merge(self, other):
        return Interval(min(self.a, other.a), max(self.b, other.b))

intervals = [Interval(*i.split('-')) for i in int_raw]

# PART A ========================================

n_fresh = 0
for i in intervals:
    found_fresh = set()
    for f in food:
        if i.contains(f):
            n_fresh += 1
            found_fresh.add(f)
    food = food - found_fresh

print(f"A :: {n_fresh}")

# PART B ========================================

def forward_merge(ints):
    ints = ints.copy()
    int_curr = ints.pop(0)

    # find all joints
    ix_mergeable = [i for i, ivl in enumerate(ints) if int_curr.has_overlap(ivl)]
    ivl_mergeable = [ints[ix] for ix in ix_mergeable]

    # find joined int
    int_new = reduce(lambda u, v: u.merge(v), ivl_mergeable, int_curr)

    # remove pieces from list
    ints = [ivl for i, ivl in enumerate(ints) if i not in ix_mergeable]

    return ints + [int_new]

def merge_round(ints):
    ints = ints.copy()
    L = len(ints)
    for i in range(L):
        ints = forward_merge(ints)
    return ints

ints = intervals.copy()
L_old = len(ints)
L_new = -1
while L_old != L_new:
    L_old = L_new
    ints = merge_round(ints)
    L_new = len(ints)

sol = sum(i.width for i in ints)
print(f"B :: {sol}")
