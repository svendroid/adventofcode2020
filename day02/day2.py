import re

def part1(inputs: str):
    passwords = [_parse(re.split('[-:\s]+', x)) for x in inputs.splitlines()]
    validCount = 0
    for p in passwords:
        count = p['pass'].count(p['letter'])
        if count >= p['min'] and count <= p['max']:
            validCount += 1

    return validCount

def part2(inputs: str):
    passwords = [_parse(re.split('[-:\s]+', x)) for x in inputs.splitlines()]
    validCount = 0
    for p in passwords:
        pas = str(p['pass'])
        pos1 = pas[p['min']-1] == p['letter']
        pos2 = pas[p['max']-1] == p['letter']
        
        if (pos1 and not pos2) or (pos2 and not pos1):
            validCount += 1

    return validCount

def _parse(x):
    return {'min': int(x[0]), 'max': int(x[1]), 'letter': x[2], 'pass': x[3]}

f = open('./day02/input.txt', 'r')
input = f.read()
print(f'Part 1: {part1(input)}')
print(f'Part 2: {part2(input)}')