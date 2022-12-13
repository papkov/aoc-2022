import re
from copy import deepcopy


def part1(crates, instructions):
    for instr in instructions:
        mv, fr, to = map(int, re.findall('\d+', instr))
        for _ in range(mv):
            crates[to].append(crates[fr].pop())

    return ''.join([c[-1] for c in crates.values()])


def part2(crates, instructions):
    for instr in instructions:
        mv, fr, to = map(int, re.findall('\d+', instr))
        crates[to].extend(crates[fr][-mv:])
        del crates[fr][-mv:]

    return ''.join([c[-1] for c in crates.values()])


def main(task):
    position = task[:8]
    instructions = task[10:]
    crates = {int(i): [] for i in task[8].strip().split()}
    for r in position[::-1]:
        for i, j in enumerate(range(0, len(r), 4)):
            crate = r[j + 1]
            if crate != ' ':
                crates[i + 1].append(crate)

    print('Part 1:', part1(deepcopy(crates), instructions))
    print('Part 2:', part2(deepcopy(crates), instructions))


if __name__ == '__main__':
    with open('data/day5.txt', 'r') as f:
        main(f.readlines())
