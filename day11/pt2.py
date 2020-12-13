import sys


def find_adjacent(seats, x, y):
    directions = (
        (x, y) for x in range(-1, 2) for y in range(-1, 2) if x != 0 or y != 0
    )
    for dx, dy in directions:
        px = x
        py = y
        try:
            while True:
                px += dx
                py += dy
                pos = (px, py)
                if seats[pos] != ".":
                    yield pos
                    break
        except KeyError:
            continue


def parse_seats(file):
    seats = {}
    adjacent = {}
    for y, line in enumerate(file):
        for x, s in enumerate(line.strip()):
            seats[(x, y)] = s

    for x, y in seats.keys():
        adjacent[(x, y)] = list(find_adjacent(seats, x, y))
    return seats, adjacent


def occupied(seats, x, y):
    s = (x, y)
    try:
        return seats[s] == "#"
    except KeyError:
        return False


def is_floor(seats, x, y):
    return seats[(x, y)] == "."


def sittable(seats, adjacent, x, y):
    if is_floor(seats, x, y):
        return False

    return all(not occupied(seats, x, y) for x, y in adjacent[(x, y)])


def leaveable(seats, adjacent, x, y):
    if is_floor(seats, x, y):
        return False

    return sum(occupied(seats, x, y) for x, y in adjacent[(x, y)]) >= 5


def simulate(seats, adjacent):
    changed = False
    new = {}
    for pos, seat in seats.items():
        if seat == ".":
            continue
        if seat == "L" and sittable(seats, adjacent, *pos):
            changed = True
            new[pos] = "#"
        elif seat == "#" and leaveable(seats, adjacent, *pos):
            changed = True
            new[pos] = "L"
        else:
            new[pos] = seat
    return new, changed


if __name__ == "__main__":
    seats, adjacent = parse_seats(sys.stdin)
    steps = 0
    changed = True
    while changed:
        steps += 1
        seats, changed = simulate(seats, adjacent)
    print(sum(occupied(seats, x, y) for x, y in seats.keys()))
