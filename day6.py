#!/usr/local/bin/python3
import InputHelper as IH
import regex as regex
from collections import defaultdict
from functools import reduce

def solve1(input):
    cords = {}
    finite_cords  = set()

    single_shorts = defaultdict(int)

    for cord in input:
        cords[cord] = dict()


    max_x = reduce(lambda one, two: max([one, two]), list(map(lambda x:x[0], input)))
    min_x = reduce(lambda one, two: min([one, two]), list(map(lambda x:x[0], input)))
    max_y = reduce(lambda one, two: max([one, two]), list(map(lambda x:x[1], input)))
    min_y = reduce(lambda one, two: min([one, two]), list(map(lambda x:x[1], input)))

    for cord in input:
        if is_finite(cord, max_x, min_x, max_y, min_y):
            finite_cords.add(cord)

    for x in range(min_x, max_x):
        for y in range(min_y, max_y):
            shorts = shortest_to((x, y), input)
            if len(shorts) == 1:
                single_shorts[shorts[0][0]] += 1

    finite_shorts = dict(filter(lambda x: x[0] in finite_cords, single_shorts.items()))
    
    return max(finite_shorts.items(), key = lambda x:x[1])[1]
    #for outer in input:
    #    for inner in input:
    #        if outer is not inner:
    #            cords[outer][inner] = calc_dist(inner, outer)
    #return 0

def shortest_to(point, cords):
    distances = {}
    for cord in cords:
        dist = calc_dist(point, cord)
        if dist != 0:
            distances[cord] = dist

    min_dist = min(distances.values())

    working = list(filter(lambda x: x[1] == min_dist, distances.items()))

    return list(filter(lambda x: x[1] == min_dist, distances.items()))

def is_finite(cord, max_x, min_x, max_y, min_y):
    return cord[0] > min_x and cord[0] < max_x and cord[1] > min_y and cord[1] < max_y

def calc_dist(one, two):
    return abs(one[0] - two[0]) + abs(one[1] - two [1])

def convert(lines):
    return [convert_line(line) for line in lines]

def convert_line(line):
    vals = list(map(lambda x:int(x), line.split(',')))
    return vals[0], vals[1]

data = IH.InputHelper(6).readlines()
#print(data)
#print(convert(data))

test_data = '1, 1\n1, 6\n8, 3\n3, 4\n5, 5\n8, 9'.splitlines(False)
#print(convert(test_data))

print(17, solve1(convert(test_data)))
#print('Part 1 ', solve1(convert(data)))

#print('Part 1/2 ', solve1and2(convert(data)))

#print('Part 2 ', solve2(convert(data)))
