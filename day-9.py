from utils import *
import numpy as np
from math import isclose

DAY = 9
YEAR = 2023
data = get_input(write=True, day=DAY, year=YEAR)
# data = """0 3 6 9 12 15
# 1 3 6 10 15 21
# 10 13 16 21 30 45"""

# ------------------------------------------------------------------------------

ans_2 = 0
data = data.splitlines()
for p in data:
    y = [int(x) for x in p.split()]
    x = list(range(len(y)))

    # subtract until we get all zeros
    deg = 0
    diffs = y.copy()
    extrap = [diffs[0]]
    while True:
        diffs = [diffs[i + 1] - diffs[i] for i in range(len(diffs) - 1)]
        if all(x == 0 for x in diffs):
            break
        deg += 1
        extrap.append(diffs[0])

    # go backwards and fill in the previous row
    curr = 0
    for v in extrap[::-1]:
        curr = v - curr

    ans_2 += curr

# ------------------------------------------------------------------------------

submit(
    ans_1=ans_1,
    ans_2=ans_2,
    day=DAY,
    year=YEAR,
    show_rank=False
)
