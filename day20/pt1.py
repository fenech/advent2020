import sys
import re


def parse(tiles):
    parsed = {}
    for m in re.finditer(r"Tile (\d+):\n", tiles):
        tile = tiles[m.end() : m.end() + 110]
        parsed[m.group(1)] = tile

    return parsed


def edge_canonical(e):
    return e if e[-1::-1] > e else e[-1::-1]


def edges(tile):
    edges = {}
    edges["top"] = tile[0:10]
    edges["left"] = tile[0::11]
    edges["right"] = tile[9::11]
    edges["bottom"] = tile[-11:-1]

    for e in edges.values():
        yield edge_canonical(e)


def find_corners(tiles):
    edge_list = {}
    for t in tiles.keys():
        for e in edges(tiles[t]):
            edge_list[e] = edge_list.get(e, []) + [t]

    border = sorted([e[0] for e in edge_list.values() if len(e) == 1])
    return [int(f[0]) for f in zip(border, border[1:]) if f[0] == f[1]]


if __name__ == "__main__":
    tiles = parse(sys.stdin.read())
    corners = find_corners(tiles)
    print(corners[0] * corners[1] * corners[2] * corners[3])
