import sys


def parse_seats(file):
    seats = {}
    for y, line in enumerate(file):
        for x, s in enumerate(line.strip()):
            seats[(x, y)] = s
    return seats


def occupied(seats, x, y):
    s = (x, y)
    try:
        return seats[s] == "#"
    except KeyError:
        return False


def adjacent(x, y):
    yield (x, y + 1)
    yield (x, y - 1)
    yield (x - 1, y - 1)
    yield (x - 1, y)
    yield (x - 1, y + 1)
    yield (x + 1, y - 1)
    yield (x + 1, y)
    yield (x + 1, y + 1)


def is_floor(seats, x, y):
    return seats[(x, y)] == "."


def sittable(seats, x, y):
    if is_floor(seats, x, y):
        return False

    return all(not occupied(seats, x, y) for x, y in adjacent(x, y))


def leaveable(seats, x, y):
    if is_floor(seats, x, y):
        return False

    return sum(occupied(seats, x, y) for x, y in adjacent(x, y)) >= 4


def simulate(seats):
    changed = False
    new = {}
    for pos, seat in seats.items():
        if seat == ".":
            continue
        if seat == "L" and sittable(seats, *pos):
            changed = True
            new[pos] = "#"
        elif seat == "#" and leaveable(seats, *pos):
            changed = True
            new[pos] = "L"
        else:
            new[pos] = seat
    return new, changed


if __name__ == "__main__":
    seats = parse_seats(sys.stdin)
    steps = 0
    changed = True
    while changed:
        steps += 1
        seats, changed = simulate(seats)
    print(sum(occupied(seats, x, y) for x, y in seats.keys()))
