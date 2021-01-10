import sys
import re


def move(line):
    x = y = 0

    for m in re.finditer(r"[ns]?[we]", line):
        move = m.group(0)
        if move == "nw":
            x -= 1
            y -= 1
        elif move == "ne":
            x += 1
            y -= 1
        elif move == "sw":
            x -= 1
            y += 1
        elif move == "se":
            x += 1
            y += 1
        elif move == "w":
            x -= 2
        elif move == "e":
            x += 2

    return x, y


if __name__ == "__main__":
    tiles = {}
    for line in sys.stdin:
        pos = move(line)
        tiles[pos] = not tiles.get(pos, False)

    print(sum(t for t in tiles.values()))
