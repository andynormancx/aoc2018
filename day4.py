#!/usr/local/bin/python3
import InputHelper as IH
import regex as regex
from collections import defaultdict

def solve1and2(input):
    lines = sorted(input, key = lambda x: (x[2], x[3], x[4], x[5]))
    latest_id = None
    guards_sleep_count = dict()
    asleep_minute = 0

    for (type, id, month, day, hour, minute) in lines:
        if type == 'shift':
            latest_id = id
            if id not in guards_sleep_count:
                guards_sleep_count[id] = (latest_id, 0, defaultdict(int))

        if type == 'asleep':
            asleep_minute = minute

        if type == 'wake':
            (_, sleep_count, sleep_minutes) = guards_sleep_count[latest_id]

            for sleep_min in range(asleep_minute, minute):
                sleep_minutes[sleep_min] = sleep_minutes[sleep_min] + 1

            guards_sleep_count[latest_id] = (latest_id, sleep_count + minute - asleep_minute, sleep_minutes)

    highest_guard = max(guards_sleep_count.values(), key=lambda x:x[1])
    hightest_hour = max(highest_guard[2].items(),  key=lambda x:x[1])

    max_count = 0
    max_guard = None
    max_hour = 0

    for guard in guards_sleep_count.items():
        for hour_entry in guard[1][2].items():
            if hour_entry[1] > max_count:
                max_count = hour_entry[1]
                max_guard = guard
                max_hour = hour_entry[0]


    return int(highest_guard[0]) * hightest_hour[0], int(max_guard[0]) * max_hour

def convert(lines):
    return [convert_line(line) for line in lines]

def convert_line(line):
    # [1518-02-06 23:52] Guard #3109 begins shift
    result = regex.match(r'\[\d+\-(\d+)\-(\d+) (\d+):(\d+)] (.+)', line)
    type = 'start shift'
    id = None

    if result.group(5) == 'wakes up':
        type = 'wake'
    elif result.group(5) == 'falls asleep':
        type = 'asleep'
    else:
        type = 'shift'
        id_result = regex.match(r'.+#(\d+)', line)
        id = id_result.group(1)

    return (
            type,
            id,
            int(result.group(1)), # month
            int(result.group(2)), # day
            int(result.group(3)), # hour
            int(result.group(4)) # minute
        )

data = IH.InputHelper(4).readlines()
#print(data)
#print(convert(data))

test_data = [
    '[1518-11-05 00:55] wakes up',
    '[1518-11-01 00:00] Guard #10 begins shift',
    '[1518-11-01 00:05] falls asleep',
    '[1518-11-01 00:25] wakes up',
    '[1518-11-01 00:30] falls asleep',
    '[1518-11-01 00:55] wakes up',
    '[1518-11-01 23:58] Guard #99 begins shift',
    '[1518-11-02 00:40] falls asleep',
    '[1518-11-02 00:50] wakes up',
    '[1518-11-03 00:05] Guard #10 begins shift',
    '[1518-11-03 00:24] falls asleep',
    '[1518-11-03 00:29] wakes up',
    '[1518-11-04 00:02] Guard #99 begins shift',
    '[1518-11-04 00:36] falls asleep',
    '[1518-11-04 00:46] wakes up',
    '[1518-11-05 00:03] Guard #99 begins shift',
    '[1518-11-05 00:45] falls asleep'
]

print(4, solve1and2(convert(test_data)))

print('Part 1/2 ', solve1and2(convert(data)))

#print('Part 2 ', solve2(convert(data)))
