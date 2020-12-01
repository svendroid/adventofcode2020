import unittest
from day1 import part1
from day1 import part2

class Day1Test(unittest.TestCase):

    def test_part1(self):
        exampleInput = [1721, 979, 366, 299, 675, 1456]
        self.assertEqual(part1(exampleInput), 514579)
    
    def test_part2(self):
        exampleInput = [1721, 979, 366, 299, 675, 1456]
        self.assertEqual(part2(exampleInput), 241861950)

if __name__ == '__main__':
    unittest.main()
