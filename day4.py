import re


def part1(intervals):
    s = 0
    for interval in intervals:
        first, second = interval[:2], interval[2:]
        if (first[0] <= second[0] and first[1] >= second[1]) or (second[0] <= first[0] and second[1] >= first[1]):
            s += 1
    return s


def part2(intervals):
    s = 0
    for interval in intervals:
        first, second = interval[:2], interval[2:]
        if first[0] <= second[0] <= first[1] or second[0] <= first[0] <= second[1]:
            s += 1
    return s


def main(task):
    intervals = [list(map(int, re.split('[,-]', r.strip()))) for r in task]
    print('Part 1:', part1(intervals))
    print('Part 2:', part2(intervals))


if __name__ == '__main__':
    with open('data/day4.txt', 'r') as f:
        main(f.readlines())
