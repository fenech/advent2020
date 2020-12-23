import sys
import re


def add(form):
    while True:
        m = re.search(r"(\d+) \+ (\d+)", form)
        if m is None:
            return form
        form = (
            form[: m.start()] + str(int(m.group(1)) + int(m.group(2))) + form[m.end() :]
        )


def mul(form):
    while True:
        m = re.search(r"(\d+) \* (\d+)", form)
        if m is None:
            return form
        form = (
            form[: m.start()] + str(int(m.group(1)) * int(m.group(2))) + form[m.end() :]
        )


def calculate(form):
    while True:
        m = re.search(r"\([^()]+\)", form)

        if m is None:
            form = add(form)
            form = mul(form)
            return form
        else:
            s = m.start()
            e = m.end()
            form = form[:s] + calculate(form[s + 1 : e - 1]) + form[e:]


if __name__ == "__main__":
    total = 0
    for line in sys.stdin:
        total += int(calculate(line))
    print(total)
