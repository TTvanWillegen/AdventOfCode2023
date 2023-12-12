import math

from pull import AocInteraction
import re

#  https://adventofcode.com/2023/day/4
#  --- Day 4: Scratchcards ---
def part_1(advent_of_code):
    with open('input.txt', 'r') as input_file:
        summed_winnings = 0
        for card in input_file:
            card_nr, game = re.split(":\\s+", card.split("\n")[0])
            card_nr = card_nr.split("Card ")[1]

            winning_s, having_s = re.split("\\s+\|\\s+", game)
            winning = set(re.split("\\s+", winning_s))
            having = set(re.split("\\s+", having_s))

            overlapping = len(winning.intersection(having))
            card_winnings = int(math.pow(2, (overlapping - 1)) if overlapping > 0 else 0)

            print(overlapping, card_winnings, winning, having)
            summed_winnings += card_winnings
        advent_of_code.answer(1, summed_winnings)


#  --- Part Two ---
def part_2(advent_of_code):
    card_counts = {}
    with open('input.txt', 'r') as input_file:
        for card in input_file:
            card_nr, game = re.split(":\\s+", card.split("\n")[0])
            card_nr = int(re.split("\\s+", card_nr)[1])
            count = card_counts.get(card_nr, 1)
            card_counts[card_nr] = count

            winning_s, having_s = re.split("\\s+\|\\s+", game)
            winning = set(re.split("\\s+", winning_s))
            having = set(re.split("\\s+", having_s))

            overlapping = len(winning.intersection(having))

            for i in range(overlapping):
                if (i + 1) > 202:
                    break
                card_counts[card_nr + i + 1] = card_counts.get(card_nr + i + 1, 1) + count

            print(overlapping, card_counts)
    s = 0
    for c, v in card_counts.items():
        s += v
    print(s)
    advent_of_code.answer(2, s)


if __name__ == "__main__":
    aoc_interaction = AocInteraction()
    part_1(aoc_interaction)
    part_2(aoc_interaction)
