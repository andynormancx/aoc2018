#!/usr/local/bin/python3
import InputHelper as IH

def solve1(input):
    return sum(convert(input))

def solve2(lines):
    target = 0
    index = 0
    freq = 0
    found = False
    seen_values = {0}

    while not found:
        next = lines[index % len(lines)]
        freq = freq + next
        if freq in seen_values:
            found = True
            target = freq
        else:
            seen_values.add(freq)
        index += 1

    return target

def convert(lines):
    return [int(line) for line in lines]

data = IH.InputHelper(1).readlines()

print('Part 1 ', solve1(data))
#print('0 ', solve2([+1, -1]))
#print('10 ', solve2([+3, +3, +4, -2, -4]))
#print('5 ', solve2([-6, +3, +8, +5, -6]))
#print('14 ', solve2([+7, +7, -2, -7, -4]))
print('Part 2 ', solve2(convert(data)))