import unittest
import day5

class Day5Test(unittest.TestCase):

    def test_parseSeat(self):
        self.assertEqual(day5.parseSeat('FBFBBFFRLR'), {'row': 44, 'col': 5, 'id': 357})
    def test_parseSeat_1(self):
        self.assertEqual(day5.parseSeat('BFFFBBFRRR'), {'row': 70, 'col': 7, 'id': 567})
    def test_parseSeat_2(self):
        self.assertEqual(day5.parseSeat('FFFBBBFRRR'), {'row': 14, 'col': 7, 'id': 119})
    def test_parseSeat_3(self):
        self.assertEqual(day5.parseSeat('BBFFBBFRLL'), {'row': 102, 'col': 4, 'id': 820})
    def test_part1(self):
        self.assertEqual(day5.part1('BFFFBBFRRR\nFFFBBBFRRR\nBBFFBBFRLL'), 820)

if __name__ == '__main__':
    unittest.main()
    