#!/usr/local/bin/python3
import InputHelper as IH
import regex as regex
from collections import defaultdict

def solve1(input):
    rules = defaultdict(list)
    remaining_steps = set()
    finished_steps = []

    for rule in input:
        remaining_steps.add(rule[0])
        remaining_steps.add(rule[1])
        rules[rule[1]].append(rule[0])

    while remaining_steps.__len__() != 0:
        available_steps = get_available(rules, remaining_steps, finished_steps)
        finished_steps.append(available_steps[0])
        remaining_steps.remove(available_steps[0])

    return ''.join(finished_steps)

def get_available(rules, remaining_steps, finished_steps):
    available = []

    for step in remaining_steps:
        if step in rules:
            include = True
            for rule in rules[step]:
                if rule not in finished_steps:
                    include = False
            else:                
                if include:
                    available.append(step)
        else:
            available.append(step)

    return sorted(available)

def convert(lines):
    return [convert_line(line) for line in lines]

def convert_line(line):
    # Step C must be finished before step A can begin.
    result = regex.match(r'Step (.) must be finished before step (.) can begin\.', line)

    return (
            result.group(1),
            result.group(2)
        )

data = IH.InputHelper(7).readlines()
#print(data)

test_data = [
    'Step C must be finished before step A can begin.',
    'Step C must be finished before step F can begin.',
    'Step A must be finished before step B can begin.',
    'Step A must be finished before step D can begin.',
    'Step B must be finished before step E can begin.',
    'Step D must be finished before step E can begin.',
    'Step F must be finished before step E can begin.'
]

print(convert(test_data))

#print(convert(data))

print('CABDFE', solve1(convert(test_data)))

print('Part 1 ', solve1(convert(data)))

#print('Part 2 ', solve2(convert(data)))
