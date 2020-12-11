import sys


def combos(run):
    """
    run of 2 => 1 combination
    4 5

    run of 3 => 2 combinations
    4 5 6
    4 X 6

    run of 4 => 4 combinations
    4 5 6 7
    4 X 6 7
    4 5 X 7
    4 X X 7

    runs of 5 => 7 combinations
    4 5 6 7 8
    4 X 6 7 8
    4 5 X 7 8
    4 5 6 X 8
    4 X X 7 8
    4 5 X X 8
    4 X 6 X 8
    """
    return [1, 1, 1, 2, 4, 7][run]


adapters = sorted(map(int, sys.stdin.readlines()))
run = 1
total = 1

for a1, a2 in zip([0] + adapters, adapters):
    if a2 - a1 == 1:
        run += 1
    else:
        total *= combos(run)
        run = 1
total *= combos(run)

print(total)
