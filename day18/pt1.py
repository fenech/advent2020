import sys


def add(form, total=0):
    while len(form):
        c, form = form[0], form[1:]
        if c == "(":
            form, t = calculate(form)
            return form, t + total
        elif c.isnumeric():
            return form, total + int(c)


def mul(form, total=0):
    while len(form):
        c, form = form[0], form[1:]
        if c == "(":
            form, t = calculate(form)
            return form, t * total
        elif c.isnumeric():
            return form, total * int(c)


def calculate(form, total=0):
    while len(form):
        c, form = form[0], form[1:]
        if c == "(":
            form, total = calculate(form, total)
        elif c == ")":
            return form, total
        elif c == "+":
            form, total = add(form, total)
        elif c == "*":
            form, total = mul(form, total)
        elif c.isnumeric() and total == 0:
            total = int(c)
    return total


if __name__ == "__main__":
    calculate("1 + (2 * 3) + (4 * (5 + 6))")

    total = 0
    for line in sys.stdin:
        total += calculate(line)

    print(total)
