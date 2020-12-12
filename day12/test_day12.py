import unittest
import day12


class DayTest(unittest.TestCase):

    example = """F10
N3
F7
R90
F11"""

    def test_part1(self):
        self.assertEqual(day12.part1(self.example), 25)

    def test_part2(self):
        self.assertEqual(day12.part2(self.example), 286)

if __name__ == '__main__':
    unittest.main()
