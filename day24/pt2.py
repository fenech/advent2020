import sys
from pt1 import flip


def neighbours(x, y):
    yield (x - 1, y - 1)
    yield (x + 1, y - 1)
    yield (x - 1, y + 1)
    yield (x + 1, y + 1)
    yield (x - 2, y)
    yield (x + 2, y)


def hex_coords(tiles):
    min_x = min(x for x, _ in tiles)
    max_x = max(x for x, _ in tiles)
    min_y = min(y for _, y in tiles)
    max_y = max(y for _, y in tiles)

    if min_y % 2:
        min_y -= 1
    if min_x % 2:
        min_x -= 1

    for y in range(min_y - 2, max_y + 2):
        for x in range(min_x - 2 + y % 2, max_x + 2, 2):
            yield x, y


if __name__ == "__main__":
    tiles = flip(sys.stdin)
    print(sum(tiles.values()))

    for day in range(100):
        new = {}
        for tile in hex_coords(tiles):
            black = tiles.get(tile, 0)
            blacks = sum(tiles.get(b, 0) for b in neighbours(*tile))
            if black and (blacks == 0 or blacks > 2):
                new[tile] = False
            elif not black and (blacks == 2):
                new[tile] = True
            else:
                new[tile] = black
        tiles = new
        print(sum(tiles.values()))
