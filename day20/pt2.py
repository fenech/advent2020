import sys
import math
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


def actions():
    for _ in range(3):
        yield rotate_90_clockwise
    yield flip_horizontal
    for _ in range(4):
        yield rotate_90_clockwise


if __name__ == "__main__":
    tiles = parse(sys.stdin.read())
    corners = find_corners(tiles)

    for i, t in tiles.items():
        tiles[i] = t.splitlines()

    width = height = int(math.sqrt(len(tiles)))

    edge_list = {}
    for t in tiles.keys():
        for edge in edges(tiles[t]).values():
            e = edge_canonical(edge)
            edge_list[e] = edge_list.get(e, []) + [t]

    current_id = str(corners[0])
    ids = {(0, 0): current_id}
    image = {}

    for y in range(height):
        for x in range(width):
            if x == 0 and y > 0:
                pos = (x, y - 1)
                neighbour = image[pos]
                neighbour_id = ids[pos]
                edge = edge_canonical(edges(neighbour)["bottom"])
                current_id = (set(edge_list[edge]) - set([neighbour_id])).pop()
            elif x > 0:
                pos = (x - 1, y)
                neighbour = image[pos]
                neighbour_id = ids[pos]
                edge = edge_canonical(edges(neighbour)["right"])
                current_id = (set(edge_list[edge]) - set([neighbour_id])).pop()

            ids[(x, y)] = current_id
            current_tile = tiles[current_id]
            for action in actions():
                current_edges = edges(current_tile)
                left = current_edges["left"]
                top = current_edges["top"]

                if (
                    (x == 0 and len(edge_list[edge_canonical(left)]) == 1)
                    or (x > 0 and left == edges(image[(x - 1, y)])["right"])
                ) and (
                    (y == 0 and len(edge_list[edge_canonical(top)]) == 1)
                    or (y > 0 and top == edges(image[(x, y - 1)])["bottom"])
                ):
                    image[(x, y)] = current_tile
                    break

                current_tile = action(current_tile)

    stripped_image = {
        k: v for k, v in map(lambda x: (x[0], strip_borders(x[1])), image.items())
    }
    lines = len(stripped_image[(0, 0)])

    combined_image = []
    for ty in range(height):
        combined_image.extend(
            [
                "".join([stripped_image[(tx, ty)][line] for tx in range(width)])
                for line in range(lines)
            ]
        )

    print("\n".join(combined_image))
