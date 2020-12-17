import sys
import re

if __name__ == "__main__":
    mem = {}
    for line in sys.stdin:
        m = re.match(r"mask = (\w+)", line)
        if m is not None:
            mask = m.group(1)
            mask_or = int(mask.replace("X", "0"), 2)
            mask_and = int(mask.replace("X", "1"), 2)
            continue
        m = re.match(r"mem\[(\d+)] = (\d+)", line)
        if m is not None:
            addr = m.group(1)
            val = (int(m.group(2)) | mask_or) & mask_and
            mem[addr] = val

    print(sum(m for m in mem.values()))
