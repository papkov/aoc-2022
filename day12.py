import numpy as np
from itertools import product

STEPS = np.array([[0, 1], [0, -1], [1, 0], [-1, 0]])


def is_outside_or_high(loc, loc_from, grid):
    return np.any(loc < 0) or np.any(loc >= np.array(grid.shape)) or grid[tuple(loc)] - grid[tuple(loc_from)] > 1


def bfs(start, end, graph):
    if isinstance(start, tuple):
        queue = [(start, 0)]
    elif isinstance(start, list) and isinstance(start[0], tuple):
        queue = [(s, 0) for s in start]
    else:
        raise ValueError

    visited = set()
    while queue:
        node, depth = queue.pop(0)
        if node == end:
            return depth
        if node not in visited:
            queue.extend((n, depth + 1) for n in graph[node])
        visited.add(node)
    return np.inf


def solve(task, from_any_a: bool = False):
    grid = np.zeros((len(task), len(task[0]) - 1), dtype=np.int32)
    start = None
    end = None

    for i, r in enumerate(task):
        for j, c in enumerate(r.strip()):
            if c == 'S':
                start = (i, j)
            elif c == 'E':
                end = (i, j)
                grid[i, j] = ord('z') - 97
            else:
                grid[i, j] = ord(c) - 97

    graph = {}
    for ij in product(*map(range, grid.shape)):
        ij = np.array(ij)
        graph[tuple(ij)] = [tuple(ij + s) for s in STEPS if not is_outside_or_high(ij + s, ij, grid)]

    if from_any_a:
        return bfs(list(zip(*np.where(grid == 0))), end, graph)
    return bfs(start, end, graph)


def main(task):
    print('Part 1:', solve(task))
    print('Part 2:', solve(task, from_any_a=True))


if __name__ == '__main__':
    with open('data/day12.txt', 'r') as f:
        main(f.readlines())
