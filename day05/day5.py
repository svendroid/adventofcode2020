

def part1(input: str):
    l = [parseSeat(num)['id'] for num in input.splitlines()]
    return max(l)

def parseSeat(input: str):
    print(input + '------------------')
    row = _parse(input[:7])
    col = _parse(input[-3:], low='L', end=7)
    seatId = row * 8 + col

    return {'col':col, 'row':row, 'id':seatId}

def _parse(inp: str, low = 'F', end=127):
    print(inp + '----')
    start = 0
    for l in inp:
        d = (end-start)/2
        if l == low:
            end = end - round(d)
        else:
            start = start + round(d)
        print(f'{l}: {start}, {end}')
    
    if inp[-1] == low:
        return start
    else:
        return end

def part2(input: str):
    seats = sorted([parseSeat(num)['id'] for num in input.splitlines()])
    missing = [x for x in range(seats[0], seats[-1]+1) if x not in seats]
    return missing

f = open('./day05/input.txt', 'r')
input = f.read()

print(f'Part 1: {part1(input)}')
print(f'Part 2: {part2(input)}')