import unittest
import day10


class DayTest(unittest.TestCase):

    exampleInput = """16
10
15
5
1
11
7
19
6
12
4"""

    def test_part1(self):
        self.assertEqual(day10.part1(self.exampleInput), 35)

    exampleInputLrg = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""

    def test_part1_larger_example(self):
        self.assertEqual(day10.part1(self.exampleInputLrg), 220)

    def test_part2(self):
        self.assertEqual(day10.part2(self.exampleInput), 8)

    def test_part2_lrg_example(self):
        self.assertEqual(day10.part2(self.exampleInputLrg), 19208)

if __name__ == '__main__':
    unittest.main()
