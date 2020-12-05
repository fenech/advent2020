import sys
import unittest


def seat_id(ticket):
    return int(ticket.translate(str.maketrans("FLBR", "0011")), 2)


class TestSeatId(unittest.TestCase):
    def test_seat_id(self):
        self.assertEqual(seat_id("FBFBBFFRLR"), 357)


if __name__ == "__main__":
    print(max(map(seat_id, sys.stdin.readlines())))
