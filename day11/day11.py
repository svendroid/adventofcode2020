from types import prepare_class
from unittest import result
import numpy as np
from numpy.core.defchararray import count, index

def part1(input: str):
    map = np.array([list(x) for x in input.splitlines()])

    round = make_round(map)
    changes = -1
    count = 1
    while changes != 0:
        round = make_round(round['map'])
        changes = round['changes']
        count += 1
    
    unique, counts = np.unique(round['map'], return_counts=True)
    return dict(zip(unique, counts))['#']

def prettyPrint(round):
    print(f'changes: {round["changes"]}')
    txt = ''
    for l in round['map']:
        a_str = ''.join([str(x) for x in l])
        txt = txt + a_str + '\n'
    return txt

def make_round(map):
    result = np.copy(map)
    changes = 0
    for row in range(map.shape[0]):
        for col in range(map.shape[1]):
            adj = []
            indices = [row-1, col-1],[row-1, col],[row-1, col+1],[row, col-1],[row, col+1],[row+1, col-1],[row+1, col],[row+1, col+1]
            for i in indices:
                    #print(f'i: {i}')
                    if (i[0] >= 0 and i[0] < map.shape[0]) and (i[1] >= 0 and i[1] < map.shape[1]):
                        adj.append(map[i[0], i[1]])

            #print(f'{row}:{col}')
            #print(adj)    
            if map[row, col] == 'L':
                # empty seat
                if adj.count('#') == 0:
                    #print('to occupied')
                    #print(adj)
                    result[row, col] = '#'
                    changes += 1
            elif map[row, col] == '#':
                if adj.count('#') >= 4:
                    #print('to empty')
                    result[row, col] = 'L'
                    changes += 1

    return {"map": result, "changes": changes}

def make_round_2(map):
    result = np.copy(map)
    changes = 0
    for row in range(map.shape[0]):
        for col in range(map.shape[1]):
            right = findSeat(map, row, col, 0, 1)
            left = findSeat(map, row, col, 0, -1)
            up = findSeat(map, row, col, -1, 0)
            down = findSeat(map, row, col, 1, 0)
            down_right = findSeat(map, row, col, 1, 1)
            down_left = findSeat(map, row, col, 1, -1)
            up_left = findSeat(map, row, col, -1, -1)
            up_right = findSeat(map, row, col, -1, 1)
            
            seats = [right, left, up, down, down_right, down_left, up_left, up_right]
            #print(row, col)
            #print(seats)
            if map[row, col] == 'L':
                # empty seat
                if seats.count('#') == 0:
                    #print('to occupied')
                    #print(adj)
                    result[row, col] = '#'
                    changes += 1
            elif map[row, col] == '#':
                if seats.count('#') >= 5:
                    #print('to empty')
                    result[row, col] = 'L'
                    changes += 1
    
    return {"map": result, "changes": changes}

def findSeat(map, row,col,row_dir,col_dir):
    seat = 'X'
    #print(f'{row, col}')
    row = row+row_dir
    col = col+col_dir
    while (seat == 'X' or seat == '.') and (row >= 0 and row < map.shape[0]) and (col >= 0 and col < map.shape[1]):
        #print(f'find{row},{col}')
        seat = map[row,col]
        row = row+row_dir
        col = col+col_dir
        #print(seat)
    return seat

def part2(input: str):
    map = np.array([list(x) for x in input.splitlines()])

    round = make_round_2(map)
    #print(prettyPrint(round))
    changes = -1
    count = 1
        
    while changes != 0:
        #print(f'Round {count}')
        round = make_round_2(round['map'])
        changes = round['changes']
        #print(prettyPrint(round))
        count += 1
    
    unique, counts = np.unique(round['map'], return_counts=True)
    return dict(zip(unique, counts))['#']



if __name__ == '__main__':
    example = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

    print(f'Part 1 Example: {part1(example)}')
    print(f'Part 2 Example: {part2(example)}')
    
    f = open('./day11/input.txt', 'r')
    input = f.read()

    print(f'Part 1: {part1(input)}')    
    print(f'Part 2: {part2(input)}')
