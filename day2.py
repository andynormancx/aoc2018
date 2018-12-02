#!/usr/local/bin/python3
import InputHelper as IH

def solve1(input):
    count_2s = 0
    count_3s = 0

    for index, line in enumerate(input):
        count_2s = count_2s + count_dupes(line, 2)
        count_3s = count_3s + count_dupes(line, 3)

    return count_2s * count_3s

def checksum(input_text):
    return 0

def count_dupes(input_text, match):
    seen = dict()

    for index, value in enumerate(list(input_text)):
        if value in seen:
            seen[value] = seen[value] + 1
        else:
            seen[value] = 1        
    
    for key, value in seen.items():
        if value == match:
            return 1

    return 0

def solve2(input):
    matched = ''
    (left, right) = find_matching_ids(input)

    right_values = list(right)

    for index, left_value in enumerate(list(left)):
        if left_value == right_values[index]:
            matched += left_value

    return (matched, left, right)

def find_matching_ids(input):
    for index_outer, outer_id in enumerate(input):
        for index_inner, inner_id in enumerate(input):
            if index_outer != index_inner:
                if count_diffs(inner_id, outer_id) == 1:
                    return (inner_id, outer_id)

    return ''

def count_diffs(left, right):
    left_values = list(left)
    right_values = list(right)
    diff_count = 0

    for index, value in enumerate(left_values):
        if value != right_values[index]:
            diff_count += 1

    return diff_count

def convert(lines):
    return [line for line in lines]

data = IH.InputHelper(2).readlines()
#print(data)

print(0, count_dupes('abcdef', 2))
print(0, count_dupes('abcdef', 3))

print(1, count_dupes('bababc', 2))
print(1, count_dupes('bababc', 3))

print(1, count_dupes('abbcde', 2))
print(0, count_dupes('abbcde', 3))

print(0, count_dupes('abcccd', 2))
print(1, count_dupes('abcccd', 3))

print(12, solve1(['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']))
print('Part 1 ', solve1(convert(data)))

print(2, count_diffs('abcde', 'axcye'))
print(1, count_diffs('fghij', 'fguij'))

print('Part 2 ', solve2(convert(data)))