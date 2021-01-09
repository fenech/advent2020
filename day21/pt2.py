import sys
from pt1 import parse


if __name__ == "__main__":
    allergens = parse(sys.stdin)

    while not all(len(a) == 1 for a in allergens.values()):
        for a, i in allergens.items():
            if len(i) == 1:
                for other_a in allergens.keys():
                    if other_a != a:
                        allergens[other_a] -= i
    print(allergens)
    print(",".join([allergens[a].pop() for a in sorted(allergens)]))
