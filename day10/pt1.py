import sys

adapters = sorted(map(int, sys.stdin.readlines()))

curr = 0
ones = 0
threes = 1
for a in adapters:
    if a == curr + 1:
        curr = a
        ones += 1
    elif a == curr + 2:
        curr = a
    elif a == curr + 3:
        curr = a
        threes += 1

print(ones * threes)
