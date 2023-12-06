from utils import *
from functools import reduce

DAY = 6
YEAR = 2023
data = get_input(write=True, day=DAY, year=YEAR)
# data = """Time:      7  15   30
# Distance:  9  40  200"""

# ------------------------------------------------------------------------------

def mul(a, b):
    return a * b

data = data.splitlines()
time = int(data[0].split(":")[1].replace(" ", ""))
dist = int(data[1].split(":")[1].replace(" ", ""))
print(time, dist)
exit()


all_wins = []
for t, d in zip(times, dists):
    num_wins = 0
    for speed in range(t + 1):
        dist = (t - speed) * speed
        if dist > d:
            num_wins += 1
    all_wins.append(num_wins)

ans_1 = reduce(mul, all_wins)

# ------------------------------------------------------------------------------

submit(
    ans_1=ans_1,
    ans_2=ans_2,
    day=DAY,
    year=YEAR,
    show_rank=False
)
