import unittest
from day2 import part1
from day2 import part2

class Day2Test(unittest.TestCase):

    def test_part1(self):
        exampleInput = "1-3 a: abcde\n1-3 b: cdefg\n2-9 c: ccccccccc\n";
        self.assertEqual(part1(exampleInput), 2)

    def test_part2(self):
        exampleInput = "1-3 a: abcde\n1-3 b: cdefg\n2-9 c: ccccccccc\n";
        self.assertEqual(part2(exampleInput), 1)

if __name__ == '__main__':
    unittest.main()
