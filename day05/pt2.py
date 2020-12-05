import sys
from pt1 import seat_id

if __name__ == "__main__":
    tickets = list(map(seat_id, sys.stdin.readlines()))
    print(set(range(min(tickets), max(tickets) + 1)).difference(tickets))
