import sys
import unittest
from pt1 import count_invalid_pass


class Validator:
    def __init__(self, char, pos1, pos2):
        self.char = char
        self.pos1 = pos1 - 1
        self.pos2 = pos2 - 1

    def validate(self, password):
        return (password[self.pos1] == self.char) ^ (password[self.pos2] == self.char)


class ValidatorTestCase(unittest.TestCase):
    def test_validate_pass(self):
        v = Validator("a", 1, 3)
        self.assertTrue(v.validate("abcde"))

    def test_validate_fail_neither(self):
        v = Validator("b", 1, 3)
        self.assertFalse(v.validate("cdefg"))

    def test_validate_fail_both(self):
        v = Validator("c", 2, 9)
        self.assertFalse(v.validate("ccccccccc"))


if __name__ == "__main__":
    print(count_invalid_pass(sys.stdin.readlines(), Validator))
