import sys
import re
from itertools import product


def all_addr(addr, mask):
    addr = "{:036b}".format(addr)
    masked = ""
    for a, m in zip(addr, mask):
        if m == "0":
            masked += a
        else:
            masked += m

    indices = [i for i, c in enumerate(masked) if c == "X"]
    for p in product("01", repeat=len(indices)):
        m = masked
        for i, c in enumerate(p):
            idx = indices[i]
            m = m[:idx] + c + m[idx + 1 :]
        yield m


if __name__ == "__main__":
    mem = {}
    for line in sys.stdin:
        m = re.match(r"mask = (\w+)", line)
        if m is not None:
            mask = m.group(1)
            continue
        m = re.match(r"mem\[(\d+)] = (\d+)", line)
        if m is not None:
            for addr in all_addr(int(m.group(1)), mask):
                mem[addr] = int(m.group(2))

    print(sum(m for m in mem.values()))
