from typing import List, Any


class Packet:
    def __init__(self, values: List[Any]):
        self.values = values

    def __lt__(self, other: 'Packet'):
        for left, right in zip(self.values, other.values):
            result = None
            if isinstance(left, int) and isinstance(right, int):
                if left > right:
                    return False
                elif left < right:
                    return True
            elif isinstance(left, list) and isinstance(right, list):
                result = Packet(left) < Packet(right)
            elif isinstance(left, int) and isinstance(right, list):
                result = Packet([left]) < Packet(right)
            elif isinstance(left, list) and isinstance(right, int):
                result = Packet(left) < Packet([right])
            else:
                raise ValueError(f'Unsupported types {type(left), type(right)}')
            if result is not None:
                return result
        if len(self.values) < len(other.values):
            return True
        elif len(self.values) > len(other.values):
            return False


def part1(first, second):
    indices = [i + 1 for i, (f, s) in enumerate(zip(first, second)) if f < s]
    return sum(indices)


def part2(first, second):
    packets = sorted([Packet([[2]]), Packet([[6]])] + first + second)
    indices = [i + 1 for i, p in enumerate(packets) if p.values in ([[2]], [[6]])]
    return indices[0] * indices[1]


def main(task):
    first = [Packet(eval(r.strip())) for r in task[::3]]
    second = [Packet(eval(r.strip())) for r in task[1::3]]
    print('Part 1:', part1(first, second))
    print('Part 2:', part2(first, second))


if __name__ == '__main__':
    with open('data/day13.txt', 'r') as f:
        main(f.readlines())
