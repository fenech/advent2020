import unittest
from pt1 import run


class RunTestCase(unittest.TestCase):
    def test_run(self):
        self.input = [
            "nop +0",
            "acc +1",
            "jmp +4",
            "acc +3",
            "jmp -3",
            "acc -99",
            "acc +1",
            "jmp -4",
            "acc +6",
        ]

        self.assertEqual(run(self.input), (5, 1))
