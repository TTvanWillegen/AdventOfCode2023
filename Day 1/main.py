from pull import AocInteraction


#  https://adventofcode.com/2023/day/1
#  --- Day 1: Trebuchet?! ---
def part_1(advent_of_code):
    with open('input.txt', 'r') as input_file:
        sum = 0
        for line in input_file:
            first = None
            last = None
            for char in line:
                if char.isdigit():
                    if first is None:
                        first = char
                    last = char
            line_val = int(first + last)
            print(line_val)
            sum += line_val
        advent_of_code.answer(1, sum)


text_to_digit = {'one': 1,
                 'two': 2,
                 'three': 3,
                 'four': 4,
                 'five': 5,
                 'six': 6,
                 'seven': 7,
                 'eight': 8,
                 'nine': 9}


#  --- Part Two ---
def part_2(advent_of_code):
    with open('input.txt', 'r') as input_file:
        sum = 0
        for line in input_file:
            line = line.replace('\n', '')
            first = None
            last = None
            index = 0

            # Forwards search
            while index < len(line):
                incr = 1
                r = None

                char = line[index]
                if char.isdigit():
                    r = char
                else:
                    for k,v in text_to_digit.items():
                        x = line.find(k, index)
                        if x == index:
                            r = str(v)
                            incr = len(k)
                            break

                if r is not None:
                    if first is None:
                        first = r
                        break
                index += incr

            # Separately backwards search for the case of 'oneight', 'eightwo' or 'eighthree' at the end of the line.
            line_r = str(line[::-1])
            index = 0
            while index < len(line):
                incr = 1
                r = None

                char = line_r[index]
                if char.isdigit():
                    r = char
                else:
                    for k, v in text_to_digit.items():
                        x = line_r.find(k[::-1], index)
                        if x == index:
                            r = str(v)
                            incr = len(k)
                            break

                if r is not None:
                    if last is None:
                        last = r
                        break
                index += incr
            line_val = int(first + last)
            print(line)
            print(line_val)
            sum += line_val
        print(sum)
        advent_of_code.answer(2, sum)


if __name__ == "__main__":
    aoc_interaction = AocInteraction()
    part_1(aoc_interaction)
    part_2(aoc_interaction)
