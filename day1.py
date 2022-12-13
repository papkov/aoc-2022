
def main():
    current_elf_calories = 0
    elf_counter = 0
    max_calories = 0
    max_elf = 0
    elf_calories = []

    with open('data/day1.txt', 'r') as f:
        all_calories = f.readlines()
        for calories in all_calories:
            if calories != '\n':
                current_elf_calories += int(calories)
            else:
                elf_calories.append(current_elf_calories)
                if current_elf_calories > max_calories:
                    max_calories = current_elf_calories
                    max_elf = elf_counter
                elf_counter += 1
                current_elf_calories = 0
    elf_calories = sorted(elf_calories)
    print(max_elf, max_calories, sum(elf_calories[-3:]))


if __name__ == '__main__':
    main()
