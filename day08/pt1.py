import sys


def run(code):
    acc = 0
    seen = set()
    line = 0
    while line < len(code):
        if line in seen:
            return acc, 1
        seen.add(line)

        inst, val = code[line].split()
        if inst == "nop":
            line += 1
        elif inst == "acc":
            acc += int(val)
            line += 1
        elif inst == "jmp":
            line += int(val)

    return acc, 0


if __name__ == "__main__":
    print(run(sys.stdin.readlines()))
