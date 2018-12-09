#!/usr/local/bin/python3
import InputHelper as IH
import regex as regex
from collections import defaultdict

def solve1(input):
    _, nodes, value = parse_node(input, 0)

    total = 0
    for node in nodes:
        for meta_data in node[1]:
            total += meta_data

    return total, value

def parse_node(input, start_index):
    index = start_index

    num_child_nodes = input[index]
    num_metadata = input[index + 1]
    index += 2

    my_child_nodes = []
    child_node_values = []
    if num_child_nodes != 0:
        for _ in range(0, num_child_nodes):
            index, child_nodes, child_value = parse_node(input, index)
            my_child_nodes = my_child_nodes + child_nodes
            child_node_values.append(child_value)

    meta_data = []
    if num_metadata != 0:
        for _ in range(0, num_metadata):
            meta_data.append(input[index])
            index += 1

    value = 0
    if num_child_nodes == 0:
        value = sum(meta_data)
    else:
        for metadata_value in meta_data:
            if metadata_value <= len(child_node_values):
                value += child_node_values[metadata_value - 1]


    nodes = my_child_nodes
    nodes.append((nodes, meta_data))

    return index, nodes, value

def solve2(input):

    return 0

def convert(lines):
    return [convert_line(line) for line in lines]

def convert_line(line):
    # Step C must be finished before step A can begin.
    result = regex.match(r'Step (.) must be finished before step (.) can begin\.', line)

    return (
            result.group(1),
            result.group(2)
        )

data = IH.InputHelper(8).readlines()
#print(data)

test_data = [int(line) for line in '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'.split(' ')]

print(test_data)

#print([int(line) for line in data[0].split(' ')])

print('138', solve1([int(line) for line in '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'.split(' ')]))
print(solve1([int(line) for line in data[0].split(' ')]))

#print('Part 1 ', solve1(convert(data)))

#print('15', solve2(convert(test_data), 0, 2))

#print('Part 2 ', solve2(convert(data), 60, 5))
