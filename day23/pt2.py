from pt1 import cups

if __name__ == "__main__":
    cups = list(cups)
    next_cups = [0] * (len(cups) + 1)

    for prev, cur in zip(cups, cups[1:]):
        next_cups[prev] = cur

    next_cups[cups[-1]] = len(cups) + 1
    next_cups += list(range(len(next_cups) + 1, 1000000 + 2))
    next_cups[-1] = cups[0]

    curr = cups[0]
    for step in range(10000000):
        c1 = next_cups[curr]
        c2 = next_cups[c1]
        c3 = next_cups[c2]
        picked = set([c1, c2, c3])

        next_cups[curr] = next_cups[c3]

        dest = curr - 1 if curr > 1 else 1000000
        while dest in picked:
            dest -= 1
            if dest < 1:
                dest = 1000000

        next_cups[dest], next_cups[c3] = c1, next_cups[dest]
        curr = next_cups[curr]

    print(next_cups[1] * next_cups[next_cups[1]])
