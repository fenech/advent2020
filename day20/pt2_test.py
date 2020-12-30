import unittest
import pt2


class RotateTestCase(unittest.TestCase):
    def test_rotate_3x3(self):
        tile = ["123", "456", "789"]
        expected = ["741", "852", "963"]
        self.assertEqual(pt2.rotate_90_clockwise(tile), expected)


class FlipTestCase(unittest.TestCase):
    def test_flip_3x3(self):
        tile = ["123", "456", "789"]
        expected = ["321", "654", "987"]
        self.assertEqual(pt2.flip_horizontal(tile), expected)


class StripTestCase(unittest.TestCase):
    def test_strip_3x3(self):
        tile = ["123", "456", "789"]
        expected = ["5"]
        self.assertEqual(pt2.strip_borders(tile), expected)


class EdgesTestCase(unittest.TestCase):
    def test_edges_3x3(self):
        tile = ["123", "456", "789"]
        self.assertEqual(
            pt2.edges(tile),
            {"top": "123", "right": "369", "bottom": "789", "left": "147"},
        )
