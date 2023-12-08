from utils import *
from itertools import cycle
from pickle import dump, load
from math import lcm

DAY = 8
YEAR = 2023
data = get_input(write=True, day=DAY, year=YEAR)
# data = """LR

# 11A = (11B, XXX)
# 11B = (XXX, 11Z)
# 11Z = (11B, XXX)
# 22A = (22B, XXX)
# 22B = (22C, 22C)
# 22C = (22Z, 22Z)
# 22Z = (22B, 22B)
# XXX = (XXX, XXX)"""

# ------------------------------------------------------------------------------

data = iter(data.splitlines())

l1 = next(data)
next(data)

nodes = {}
while True:
    try:
        l = next(data)
    except StopIteration:
        break

    n, dirs = l.split(" = ")
    dirs = dirs.split(", ")
    dirs[0] = dirs[0][1:]
    dirs[-1] = dirs[-1][:-1]
    nodes[n] = dirs

num_steps = 0
starts_a = [k for k in nodes if k[-1] == "A"]
cycles = load(open("inputs/day-8-cycles.pkl", "rb"))

cycle_params = []
for k, c in zip(starts_a, cycles):
    z_idxs = [i for i, x in enumerate(c) if x[0][-1] == "Z"]
    z_idx = z_idxs[0]

    repeats_back_to = c.index(c[-1])
    cycle_len = (len(c) - 1) - repeats_back_to
    cycle_params.append((z_idx, cycle_len))

    print(f"{k}: {z_idxs}, repeats to: {repeats_back_to} after {len(c) - 1} steps (cl: {cycle_len})")

# get the intersection of all hits
all_hits = []
l = lcm(*[x[1] for x in cycle_params])
for z_idx, cycle_len in cycle_params:
    start_guess = l // cycle_len

    # search around the start guess
    hits = {
        z_idx + k * cycle_len
        for k in range(start_guess - 100, start_guess + 100)
    }

    all_hits.append(hits)

ans_2 = set.intersection(*all_hits).pop()

# c = "AAA"
# num_steps = 0
# steps = cycle(l1)
# while True:
#     s = next(steps)
#     if s == "R":
#         c = nodes[c][1]
#     elif s == "L":
#         c = nodes[c][0]

#     num_steps += 1
#     if c[-1] == "Z":
#         break
# ans_1 = num_steps

# ------------------------------------------------------------------------------

submit(
    ans_1=ans_1,
    ans_2=ans_2,
    day=DAY,
    year=YEAR,
    show_rank=False
)
