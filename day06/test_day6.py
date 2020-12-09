import unittest
import day6


class Day6Test(unittest.TestCase):

    exampleInput = """abc

a
b
c

ab
ac

a
a
a
a

b"""

    def test_part1(self):
        self.assertEqual(day6.part1(self.exampleInput), 11)

    def test_part2(self):
        self.assertEqual(day6.part2(self.exampleInput), 6)

if __name__ == '__main__':
    unittest.main()
