from utils import *
import numpy as np

DAY = 11
YEAR = 2023
data = get_input(write=True, day=DAY, year=YEAR)
# data = """...#......
# .......#..
# #.........
# ..........
# ......#...
# .#........
# .........#
# ..........
# .......#..
# #...#....."""

# ------------------------------------------------------------------------------

data = data.splitlines()
data = [list(x) for x in data]
data = np.array(data)

empty_rows = []
empty_cols = []
for r in range(len(data)):
    if all(data[r, :] == "."):
        empty_rows.append(r)
for c in range(len(data[0])):
    if all(data[:, c] == "."):
        empty_cols.append(c)

galaxies = []
for r in range(len(data)):
    for c in range(len(data[0])):
        if data[r, c] == "#":
            galaxies.append((r, c))

ans_2 = 0
for a in range(len(galaxies)):
    for b in range(a + 1, len(galaxies)):
        g1 = galaxies[a]
        g2 = galaxies[b]

        x1, x2 = min(g1[0], g2[0]), max(g1[0], g2[0])
        y1, y2 = min(g1[1], g2[1]), max(g1[1], g2[1])

        # count the number of empty rows between the two galaxies
        x2 += (1000000 - 1) * sum(x1 < e < x2 for e in empty_rows)
        y2 += (1000000 - 1) * sum(y1 < e < y2 for e in empty_cols)

        d = (x2 - x1) + (y2 - y1)
        ans_2 += d

# ------------------------------------------------------------------------------

submit(
    ans_1=ans_1,
    ans_2=ans_2,
    day=DAY,
    year=YEAR,
    show_rank=False
)
