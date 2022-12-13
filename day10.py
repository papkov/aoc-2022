def part1(task):
    register = [1]
    for r in task:
        if r.startswith('addx'):
            register.append(register[-1])
            v = int(r.strip().split()[1])
            register.append(register[-1] + v)
        else:
            register.append(register[-1])

    strength = [register[i] * (i + 1) for i in range(19, 220, 40)]
    return sum(strength)


def draw_cycle(x, cycle):
    if x - 1 <= cycle % 40 <= x + 1:
        print('#', end='')
    else:
        print('.', end='')
    cycle += 1
    return cycle


def part2(task):
    cycle = 0
    x = 1
    for i, r in enumerate(task):
        if r.startswith('addx'):
            cycle = draw_cycle(x, cycle)
            cycle = draw_cycle(x, cycle)
            x += int(r.strip().split()[1])
        else:
            cycle = draw_cycle(x, cycle)
        if cycle % 40 == 0:
            print()


def main(task):
    print('Part 1:', part1(task))
    part2(task)


if __name__ == '__main__':
    with open('data/day10.txt', 'r') as f:
        main(f.readlines())
