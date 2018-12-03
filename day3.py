#!/usr/local/bin/python3
import InputHelper as IH
import regex as regex

def solve1(input):
    locations = dict()
    overlaps = dict()
    all_ids = set()
    count_overlaps = 0

    for line in input:
        (id, x, y, width, height) = line
        all_ids.add(id)

        for col in range(x, x + width):
            for row in range(y, y + height):
                key = str(col) + '_' + str(row)
                if key in locations.keys():
                    if not(key) in overlaps.keys():
                        count_overlaps += 1
                        overlaps[key] = set([id, locations[key]])
                    else:
                        ids = overlaps[key]
                        ids.add(id)
                        overlaps[key] = ids
                else:
                    locations[key] = id

    overlap_ids = set()

    for key, overlap in overlaps.items():
        for id in overlap:
            overlap_ids.add(id)

    non_overlaps = all_ids.difference(overlap_ids)

    return (count_overlaps, non_overlaps.pop())

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
