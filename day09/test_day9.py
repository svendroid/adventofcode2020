import unittest
import day9

class Day9Test(unittest.TestCase):

    exampleInput = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""

    example_2="""37
1
33
42
17
34
27
44
26
39
3
43
30
22
9
38
7
28
21
4
50
14
35
12
5
6
71
8
15
10
11
13
16
53
17
20
18
19
23
24
9
22
25
26
21
27
28
14
67
"""

    def test_part1(self):
        self.assertEqual(day9.findInvalid(self.exampleInput), 127)

    def test_example_part1(self):
        self.assertEqual(day9.findInvalid(self.example_2, 25), -1)

    def test_part2(self):
        self.assertEqual(day9.part2(self.exampleInput, invalid_n = 127),62)

if __name__ == '__main__':
    unittest.main()
