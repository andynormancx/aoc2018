#!/usr/local/bin/python3
import InputHelper as IH
import regex as regex
from collections import defaultdict

class Point:
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def Move(self):
        self.x = self.x + self.dx
        self.y = self.y + self.dy

    def MoveBack(self):
        self.x = self.x - self.dx
        self.y = self.y - self.dy

def solve1and2(points):
    lastYSpread = (max(points, key = lambda p: p.y)).y - (min(points, key = lambda p: p.y)).y

    second = 0
    while True:
        for point in points:
            point.Move()
        
        newYSpread = (max(points, key = lambda p: p.y)).y - (min(points, key = lambda p: p.y)).y

        if newYSpread > lastYSpread:
            break
        
        lastYSpread = newYSpread
        second += 1

    for point in points:
        point.MoveBack()

    print_message(points)

    return lastYSpread, second

def print_message(points):
    display = defaultdict(int)
    minX = min(points, key = lambda p: p.x).x
    minY = min(points, key = lambda p: p.y).y
    maxX = max(points, key = lambda p: p.x).x
    maxY = max(points, key = lambda p: p.y).y

    for point in points:
        display[(point.x, point.y)] = 1

    for y in range(minY, maxY + 1):
        line = ''
        for x in range(minX, maxX + 1):
            if display[(x, y)] == 1:
                line += '#'
            else:
                line += '.'
        else:
            print(line)

def convert(lines):
    return [convert_line(line) for line in lines]

def convert_line(line):
    # position=<-52992,  10809> velocity=< 5, -1>
    ints = [int(x) for x in regex.findall(r'-?\d+', line)]

    return Point(ints[0], ints[1], ints[2], ints[3])

data = IH.InputHelper(10).readlines()
#print(data)

test_data = [
    'position=< 9,  1> velocity=< 0,  2>',
    'position=< 7,  0> velocity=<-1,  0>',
    'position=< 3, -2> velocity=<-1,  1>',
    'position=< 6, 10> velocity=<-2, -1>',
    'position=< 2, -4> velocity=< 2,  2>',
    'position=<-6, 10> velocity=< 2, -2>',
    'position=< 1,  8> velocity=< 1, -1>',
    'position=< 1,  7> velocity=< 1,  0>',
    'position=<-3, 11> velocity=< 1, -2>',
    'position=< 7,  6> velocity=<-1, -1>',
    'position=<-2,  3> velocity=< 1,  0>',
    'position=<-4,  3> velocity=< 2,  0>',
    'position=<10, -3> velocity=<-1,  1>',
    'position=< 5, 11> velocity=< 1, -2>',
    'position=< 4,  7> velocity=< 0, -1>',
    'position=< 8, -2> velocity=< 0,  1>',
    'position=<15,  0> velocity=<-2,  0>',
    'position=< 1,  6> velocity=< 1,  0>',
    'position=< 8,  9> velocity=< 0, -1>',
    'position=< 3,  3> velocity=<-1,  1>',
    'position=< 0,  5> velocity=< 0, -1>',
    'position=<-2,  2> velocity=< 2,  0>',
    'position=< 5, -2> velocity=< 1,  2>',
    'position=< 1,  4> velocity=< 2,  1>',
    'position=<-2,  7> velocity=< 2, -2>',
    'position=< 3,  6> velocity=<-1, -1>',
    'position=< 5,  0> velocity=< 1,  0>',
    'position=<-6,  0> velocity=< 2,  0>',
    'position=< 5,  9> velocity=< 1, -2>',
    'position=<14,  7> velocity=<-2,  0>',
    'position=<-3,  6> velocity=< 2, -1>'
]

#print(test_data)

#print('Part 1 ', solve1(convert(data)))

#print([int(line) for line in data[0].split(' ')])


#print('HI ', solve1and2(convert(test_data)))
print('Part 1 and 2 ', solve1and2(convert(data)))

#print('15', solve2(convert(test_data), 0, 2))

#print('Part 2 ', solve2(convert(data), 60, 5))
