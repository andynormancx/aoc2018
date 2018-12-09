#!/usr/local/bin/python3
import InputHelper as IH
import regex as regex
from collections import defaultdict

def solve1(num_players, last_marble_worth):
    high_score = 0
    marbles = []
    next_marble = 0

    current_marble = 0
    current_player = 0

    player_scores = [0] * num_players

    marbles.append(0)
    next_marble = 1

    #print_state(marbles, current_marble)

    while next_marble <= last_marble_worth:
        if next_marble % 100000 == 0:
            print(str(next_marble))

        if next_marble % 23 == 0:
            player_scores[current_player] += next_marble
            seven_back_index = ((current_marble - 7) % len(marbles))
            player_scores[current_player] += marbles[seven_back_index]
            marbles.remove(marbles[seven_back_index]) # lazy !
            current_marble = (seven_back_index % len(marbles))
        else:
            current_marble = ((current_marble + 1) % len(marbles)) + 1
            marbles.insert(current_marble, next_marble)

        next_marble += 1
        current_player = (current_player + 1) % num_players

    return max(player_scores)


def print_state(marbles, current_marble):
    return
    output = ''

    for index, marble in enumerate(marbles):
        if index == current_marble:
            output += ' (' + str(marble) + ')'
        else:
            output += '  ' + str(marble) + ' '

    print(output)

#print('32', solve1(9, 25))
#print('32 x 10', solve1(9, 250))

#print('8317', solve1(10, 1618))
#print('8317  x 10', solve1(10, 16180))
#print('146373 x 10', solve1(13, 79990))
##print('146373', solve1(13, 7999))
#print('2764', solve1(17, 1104))
#print('2764 x 10', solve1(17, 11040))
#print('54718 x 10', solve1(21, 61110))
##print('54718', solve1(21, 6111))
#print('37305', solve1(30, 5807))
#print('37305 x 10', solve1(30, 58070))


#print('Part 1', solve1(452, 71250))
#print('Part 1', solve1(452, 400000))

#print('Part 1', solve1(452, 142500))

#print('Part 1', solve1(452, 712500))
print('Part 2', solve1(452, 7125000))

#print('Part 1 ', solve1(convert(data)))

#print('15', solve2(convert(test_data), 0, 2))

#print('Part 2 ', solve2(convert(data), 60, 5))
