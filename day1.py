import re

from common import read_lines


def part1(lines):
    sum = 0

    for line in lines:
        digits = [c for c in line if c.isdigit()]
        sum += int(''.join([digits[0], digits[len(digits) - 1]]))

    print(sum)


def part2(lines):
    spelled = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }

    sum = 0

    for line in lines:
        digits = {}

        for k, v in spelled.items():
            try:
                # find all indices where we see a spelled number
                matches = [m.start() for m in re.finditer(k, line)]

                # we add these digits with their indices to the map
                for m in matches:
                    digits[m] = v
            except ValueError:
                pass

        # add actual digits characters with their indices to the map
        for i in range(len(line)):
            if line[i].isdigit():
                digits[i] = line[i]

        # sort the map by its keys
        digits = dict(sorted(digits.items()))

        # get the values of the map sorted
        digits = list(digits.values())

        # sum first and last as we did on part 1
        sum += int(''.join([digits[0], digits[len(digits) - 1]]))

    print(sum)


if __name__ == '__main__':
    lines = read_lines('input/day1.txt')
    part1(lines)
    part2(lines)
