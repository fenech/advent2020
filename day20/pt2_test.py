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


class SeaMonsterTestCase(unittest.TestCase):
    def test_sea_monster(self):
        self.assertTrue(pt2.sea_monster(pt2.monster, 0, 0))

    def test_all_dots(self):
        image = ["............................" for line in pt2.monster]
        self.assertFalse(pt2.sea_monster(image, 0, 0))

    def test_all_hashes(self):
        image = ["############################" for line in pt2.monster]
        self.assertTrue(pt2.sea_monster(image, 0, 0))
