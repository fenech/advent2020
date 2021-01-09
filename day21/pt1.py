import sys
import re


def parse(lines):
    allergens = {}
    ingredients = []

    for line in lines:
        p = line.index("contains")
        i = re.findall(r"\w+", line[:p])
        ingredients.extend(i)
        for a in re.findall(r"\w+", line[p + 8 :]):
            if a in allergens:
                allergens[a] &= set(i)
            else:
                allergens[a] = set(i)

    print(allergens)
    candidates = set()
    for a in allergens.values():
        candidates |= a

    count = sum(i not in candidates for i in ingredients)
    print(count)
    return allergens


if __name__ == "__main__":
    parse(sys.stdin)
