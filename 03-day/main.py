raw = open('data/input.txt', 'r').readlines()
data = [[int(i) for i in line.strip()] for line in raw]

# PART A ========================================

def max_jolt_a(line):
    max1 = max(line[:-1])
    ix_max = line.index(max1)
    max2 = max(line[ix_max + 1:])
    return 10*max1 + max2

maxes = [max_jolt_a(line) for line in data]
sol = sum(maxes)
print(f"A :: {sol}")

# PART B ========================================

def max_jolt_b(line):

    joltage = []
    jolts = line.copy()
    for i in range(12):
        maxval = max(jolts[:i - 11]) if i < 11 else max(jolts)
        ix = jolts.index(maxval)
        jolts = jolts[ix + 1:]
        joltage.append(maxval)

    return int(''.join([str(n) for n in joltage]))

maxes = [max_jolt_b(line) for line in data]
sol = sum(maxes)
print(f"B :: {sol}")
