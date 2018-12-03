#!/usr/local/bin/python3
import InputHelper as IH
import regex as regex

def solve1(input):
    locations = set()
    overlaps = set()
    count_overlaps = 0
    count_squares = 0

    max_x = 0
    max_y = 0

    for line in input:
        (id, x, y, width, height) = line
        max_x = max(max_x, x + width)
        max_y = max(max_y, y + width)

        for col in range(x, x + width):
            for row in range(y, y + height):
                count_squares += 1
                key = str(col) + '_' + str(row)
                if key in locations:
                    if not(key) in overlaps:
                        count_overlaps += 1
                        overlaps.add(key)
                else:
                    locations.add(key)

    print(max_x)
    print(max_y)
    print(count_squares)

    return count_overlaps

def convert(lines):
    return [convert_line(line) for line in lines]

def convert_line(line):
    result = regex.match('#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', line)

    return (
            result.group(1),
            int(result.group(2)),
            int(result.group(3)),
            int(result.group(4)),
            int(result.group(5))
        )

data = IH.InputHelper(3).readlines()
#print(data)
#print(convert(data))

test_data = [
    '#1 @ 1,3: 4x4',
    '#2 @ 3,1: 4x4',
    '#3 @ 5,5: 2x2'  
]

#print(4, solve1(convert(test_data)))

print('Part 1 ', solve1(convert(data)))

#print('Part 2 ', solve2(convert(data)))
