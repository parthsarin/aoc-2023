from utils import *
from collections import defaultdict

DAY = 3
YEAR = 2023
data = get_input(write=True, day=DAY, year=YEAR)
# data = """467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598.."""

# ------------------------------------------------------------------------------

nums = defaultdict(list)
x = 0
for line in data.split('\n'):
    curr_num = ''
    cur_num_coords = []
    for y, ch in enumerate(line):
        if ch.isdigit():
            curr_num += ch
            cur_num_coords.append((x, y))
        elif curr_num:
            # reset
            nums[curr_num].append(cur_num_coords)
            curr_num = ''
            cur_num_coords = []
    if curr_num:
        nums[curr_num].append(cur_num_coords)

    x += 1


def surrounding(x, y):
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == dy == 0:
                continue
            yield x+dx, y+dy


# find the non-digit symbols
x = 0
gear_ratios = []
for line in data.split("\n"):
    for y, ch in enumerate(line):
        # if ch.isdigit() or ch == '.':
        #     continue
        if ch != "*":
            continue

        s = set(surrounding(x, y))
        adjacent_nums = set()
        for n, coords in nums.items():
            for c in coords:
                if s & set(c):
                    adjacent_nums.add((int(n), tuple(c)))
        if len(adjacent_nums) == 2:
            a, b = adjacent_nums.pop(), adjacent_nums.pop()
            gear_ratios.append(a[0] * b[0])

    x += 1

ans_2 = sum(gear_ratios)

# ------------------------------------------------------------------------------

submit(
    ans_1=ans_1,
    ans_2=ans_2,
    day=DAY,
    year=YEAR,
    show_rank=False
)
