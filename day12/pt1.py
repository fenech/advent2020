import sys


def north(state, value):
    state["y"] -= value


def south(state, value):
    state["y"] += value


def east(state, value):
    state["x"] += value


def west(state, value):
    state["x"] -= value


directions = {0: "N", 90: "E", 180: "S", 270: "W"}


def left(state, value):
    state["d"] -= value


def right(state, value):
    state["d"] += value


def forward(state, value):
    table[directions[state["d"] % 360]](state, value)


table = {
    "N": north,
    "S": south,
    "E": east,
    "W": west,
    "L": left,
    "R": right,
    "F": forward,
}


def act(state, line):
    action = line[0]
    value = int(line[1:])
    table[action](state, value)


if __name__ == "__main__":
    state = {"d": 90, "x": 0, "y": 0}

    for line in sys.stdin:
        act(state, line)

    print(abs(state["x"]) + abs(state["y"]))
