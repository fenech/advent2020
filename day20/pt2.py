import sys
from pt1 import parse, find_corners, edge_canonical


def rotate_90_clockwise(tile):
    return ["".join([y[i] for y in tile[-1::-1]]) for i, _ in enumerate(tile)]


def flip_horizontal(tile):
    return [t[-1::-1] for t in tile]


def strip_borders(tile):
    return [t[1:-1] for t in tile[1:-1]]


def edges(tile):
    return {
        "top": tile[0],
        "right": "".join(t[-1] for t in tile),
        "bottom": tile[-1],
        "left": "".join(t[0] for t in tile),
    }


if __name__ == "__main__":
    tiles = parse(sys.stdin.read())
    corners = find_corners(tiles)

    for i, t in tiles.items():
        tiles[i] = t.splitlines()

    # build dictionary of all shared edges, ignoring flipping/rotation for now
    edge_list = {}
    for t in tiles.keys():
        for edge in edges(tiles[t]).values():
            e = edge_canonical(edge)
            edge_list[e] = edge_list.get(e, []) + [t]

    start = corners[0]
    # find correct orientation so that the bottom + right edges are shared

    # find rhs neighbour
