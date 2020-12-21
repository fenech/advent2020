import sys


def neighbours(pos):
    x, y, z = pos
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            for k in range(z - 1, z + 2):
                if i == x and j == y and k == z:
                    continue
                yield i, j, k


def is_active(state, pos):
    return pos in state and state[pos] == 1


if __name__ == "__main__":
    z = 0
    state = {}
    for y, line in enumerate(sys.stdin):
        for x, c in enumerate(line):
            if c == "#":
                state[(x, y, z)] = 1

    for step in range(6):
        next_state = {}
        for pos in state.keys():
            active = sum(is_active(state, n) for n in neighbours(pos))
            if active == 2 or active == 3:
                next_state[pos] = 1

            for neighbour in neighbours(pos):
                if is_active(state, neighbour):
                    continue
                if sum(is_active(state, n) for n in neighbours(neighbour)) == 3:
                    next_state[neighbour] = 1

        state = next_state

    print(sum(state.values()))
