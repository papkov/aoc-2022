def solve(task, n: int):
    for i in range(len(task) - n):
        if len(set(task[i:i + n])) == n:
            return i + n


def main(task):
    print('Part 1:', solve(task, 4))
    print('Part 2:', solve(task, 14))


if __name__ == '__main__':
    with open('data/day6.txt', 'r') as f:
        main(f.readline())
