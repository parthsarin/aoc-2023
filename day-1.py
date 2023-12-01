from utils import *

DAY = 1
YEAR = 2023
data = get_input(write=True, day=DAY, year=YEAR)

# ------------------------------------------------------------------------------
ans_2 = 0
digits = ["", "one", "two", "three", "four",
          "five", "six", "seven", "eight", "nine"]
for line in data.split('\n'):
    locs = {}
    for digit in digits:
        if digit == "":
            continue
        first_idx = line.find(digit)
        last_idx = line.rfind(digit)
        digit = str(digits.index(digit))
        if first_idx != -1:
            locs[first_idx] = digit

        if last_idx != -1:
            locs[last_idx] = digit
    for i, ch in enumerate(line):
        if ch.isdigit():
            locs[i] = str(ch)

    # earliest, latest
    print(locs)
    earliest = min(locs.keys())
    latest = max(locs.keys())
    i = locs[earliest] + locs[latest]
    ans_2 += int(i)


# ------------------------------------------------------------------------------

submit(
    ans_1=ans_1,
    ans_2=ans_2,
    day=DAY,
    year=YEAR,
    show_rank=False
)
