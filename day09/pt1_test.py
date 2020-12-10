import unittest
from pt1 import xmas

example = [
    35,
    20,
    15,
    25,
    47,
    40,
    62,
    55,
    65,
    95,
    102,
    117,
    150,
    182,
    127,
    219,
    299,
    277,
    309,
    576,
]


class XmasTestCase(unittest.TestCase):
    def test_xmas(self):
        self.assertEqual(xmas(example, 5), 127)
