#!/usr/local/bin/python3
import InputHelper as IH
import regex as regex
from collections import defaultdict

class Cart():
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.vectors = [
            (0, -1),
            (1, 0),
            (0, 1),
            (-1, 0)
        ]
        self.next_turn = -1

    def move(self):
        vector = self.vectors[self.direction]
        self.x += vector[0]
        self.y += vector[1]
            
    def set_dir(self, map):
        cell = map[self.y][self.x]

        if cell == '+':
            self.direction = (self.direction + self.next_turn) % 4
            self.next_turn = (((self.next_turn + 1) + 1) % 3) - 1
        elif cell == '-' or cell == '|':
            return
        elif self.direction == 0:
            if cell == '\\':
                self.direction = 3
            elif cell == '/':
                self.direction = 1
        elif self.direction == 1:
            if cell == '\\':
                self.direction = 2
            elif cell == '/':
                self.direction = 0
        elif self.direction == 2:
            if cell == '\\':
                self.direction = 1
            elif cell == '/':
                self.direction = 3
        elif self.direction == 3:
            if cell == '\\':
                self.direction = 0
            elif cell == '/':
                self.direction = 2

def solve1(map):
    carts = find_carts(map)

    second = 0
    col = None

    while True:
        for cart in carts:
            cart.move()
            cart.set_dir(map)

        col = colision_check(carts)
        if col:
            break

        second += 1
    return col

def solve2(map):
    carts = find_carts(map)

    second = 0
    col = None

    while True:
        for cart in carts:
            cart.move()
            cart.set_dir(map)

        col = True
        while col:
            col = colision_check2(carts)
            printed_tick = False
            if col:
                if not printed_tick:
                    print()
                    print(second)
                    printed_tick = True
                print('Collison at ', col[0].x, col[0].y)
                carts.remove(col[0])
                carts.remove(col[1])
                removed = True

        if len(carts) == 1:
            return carts[0].x, carts[0].y

        second += 1
    return col, second

def colision_check(carts):
    for outer_index, outer_cart in enumerate(carts):
        for inner_index, inner_cart in enumerate(carts):
            if outer_index != inner_index and outer_cart.x == inner_cart.x and outer_cart.y == inner_cart.y:
                return outer_cart.x, outer_cart.y

    return None

def colision_check2(carts):
    for outer_index, outer_cart in enumerate(carts):
        for inner_index, inner_cart in enumerate(carts):
            if outer_index != inner_index and outer_cart.x == inner_cart.x and outer_cart.y == inner_cart.y:
                return outer_cart, inner_cart

    return None

def find_carts(map):
    carts = []

    # 0 is up
    for y, row in enumerate(map):
        for x, cell in enumerate(row):
            if cell == r'^':
                carts.append(Cart(x, y, 0))
                map[y][x] = '|'
            if cell == r'>':
                carts.append(Cart(x, y, 1))
                map[y][x] = '-'
            if cell == r'v':
                carts.append(Cart(x, y, 2))
                map[y][x] = '|'
            if cell == r'<':
                carts.append(Cart(x, y, 3))
                map[y][x] = '-'

    return carts

def convert(lines):
    return [convert_line(line) for line in lines]

def convert_line(line):
    # Step C must be finished before step A can begin.

    result = [''] * len(line) 

    for index, char in enumerate(line):
        result[index] = char

    return result

data = IH.InputHelper(13).readlines()
#print(data)

test_data = [
    '/->-\\        ',
    '|   |  /----\\',
    '| /-+--+-\  |',
    '| | |  | v  |',
    '\-+-/  \-+--/',
    '  \------/  '
]

test_data2 = [
    '/>-<\  ',
    '|   |  ',
    '| /<+-\\',
    '| | | v',
    '\>+</ |',
    '  |   ^',
    '  \<->/'
]


#print(test_data)
#print(convert(test_data))
#print('7,3 ', solve1(convert(test_data)))

#print([int(line) for line in data[0].split(' ')])

#print('138', solve1([int(line) for line in '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'.split(' ')]))
#print(solve1([int(line) for line in data[0].split(' ')]))

#print('Part 1 ', solve1(convert(data)))
print('6,4 ', solve2(convert(test_data2)))
print('Part 2 ', solve2(convert(data)))

#print('15', solve2(convert(test_data), 0, 2))

#print('Part 2 ', solve2(convert(data), 60, 5))
