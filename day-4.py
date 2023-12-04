from utils import *
from collections import defaultdict

DAY = 4
YEAR = 2023
data = get_input(write=True, day=DAY, year=YEAR)
# data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
# """

# ------------------------------------------------------------------------------

card_vals = {}
card_inst = defaultdict(int)
for i, line in enumerate(data.split('\n'), 1):
    if not line:
        continue

    c = line.split(":")[1]
    c = c.strip()
    c = c.split(' | ')

    winning = c[0]
    winning = [int(x) for x in winning.split()]
    have = [int(x) for x in c[1].split()]

    overlap = len(set(have) & set(winning))
    # if not overlap:
    #     continue

    # value = 2 ** (overlap - 1)
    # card_vals[i] = value

    card_inst[i] += 1
    for offset in range(1, overlap + 1):
        card_inst[i + offset] += card_inst[i]


ans_2 = sum(card_inst.values())
# ------------------------------------------------------------------------------

submit(
    ans_1=ans_1,
    ans_2=ans_2,
    day=DAY,
    year=YEAR,
    show_rank=False
)
