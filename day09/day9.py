from typing import List

def findInvalid(input: str, preamble_length: int = 5):
    nums = [int(x) for x in input.splitlines()]

    for i, x in enumerate(nums[preamble_length:], preamble_length):
        preamble = [p for p in nums[i-preamble_length:i]]
        valid = False
        print(f'preamble: {preamble}')
        for p in preamble:
            d = abs(x - p)
            if d in preamble and d is not p and d is not x:
                valid = True
        if not valid:
            return x
    return -1

def part2(input: str, invalid_n):
    nums = [int(x) for x in input.splitlines()]

    nums = nums[:nums.index(invalid_n)]


    for n_idx in range(len(nums)):
        sum = 0
        for i, x in enumerate(nums[n_idx:],n_idx):
            sum += x
            if sum == invalid_n:
                values = nums[n_idx:i+1]
                print((n_idx, i+1))
                print(values)
                check = 0
                for v in values:
                    check += v
                return min(values) + max(values)
            elif sum > invalid_n:
                continue
    return -1

if __name__ == '__main__':
    f = open('./day09/input.txt', 'r')
    input = f.read()
    print(f'Part 1: {findInvalid(input, preamble_length=25)}')
    print(f'Part 2: {part2(input, invalid_n=50047984)}')
