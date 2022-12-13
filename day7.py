from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class File:
    name: str
    size: int
    parent: Dir


@dataclass
class Dir:
    name: str
    parent: Dir = None
    children: List[Dir] = field(default_factory=list)
    files: List[File] = field(default_factory=list)


def parse_file_tree(f):
    line = f.readline().strip().split()
    cwd = Dir('root')
    cwd.children.append(Dir('/', cwd))
    while line:
        if line[0] != '$':
            if line[0] == 'dir':
                cwd.children.append(Dir(line[1], cwd))
            else:
                cwd.files.append(File(line[1], int(line[0]), cwd))
        else:
            if line[1] == 'cd':
                if line[2] == '..':
                    cwd = cwd.parent
                else:
                    cwd = next(filter(lambda d: d.name == line[2], cwd.children))
        line = f.readline().strip().split()

    while cwd.name != '/':
        cwd = cwd.parent

    return cwd


def print_dir(d: Dir, level: int = 0):
    space = ' ' * level
    print(f'{space} - {d.name} (dir)')
    for file in d.files:
        print(f'{space}  - {file.name} (file, size={file.size})')
    for child in d.children:
        print_dir(child, level + 1)


def get_dir_size(d: Dir, sizes: Dict[str, int]):
    s = sum([f.size for f in d.files]) + sum([get_dir_size(c, sizes) for c in d.children])
    sizes[f'{d.parent.name}/{d.name}'] = s
    return s


def part1(sizes: Dict[str, int]):
    print('Part 1:', sum(filter(lambda x: x <= 100000, sizes.values())))


def part2(sizes: Dict[str, int], total: int = 70000000, required: int = 30000000):
    to_free = required - (total - sizes['root//'])
    print('Part 2:', next(filter(lambda x: x >= to_free, sorted(sizes.values()))))


def main(f):
    cwd = parse_file_tree(f)
    print_dir(cwd)

    sizes = {}
    _ = get_dir_size(cwd, sizes)
    print('\nDir sizes:', sizes)

    part1(sizes)
    part2(sizes)


if __name__ == '__main__':
    with open('data/day7.txt', 'r') as f:
        main(f)
