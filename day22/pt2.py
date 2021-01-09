import sys
from collections import deque
from pt1 import hand, block


def score(hand):
    h = hand.copy()
    h.reverse()
    return sum(i * c for i, c in enumerate(h, start=1))


def game(p1, p2):
    p1_seen = set()
    p2_seen = set()

    while len(p1) and len(p2):
        c1 = p1.popleft()
        c2 = p2.popleft()

        if tuple(p1) in p1_seen and tuple(p2) in p2_seen:
            return 1, score(p1)

        p1_seen.add(tuple(p1))
        p2_seen.add(tuple(p2))

        if c1 <= len(p1) and c2 <= len(p2):
            winner, _ = game(deque(list(p1)[:c1]), deque(list(p2)[:c2]))
        elif c1 > c2:
            winner = 1
        elif c2 > c1:
            winner = 2

        if winner == 1:
            p1.extend([c1, c2])
        else:
            p2.extend([c2, c1])

    return (1, score(p1)) if len(p1) else (2, score(p2))


if __name__ == "__main__":
    p1 = hand(block(sys.stdin))
    p2 = hand(block(sys.stdin))
    print(game(p1, p2))
