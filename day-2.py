from utils import *
from collections import defaultdict

DAY = 2
YEAR = 2023
data = get_input(write=True, day=DAY, year=YEAR)

# ------------------------------------------------------------------------------

existing_cubes = dict(zip(['red', 'green', 'blue'], [12, 13, 14]))
powers = []
for line in data.split('\n'):
    if not line.strip():
        continue
    gid = int(line.split(":")[0].split(" ")[1])
    games = line.split(":")[1].strip().split(';')
    games = [g.strip() for g in games]

    games = [g.split(', ') for g in games]
    all_games = defaultdict(list)
    for g in games:
        game_d = {}
        for e in g:
            q, color = e.split(" ")
            all_games[color].append(int(q))

    for color in all_games:
        all_games[color] = max(all_games[color])

    power = all_games['red'] * all_games['green'] * all_games['blue']
    powers.append(power)

ans_2 = sum(powers)

# ------------------------------------------------------------------------------

submit(
    ans_1=ans_1,
    ans_2=ans_2,
    day=DAY,
    year=YEAR,
    show_rank=False
)
