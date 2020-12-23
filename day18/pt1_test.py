import unittest
from pt1 import calculate


class CalculateTestCase(unittest.TestCase):
    def test_no_parens(self):
        self.assertEqual(calculate("1 + 2 * 3 + 4 * 5 + 6"), 71)

    def test_parens(self):
        self.assertEqual(calculate("1 + (2 * 3) + (4 * (5 + 6))"), 51)

    def test_nested(self):
        self.assertEqual(
            calculate("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"), 13632
        )

    def test_other(self):
        examples = {
            "2 * 3 + (4 * 5)": 26,
            "5 + (8 * 3 + 9 + 3 * 4 * 3)": 437,
            "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))": 12240,
        }

        for line, expected in examples.items():
            self.assertEqual(calculate(line), expected)
