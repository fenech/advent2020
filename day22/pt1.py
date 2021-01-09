import sys
from collections import deque


def block(lines):
    for line in lines:
        if line == "\n":
            break
        yield line


def hand(lines):
    return deque(int(card) for i, card in enumerate(lines) if i > 0)


if __name__ == "__main__":
    p1 = hand(block(sys.stdin))
    p2 = hand(block(sys.stdin))

    while len(p1) and len(p2):
        c1 = p1.popleft()
        c2 = p2.popleft()
        if c1 > c2:
            p1.extend([c1, c2])
        elif c2 > c1:
            p2.extend([c2, c1])

    winner = p1 if len(p1) else p2
    winner.reverse()
    print(sum(i * c for i, c in enumerate(winner, start=1)))
