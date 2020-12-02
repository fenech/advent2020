import sys
from array import array
from itertools import combinations
from functools import reduce
from operator import mul
import unittest

def find_tuple(expenses, n):
  for tup in combinations(expenses, n):
    if sum(tup) == 2020:
      print(tup)
      return reduce(mul, tup) 

class FindPairTestCase(unittest.TestCase):
  def setUp(self):
    self.expenses = [
      1721,
      979,
      366,
      299,
      675,
      1456,
    ]

  def test_find_pair(self):
    self.assertEqual(find_tuple(self.expenses, 3), 241861950)

if __name__ == "__main__":
  expenses = map(int, sys.stdin.read().splitlines())
  print(find_tuple(expenses, 3))
