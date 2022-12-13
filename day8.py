import numpy as np


def part1(grid):
    visible = np.zeros_like(grid)
    for rot in range(4):
        tallest = np.zeros_like(grid[0]) - 1
        for i, r in enumerate(grid):
            visible[i] += r > tallest
            tallest = np.maximum(tallest, r)
        grid = np.rot90(grid)
        visible = np.rot90(visible)

    print((visible > 0).sum())


def part2(grid):
    scores = []
    for rot in range(4):
        scenic_score = np.zeros_like(grid)
        for i in range(grid.shape[1] - 1):
            visibility = np.cumprod(grid[i+1:] < grid[i][None, :], 0)
            scenic_score[i] = np.clip(visibility.sum(0) + 1, 1, grid.shape[1] - i - 1)

        scenic_score = np.rot90(scenic_score, -rot)
        scores.append(scenic_score)
        grid = np.rot90(grid)

    scores = np.prod(scores, axis=0)
    print(np.max(scores))


def main(task):
    grid = np.array([[int(c) for c in r.strip()] for r in task])
    part1(grid)
    part2(grid)


if __name__ == '__main__':
    with open('data/day8.txt', 'r') as f:
        main(f.readlines())
