import numpy as np


def print_field_rope(field_shape, rope):
    for i in range(field_shape[0]):
        for j in range(field_shape[1]):
            for ir, r in enumerate(rope):
                if np.all(r == (i, j)):
                    print('H' if ir == 0 else ir, end='')
                    break
            else:
                print('.', end='')
        print('\n', end='')
    print('\n')


def solve(task, n_knots: int = 10):
    moves = {
        'R': np.array([0, 1]),
        'L': np.array([0, -1]),
        'D': np.array([-1, 0]),
        'U': np.array([1, 0])
    }

    visited = set()
    rope = np.zeros((n_knots, 2), dtype=np.int32)
    for r in task:
        direction, steps = r.strip().split()
        for _ in range(int(steps)):
            rope[0] += moves[direction]  # move the head
            for i in range(1, n_knots):
                delta = rope[i - 1] - rope[i]
                if np.abs(delta).max() > 1:  # check the distance
                    rope[i] += np.clip(delta, -1, 1)  # move the knot at most by 1
            visited.add(tuple(rope[-1]))
    return len(visited)


def main(task):
    print('Part 1:', solve(task, 2))
    print('Part 2:', solve(task, 10))


if __name__ == '__main__':
    with open('data/day9.txt', 'r') as f:
        main(f.readlines())
