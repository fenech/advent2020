import sys
from itertools import accumulate
from pt1 import xmas as xmaspt1


def crack(data, target):
    for i, _ in enumerate(data):
        for j, c in enumerate(accumulate(data[i:])):
            if c == target:
                sl = data[i : i + j]
                return min(sl) + max(sl)
            elif c > target:
                continue


if __name__ == "__main__":
    data = list(map(int, sys.stdin.readlines()))
    target = xmaspt1(data, 25)
    print(crack(data, target))
