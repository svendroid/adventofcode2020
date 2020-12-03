def part1(inputs):
    return _slopeCount(inputs)


def part2(inputs):
    result = _slopeCount(inputs, x_step=1, y_step=1)
    result *= _slopeCount(inputs, x_step=3, y_step=1)
    result *= _slopeCount(inputs, x_step=5, y_step=1)
    result *= _slopeCount(inputs, x_step=7, y_step=1)
    result *= _slopeCount(inputs, x_step=1, y_step=2)
    return result


def _slopeCount(inputs, x_step=3, y_step=1):
    x = 0
    trees = 0
    for l in inputs.splitlines()[y_step::y_step]:
        x = (x + x_step) % len(l)
        if l[x] == '#':
            trees += 1
        #print(l[:x] + '0' + l[x+1:])
    return trees


f = open('./day03/input.txt', 'r')
inputs = f.read()

print(f'Part 1: {part1(inputs)}')
print(f'Part 2: {part2(inputs)}')
