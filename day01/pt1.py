import sys
from array import array
import unittest

def find_pair(expenses):
  arr = array('i', sorted(expenses))
  for i, x in enumerate(arr):
    for y in arr[i::-1]:
      if x + y == 2020:
        print(x, y)
        return x * y

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
    self.assertEqual(find_pair(self.expenses), 514579)

if __name__ == "__main__":
  expenses = map(int, sys.stdin.read().splitlines())
  print(find_pair(expenses))
