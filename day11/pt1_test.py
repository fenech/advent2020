import unittest
from pt1 import parse_seats, sittable


class ParseSeatsTestCase(unittest.TestCase):
    def test_parse_seats(self):
        example = ["L.", ".L"]
        self.assertEqual(
            parse_seats(example), {(0, 0): "L", (0, 1): ".", (1, 0): ".", (1, 1): "L"}
        )


class SittableTestCase(unittest.TestCase):
    def test_sittable(self):
        seats = {(0, 0): "L", (0, 1): ".", (1, 0): ".", (1, 1): "L"}
        self.assertTrue(sittable(seats, 0, 0))
        self.assertFalse(sittable(seats, 0, 1))
        self.assertFalse(sittable(seats, 1, 0))
        self.assertTrue(sittable(seats, 1, 1))
