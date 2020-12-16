import sys
import re
from functools import reduce
from operator import mul


def parse(timetable):
    buses = []
    m = re.split(r"\n|,", timetable)
    for i, bus in enumerate(m[1:]):
        if re.match(r"\d", bus):
            buses.append({"offset": -i, "bus": int(bus)})
    return buses


def chinese_remainder(n, a):
    s = 0
    prod = reduce(mul, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        s += a_i * euclid_extended(p, n_i) * p
    return s % prod


def euclid_extended(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q, r = divmod(a, b)
        a, b = b, r
        x0, x1 = x1 - q * x0, x0
    return x1 % b0


if __name__ == "__main__":
    buses = parse(sys.stdin.read())
    print(chinese_remainder([b["bus"] for b in buses], [b["offset"] for b in buses]))
