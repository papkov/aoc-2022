def part1(task):
    scores = {
        'A': 1,
        'B': 2,
        'C': 3,
        'X': 1,
        'Y': 2,
        'Z': 3,
    }
    total_score = 0
    for r in task:
        r = r.strip().split()
        opponent = scores[r[0]]
        player = scores[r[1]]
        total_score += player
        if player - opponent == 1 or opponent - player == 2:
            total_score += 6
        elif player == opponent:
            total_score += 3
    return total_score


def part2(task):
    scores = {
        'A': 1,
        'B': 2,
        'C': 3,
        'X': -1,
        'Y': 0,
        'Z': 1,
    }
    total_score = 0
    for r in task:
        r = r.strip().split()
        opponent = scores[r[0]]
        outcome = scores[r[1]]

        player = opponent + outcome
        if player == 0:
            player = 3
        elif player == 4:
            player = 1

        total_score += player
        if outcome == 1:
            total_score += 6
        elif outcome == 0:
            total_score += 3
    return total_score


def main(task):
    print('Part 1:', part1(task))
    print('Part 2:', part2(task))


if __name__ == '__main__':
    with open('data/day2.txt', 'r') as f:
        main(f.readlines())