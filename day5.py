#!/usr/local/bin/python3
import InputHelper as IH
import regex as regex
from collections import defaultdict

def solve1(input):
    made_changes = True
    working_input = None
    next_input = input.copy()

    while made_changes:
        working_input = next_input.copy()
        next_input = []
        made_changes = False
        index = 0

        while True:
            diff = ord(working_input[index]) - ord(working_input[index + 1])
            if abs(diff) == 32:
                made_changes = True
                index += 2
            else:
                next_input.append(working_input[index])
                index += 1
                if index == len(working_input) - 1:
                    next_input.append(working_input[index])

            if index >= len(working_input) - 1:
                break

    return ''.join(working_input), len(working_input)

def solve2(input):
    min_size = len(input)

    for letter_index in range(ord('A'), ord('Z') + 1):
        large = chr(letter_index)
        small = chr(letter_index + 32)
        print(large)
        working_input = list(filter(lambda x: x != large and x != small, input))
        _, length = solve1(working_input)

        if length < min_size:
            min_size = length

        print(length)


    return min_size
    


data = IH.InputHelper(5).readlines()
#print(data)
#print(convert(data))

test_data = [
]

#print(4, solve1(list('aAcbbBB')))

#print(10, solve1(list('dabAcCaCBAcCcaDA')))

print('Part 1 ', solve1(list(data[0])))

print('Part 2 ', solve2(list(data[0])))

#print(4, solve2(list('dabAcCaCBAcCcaDA')))
