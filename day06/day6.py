import re
from typing import List, Set

def part1(input: str):
    groups = parseGroups(input)
    count = 0
    for g in groups:
        print(g)
        count += len(g)

    return count

def parseGroups(input: str):
    lines = re.split('\s', input)
    group: Set = set()
    for l in lines:
        if(len(l) == 0):
            yield group
            group = set()
        else:
            group.update(list(l))
    yield group

def part2(input: str):
    groups = parseGroups2(input)
    total_count = 0
    for g in groups:
        count = {}
        for p in g:
            for c in p:
                count[c] = count.setdefault(c,0) + 1
        print(count)
        for k, v in count.items():
            if v == len(g):
                print(f'FOUND {k}: {v}')
                total_count +=1
        print('TOTAL: ' + str(total_count))

    return total_count

def parseGroups2(input: str):
    lines = re.split('\s', input)
    group: List = []
    for l in lines:
        if(len(l) == 0):
            yield group
            group = []
        else:
            group.append(l)
    yield group


f = open('./day06/input.txt', 'r')
input = f.read()

print(f'Part 1: {part1(input)}')
print(f'Part 2: {part2(input)}')