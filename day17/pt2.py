import sys
from itertools import product


def neighbours(pos):
    return filter(lambda x: x != pos, product(*((c - 1, c, c + 1) for c in pos)))


def is_active(state, pos):
    return pos in state and state[pos] == 1


if __name__ == "__main__":
    z = w = 0
    state = {}
    for y, line in enumerate(sys.stdin):
        for x, c in enumerate(line):
            if c == "#":
                state[(x, y, z, w)] = 1

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
