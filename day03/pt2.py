import sys
from functools import reduce
from operator import mul

from pt1 import collisions

if __name__ == "__main__":
    trees = sys.stdin.read().splitlines()
    directions = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]
    print(reduce(mul, map(lambda d: collisions(trees, *d), directions)))
