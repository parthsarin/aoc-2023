from utils import *
from collections import defaultdict

DAY = 5
YEAR = 2023
data = get_input(write=True, day=DAY, year=YEAR)
# data = """seeds: 79 14 55 13

# seed-to-soil map:
# 50 98 2
# 52 50 48

# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15
# 57 0 1

# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4

# water-to-light map:
# 88 18 7
# 18 25 70

# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13

# temperature-to-humidity map:
# 0 69 1
# 1 0 69

# humidity-to-location map:
# 60 56 37
# 56 93 4"""

data = iter(data.splitlines())

# ------------------------------------------------------------------------------

curr = [int(x) for x in next(data).split(": ")[1].split()]
curr = [(s, s + l - 1) for s, l in zip(curr[::2], curr[1::2])]
# for start, length in zip(curr[::2], curr[1::2]):
#     start + length

# get all maps
next(data)
next_level = []
while True:
    # update curr with next_level
    curr += next_level
    next_level = []
    print(curr)

    try:
        l = next(data)
    except StopIteration:
        break

    if 'map' in l:
        print(l)
        l = next(data)
        while l:
            a, b, c = l.split()
            a, b, c = int(a), int(b), int(c)
            dst_range = (a, a+c - 1)
            src_range = (b, b+c - 1)

            max_iter = len(curr)
            for _ in range(max_iter):
                r = curr.pop(0)
                overlap = (max(r[0], src_range[0]),
                           min(r[1], src_range[1]))

                if overlap[0] > overlap[1]:
                    # no overlap
                    curr.append(r)
                    continue

                new_min = (overlap[0] - b) + a
                new_max = (overlap[1] - b) + a
                next_level.append((new_min, new_max))

                # we need to resolve these ranges
                if r[0] <= overlap[0] - 1:
                    curr.append((r[0], overlap[0] - 1))
                if r[1] >= overlap[1] + 1:
                    curr.append((overlap[1] + 1, r[1]))

            try:
                l = next(data)
            except StopIteration:
                break

ans_2 = min([r[0] for r in curr] + [r[1] for r in curr])

# ------------------------------------------------------------------------------

submit(
    ans_1=ans_1,
    ans_2=ans_2,
    day=DAY,
    year=YEAR,
    show_rank=False
)
