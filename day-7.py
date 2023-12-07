from utils import *
from collections import defaultdict

DAY = 7
YEAR = 2023
data = get_input(write=True, day=DAY, year=YEAR)
# data = """32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483"""
non_j = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]

# ------------------------------------------------------------------------------

hands = defaultdict(list)
for l in data.splitlines():
    h, b = l.split()
    b = int(b)

    matchings = []
    for c in non_j:
        print(c, end=" ")
        h, _ = l.split()
        h = h.replace("J", c)

        n_diff = len(set(h))
        if n_diff == 1:
            # five of a kind
            matchings.append((7, c))

        elif n_diff == 2:
            counts = sorted([h.count(c) for c in h])
            if counts == [1, 4, 4, 4, 4]:
                # four of a kind
                matchings.append((6, c))

            elif counts == [2, 2, 3, 3, 3]:
                # full house
                matchings.append((5, c))

        elif n_diff == 3:
            counts = sorted([h.count(c) for c in h])
            if counts == [1, 2, 2, 2, 2]:
                # two pair
                matchings.append((3, c))
            elif counts == [1, 1, 3, 3, 3]:
                # three of a kind
                matchings.append((4, c))

        elif n_diff == 4:
            # one pair
            matchings.append((2, c))

        elif n_diff == 5:
            # high card
            matchings.append((1, c))

    # get the best matching
    idx, c = max(matchings, key=lambda x: x[0])
    h, _ = l.split()
    hands[idx].append((h, b))
    print(f"chose c = {c} for hand = {idx}")

# break ties based on index of card in cards
for k in hands:
    hands[k] = sorted(
        hands[k],
        key=lambda x: tuple(cards.index(c) for c in x[0])
    )

# reaggregate into one list
all_hands = []
for idx in (7, 6, 5, 4, 3, 2, 1):
    all_hands.extend(hands[idx])

# ranks are highest -> 1, multiply with bids
ranks = range(len(all_hands), 0, -1)
ans_2 = 0
for r, (h, b) in zip(ranks, all_hands):
    ans_2 += r * b

# ------------------------------------------------------------------------------

submit(
    ans_1=ans_1,
    ans_2=ans_2,
    day=DAY,
    year=YEAR,
    show_rank=False
)
