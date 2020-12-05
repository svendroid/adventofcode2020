import unittest
from day3 import part1
from day3 import part2


class Day3Test(unittest.TestCase):

    exampleInput = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""

    def test_part1(self):
        self.assertEqual(part1(self.exampleInput), 7)

    def test_part2(self):
        self.assertEqual(part2(self.exampleInput), 336)


if __name__ == '__main__':
    unittest.main()
