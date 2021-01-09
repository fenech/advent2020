from collections import deque

cups = deque(map(int, "586439172"))


def move(cups):
    current = cups.popleft()
    cups.append(current)

    pickup = [cups.popleft() for _ in range(3)]

    dest = int(current) - 1
    while True:
        try:
            idx = cups.index(dest)
            for i in range(3):
                cups.insert(idx + 1 + i, pickup[i])
            break
        except ValueError:
            dest -= 1
            if dest < min(cups):
                dest = max(cups)


if __name__ == "__main__":
    for step in range(100):
        move(cups)

    while cups.index(1) != 0:
        cups.rotate()

    print("".join(map(str, list(cups)[1:])))
