from typing import List

def part1(inputs: List[int]):
    for n in inputs:
        for i in inputs:
            if n+i == 2020:
                return n*i
    return -1

def part2(inputs: List[int]):
    for n in inputs:
        for i in inputs:
            for x in inputs:
                if n+i+x == 2020:
                    return n*i*x
    return -1

f = open('./day01/input.txt', 'r')
inputs = list(map(lambda x: int(x), f.read().splitlines()))

print(f'Part 1: {part1(inputs)}')
print(f'Part 2: {part2(inputs)}')