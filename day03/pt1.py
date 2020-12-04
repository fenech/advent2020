import sys
import unittest

trees = [
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#",
]


def is_tree(trees, x, y):
    width = len(trees[0])
    return trees[y][x % width] == "#"


class TestCaseIsTree(unittest.TestCase):
    def test_simple_not_tree(self):
        self.assertFalse(is_tree(trees, 0, 0))

    def test_simple_is_tree(self):
        self.assertTrue(is_tree(trees, 2, 0))
        self.assertTrue(is_tree(trees, 3, 0))
        self.assertTrue(is_tree(trees, 0, 1))

    def test_map_repeat(self):
        self.assertFalse(is_tree(trees, 11, 0))
        self.assertFalse(is_tree(trees, 12, 0))
        self.assertTrue(is_tree(trees, 13, 0))
        self.assertTrue(is_tree(trees, 14, 0))


def collisions(trees, dx, dy):
    x = y = 0
    count = 0
    while y < len(trees):
        count += is_tree(trees, x, y)
        x += dx
        y += dy

    return count


class TestCaseCollisions(unittest.TestCase):
    def test_collisions(self):
        self.assertEqual(collisions(trees, 3, 1), 7)


if __name__ == "__main__":
    trees = sys.stdin.read().splitlines()
    print(collisions(trees, 3, 1))
