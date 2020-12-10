import sys
from itertools import combinations


def xmas(data, preamble):
    for i, number in enumerate(data[preamble:]):
        if not any(sum(x) == number for x in combinations(data[i:], 2)):
            return number


if __name__ == "__main__":
    data = list(map(int, sys.stdin.readlines()))
    print(xmas(data, 25))
