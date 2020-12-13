import sys
import re


def parse(timetable):
    m = list(map(int, re.findall(r"\d+", timetable, re.MULTILINE)))
    if len(m):
        return m[0], m[1:]


def bus_arrives(t, buses):
    for b in buses:
        if t % b == 0:
            return b


if __name__ == "__main__":
    t0, buses = parse(sys.stdin.read())
    t = t0
    while True:
        b = bus_arrives(t, buses)
        if b is not None:
            break
        t += 1
    print((t - t0) * b)
