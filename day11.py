import math


def get_op(line: str):
    return eval(f'lambda old: {line}')


def solve(task, rounds: int = 20, reduce_worry: bool = True):
    items = [list(map(int, line.strip().replace('Starting items: ', '').split(', '))) for line in task[1::7]]
    operations = [get_op(line.strip().replace('Operation: new = ', '')) for line in task[2::7]]
    test_divisible = [int(line.strip().replace('Test: divisible by ', '')) for line in task[3::7]]
    divisible_true = [int(line.strip().replace('If true: throw to monkey ', '')) for line in task[4::7]]
    divisible_false = [int(line.strip().replace('If false: throw to monkey ', '')) for line in task[5::7]]
    item_count = [0 for _ in items]
    reduction = math.prod(test_divisible)

    for r in range(rounds):
        for monkey in range(len(items)):
            for item_worry in items[monkey]:
                item_count[monkey] += 1
                item_worry = operations[monkey](item_worry)
                if reduce_worry:
                    item_worry = int(item_worry / reduce_worry)
                else:
                    item_worry %= reduction

                if item_worry % test_divisible[monkey] == 0:
                    throw_to = divisible_true[monkey]
                else:
                    throw_to = divisible_false[monkey]
                items[throw_to].append(item_worry)
            items[monkey] = []
        # if (r + 1) in (1, 20) or (r + 1) % 1000 == 0:
        #     print(item_count)

    return math.prod(sorted(item_count)[-2:])


def main(task):
    print('Part 1:', solve(task, 20, True))
    print('Part 2:', solve(task, 10000, False))


if __name__ == '__main__':
    with open('data/day11.txt', 'r') as f:
        main(f.readlines())
