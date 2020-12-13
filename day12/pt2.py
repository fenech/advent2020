import sys


def north(state, value):
    state["wy"] -= value


def south(state, value):
    state["wy"] += value


def east(state, value):
    state["wx"] += value


def west(state, value):
    state["wx"] -= value


def left(state, value):
    rot = value % 360
    if rot == 90:
        state["wx"], state["wy"] = state["wy"], -state["wx"]
    elif rot == 180:
        state["wx"], state["wy"] = -state["wx"], -state["wy"]
    elif rot == 270:
        state["wx"], state["wy"] = -state["wy"], state["wx"]


def right(state, value):
    left(state, -value)


def forward(state, value):
    for _ in range(value):
        state["x"] += state["wx"]
        state["y"] += state["wy"]


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
    state = {"d": 90, "wx": 10, "wy": -1, "x": 0, "y": 0}

    for line in sys.stdin:
        act(state, line)

    print(abs(state["x"]) + abs(state["y"]))
