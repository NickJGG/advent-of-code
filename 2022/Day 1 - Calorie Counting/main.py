def part_one():
    file = open("input.txt", "r")
    all_text = file.read()
    lines = all_text.split("\n")

    fattest_elf = [0, 0]

    current_elf = [0, 0]

    for line in lines:
        if line.isnumeric():
            current_elf[1] += int(line)

            continue
        
        if current_elf[1] > fattest_elf[1]:
            fattest_elf = current_elf

        current_elf = [current_elf[0] + 1, 0]
    
    print(f"1. The fattest elf is #{ fattest_elf[0] } at { fattest_elf[1] } calories")

def part_two():
    file = open("input.txt", "r")
    all_text = file.read()
    lines = all_text.split("\n")

    fattest_elves = [
        [0, 0]
    ]

    current_elf = [0, 0]

    for line in lines:
        if line.isnumeric():
            current_elf[1] += int(line)

            continue
        
        for i, fat_elf in enumerate(fattest_elves):
            if current_elf[0] != fat_elf[0] and current_elf[1] > fat_elf[1]:
                fattest_elves.insert(i, current_elf)
                fattest_elves = fattest_elves[:3]

                break

        current_elf = [current_elf[0] + 1, 0]
    
    fattest_elf_indices = list(map(lambda elf: elf[0], fattest_elves))
    fattest_elves_calories = sum(list(map(lambda elf: elf[1], fattest_elves)))

    print(f"2. The fattest elves are #{ fattest_elf_indices } at { fattest_elves_calories } combined calories")

if __name__ == "__main__":
    part_one()
    part_two()
