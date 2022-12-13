def part1(task):
    s = 0
    for line in task:
        length = len(line)
        first, second = map(set, [line[:length // 2], line[length // 2:]])
        in_both = (first & second).pop()
        priority = ord(in_both) - (96 if in_both.islower() else 38)
        s += priority
    return s


def part2(task):
    s = 0
    for g in range(0, len(task), 3):
        first, second, third = map(lambda x: set(x.strip()), task[g:g+3])
        badge = (first & second & third).pop()
        priority = ord(badge) - (96 if badge.islower() else 38)
        s += priority
    return s


def main(task):
    print('Part 1:', part1(task))
    print('Part 2:', part2(task))


if __name__ == '__main__':
    with open('data/day3.txt', 'r') as f:
        main(f.readlines())
