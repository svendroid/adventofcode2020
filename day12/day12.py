from unittest.main import main

def part1(input: str):
    instructions = input.splitlines()

    directions = ['E', 'S', 'W', 'N']
    direction = 0
    x = 0
    y = 0
    for instr in instructions:    
        cmd = instr[0]
        value = int(instr[1:])
        if cmd == 'R':
            direction = int((direction + value/90)%4)
            continue
        elif cmd == 'L':
            direction = int((direction - value/90)%4)
            continue
        elif cmd == 'F':
            cmd = directions[direction]        
        
        if cmd == 'N':
            y += value
        elif cmd == 'E':
            x += value
        elif cmd == 'S':
            y -= value
        elif cmd == 'W':
            x -= value

    return abs(x) + abs(y)

def part2(input: str):
    instructions = input.splitlines()

    directions = ['E', 'S', 'W', 'N']
    direction = 0

    x = 10
    y = 1

    pos_x = 0
    pos_y = 0

    for instr in instructions:
        print(instr)  
        cmd = instr[0]
        value = int(instr[1:])
        if cmd == 'R':
            for _ in range(int((value/90)%4)):
                temp_x = x
                temp_y = y
                x = temp_y
                y = -temp_x
        elif cmd == 'L':
            for _ in range(int((value/90)%4)):
                temp_x = x
                temp_y = y
                x = -temp_y
                y = temp_x
        elif cmd == 'F':
            cmd = directions[direction]
            pos_x += value * x
            pos_y += value * y 
        elif cmd == 'N':
            y += value
        elif cmd == 'E':
            x += value
        elif cmd == 'S':
            y -= value
        elif cmd == 'W':
            x -= value

        print(f'waypoint ({x},{y})')
        print(f'pos ({pos_x},{pos_y})')

    return abs(pos_x) + abs(pos_y)

if __name__ == "__main__":
    f = open('./day12/input.txt')
    input = f.read()

    print(f'Part 1: {part1(input)}')
    print(f'Part 2: {part2(input)}')