import sys
from pt1 import run

if __name__ == "__main__":
    code = sys.stdin.readlines()
    for i, line in enumerate(code):
        mod = None
        if line.startswith("nop"):
            mod = "jmp"
        elif line.startswith("jmp"):
            mod = "nop"

        if mod is not None:
            output, status = run(code[:i] + [mod + line[3:]] + code[i + 1 :])
            if status == 0:
                print(output)
