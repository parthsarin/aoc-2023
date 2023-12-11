from matplotlib.path import Path
from utils import *
from pickle import dump, load

DAY = 10
YEAR = 2023
data = get_input(write=True, day=DAY, year=YEAR)
# data = """-L|F7
# 7S-7|
# L|7||
# -L-J|
# L|-JF"""

# ------------------------------------------------------------------------------

data = list(data.splitlines())
data = [list(s) for s in data]
start_loc = None
all_idxs = set()
for x in range(len(data)):
    for y in range(len(data[x])):
        all_idxs.add((x, y))
        if data[x][y] == 'S':
            start_loc = (x, y)


def get_val(grid, t):
    x, y = t
    if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[x]):
        return None
    return grid[x][y]


# walk the cycle starting at start_loc
moves = {
    "S": [(1, 0)],  # move south
    "-": [(0, 1), (0, -1)],  # move east or west
    "|": [(1, 0), (-1, 0)],  # move south or north
    "L": [(-1, 0), (0, 1)],  # move north or east
    "J": [(-1, 0), (0, -1)],  # move north or west
    "7": [(1, 0), (0, -1)],  # move south or west
    "F": [(1, 0), (0, 1)],  # move south or east
}

path = load(open("inputs/day-10-path.pkl", "rb"))
# curr = start_loc
# path = [curr]
# keep_exploring = True
# while keep_exploring:
#     move_opts = moves[get_val(data, curr)]
#     for move in move_opts:
#         next_pos = (curr[0] + move[0], curr[1] + move[1])

#         # looped back to the start
#         if next_pos == path[0]:
#             keep_exploring = False
#             break

#         if next_pos in path:
#             # don't loop back on yourself
#             continue

#         # otherwise accept this move
#         path.append(next_pos)
#         curr = next_pos
#         break

dist_forward = list(range(len(path)))
dist_backward = list(range(1, len(path) + 1))[::-1]
dists = [min(dist_forward[i], dist_backward[i]) for i in range(len(path))]

# dump(path, open("inputs/day-10-path.pkl", "wb"))

ans_2 = 0
poly = Path(path)
for x in range(len(data)):
    for y in range(len(data[x])):
        if (x, y) in path:
            continue
        if poly.contains_point((x, y)):
            ans_2 += 1

# ------------------------------------------------------------------------------

submit(
    ans_1=ans_1,
    ans_2=ans_2,
    day=DAY,
    year=YEAR,
    show_rank=False
)
