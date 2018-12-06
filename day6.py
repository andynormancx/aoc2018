#!/usr/local/bin/python3
import InputHelper as IH
import regex as regex
from collections import defaultdict
from functools import reduce

def solve1(input):
    finite_cords  = set()
    single_shorts = defaultdict(int)

    max_x = reduce(lambda one, two: max([one, two]), list(map(lambda x:x[0], input)))
    min_x = reduce(lambda one, two: min([one, two]), list(map(lambda x:x[0], input)))
    max_y = reduce(lambda one, two: max([one, two]), list(map(lambda x:x[1], input)))
    min_y = reduce(lambda one, two: min([one, two]), list(map(lambda x:x[1], input)))

    shorts_for_cords = defaultdict(list)

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            shorts = shortest_to((x, y), input)
            if len(shorts) == 1:
                single_shorts[shorts[0][0]] += 1
                shorts_for_cords[shorts[0][0]].append((x, y))

    for cord in input:
        if is_finite(cord, shorts_for_cords[cord], max_x, min_x, max_y, min_y):
            finite_cords.add(cord)

    finite_shorts = dict(filter(lambda x: x[0] in finite_cords, single_shorts.items()))
    
    return max(finite_shorts.items(), key = lambda x:x[1])[1]

def solve2(input, target_dist):
    max_x = reduce(lambda one, two: max([one, two]), list(map(lambda x:x[0], input)))
    min_x = reduce(lambda one, two: min([one, two]), list(map(lambda x:x[0], input)))
    max_y = reduce(lambda one, two: max([one, two]), list(map(lambda x:x[1], input)))
    min_y = reduce(lambda one, two: min([one, two]), list(map(lambda x:x[1], input)))

    matched = 0

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            total_dist = 0
            for cord in input:
                total_dist += calc_dist((x, y), cord)
            else:
                if total_dist < target_dist:
                    matched += 1
    
    return matched

def shortest_to(point, cords):
    distances = {}
    for cord in cords:
        dist = calc_dist(point, cord)
        distances[cord] = dist

    min_dist = min(distances.values())

    return list(filter(lambda x: x[1] == min_dist, distances.items()))

def is_finite(cord, shorts, max_x, min_x, max_y, min_y):
    for short in shorts:
        if short[0] <= min_x or short[0] >= max_x or short[1] <= min_y or short[1] >= max_y:
            return False

    return True

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

#print(17, solve1(convert(test_data)))
print('Part 1 ', solve1(convert(data)))

print(16, solve2(convert(test_data), 32))

#print('Part 1/2 ', solve1and2(convert(data)))

print('Part 2 ', solve2(convert(data), 10000))
