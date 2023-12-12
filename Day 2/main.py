from pull import AocInteraction
import re


#  https://adventofcode.com/2023/day/2
#  --- Day 2: Cube Conundrum ---

def part_1(advent_of_code):
    max_cubes = {
        'red': 12,
        'green': 13,
        'blue': 14
    }
    possible_arr = []
    s = 0
    with open('input.txt', 'r') as input_file:
        for game in input_file:
            game_num, game_results = ((game.split('\n')[0]).split("Game ")[1]).split(": ")
            grabs = game_results.split("; ")
            possible = True

            for grab in grabs:
                cubes = grab.split(", ")
                for cube in cubes:
                    grabbed_num = int(cube.split(" ")[0])
                    for color, max_amount in max_cubes.items():
                        if cube.endswith(" " + color):
                            possible = possible and grabbed_num <= max_amount
            if possible:
                possible_arr.append(int(game_num))
                s += int(game_num)
    advent_of_code.answer(1, s)


#  --- Part Two ---
def part_2(advent_of_code):
    total_power = 0
    with open('input.txt', 'r') as input_file:
        for game in input_file:
            game_max = {
                'red': 0,
                'green': 0,
                'blue': 0
            }
            game_num, game_results = ((game.split('\n')[0]).split("Game ")[1]).split(": ")
            grabs = game_results.split("; ")

            for grab in grabs:
                cubes = grab.split(", ")
                for cube in cubes:
                    grabbed_num = int(cube.split(" ")[0])
                    for color, current_max in game_max.items():
                        if cube.endswith(" " + color) and grabbed_num > current_max:
                            game_max[color] = grabbed_num
            game_power = 1
            for color, current_max in game_max.items():
                game_power *= current_max
            total_power += game_power
        advent_of_code.answer(2, total_power)


if __name__ == "__main__":
    aoc_interaction = AocInteraction()
    part_1(aoc_interaction)
    part_2(aoc_interaction)
