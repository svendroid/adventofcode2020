from collections import Counter
from collections import defaultdict

from numpy.lib.function_base import diff

def part1(input: str):
    adapters = [int(x) for x in input.splitlines()]

    adapters.append(0)
    adapters.append(max(adapters)+3)

    adapters = sorted(adapters)

    diffs = [y - x for x,y in zip(adapters, adapters[1:])]
    #print(diffs)

    c = Counter(diffs)

    return c[1] * c[3]

def part2(input: str):
    adapters = [int(x) for x in input.splitlines()]
    adapters.append(0)
    adapters.append(max(adapters)+3)
    adapters = sorted(adapters)

    # played arround quite some time with getting a nice way to use the list of diffs from part 1, finally I gave up and used a long and cumbersome recursive solution. Afterwards found this quite elegant solution which does not use a math formula und is really short on reddit. https://www.reddit.com/r/adventofcode/comments/ka8z8x/2020_day_10_solutions/gfcxuxf/?utm_source=reddit&utm_medium=web2x&context=3
    paths = defaultdict(int)
    paths[0] = 1
    for adapter in adapters:
        first = True
        for diff in range(1, 4):
            next_adapter = adapter + diff
            if next_adapter in adapters:
                paths[next_adapter] += paths[adapter]
    
    return paths[max(adapters)]


if __name__ == "__main__":
    f = open('./day10/input.txt', 'r')
    input = f.read()
    print(f'Part1: {part1(input)}')
    print(f'Part2: {part2(input)}')