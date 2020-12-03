import sys
import unittest
import re


class Validator:
    def __init__(self, char, min, max):
        self.char = char
        self.min = min
        self.max = max

    def __eq__(self, other):
        return (
            self.char == other.char and self.min == other.min and self.max == other.max
        )

    def validate(self, password):
        return self.min <= password.count(self.char) <= self.max


class ValidatorTestCase(unittest.TestCase):
    def test_validate_pass(self):
        v = Validator("a", 1, 3)
        self.assertTrue(v.validate("abcde"))

    def test_validate_fail(self):
        v = Validator("b", 1, 3)
        self.assertFalse(v.validate("cdefg"))


def parse_pass(line, validator):
    m = re.match(r"(\d+)-(\d+) (\w): (\w+)", line)
    return validator(m.group(3), int(m.group(1)), int(m.group(2))), m.group(4)


class ParsePassTestCase(unittest.TestCase):
    def test_parse_line(self):
        v = Validator
        self.assertEqual(parse_pass("1-3 a: abcde", v), (v("a", 1, 3), "abcde"))


def count_invalid_pass(pass_list, validator):
    count = 0
    for line in pass_list:
        v, password = parse_pass(line, validator)
        count += v.validate(password)
    return count


class CountInvalidPassTestCase(unittest.TestCase):
    def setUp(self):
        self.input = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]

    def test_count_invalid_pass(self):
        self.assertEqual(count_invalid_pass(self.input, Validator), 2)


if __name__ == "__main__":
    print(count_invalid_pass(sys.stdin.readlines(), Validator))
