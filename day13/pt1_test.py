import unittest
from pt1 import parse


class ParseTestCase(unittest.TestCase):
    def test_parse(self):
        timetable = """939
7,13,x,x,59,x,31,19"""
        t, buses = parse(timetable)
        self.assertEqual(t, 939)
        self.assertEqual(buses, [7, 13, 59, 31, 19])
