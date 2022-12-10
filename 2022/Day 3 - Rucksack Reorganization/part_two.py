from util import read_file, find_nonunique_item, calculate_priority

def part_two():
    groups = group_rucksacks()

    total_priorities = 0

    for group in groups:
        item = find_nonunique_item(group)
        priority = calculate_priority(item)

        total_priorities += priority
    
    print(f"2. The sum of all priorities is { total_priorities }")

def group_rucksacks():
    sacks = read_file()
    group_count = int(len(sacks) / 3)

    grouped_sacks = []

    for i in range(group_count):
        start_index = i * 3

        group = [sacks[start_index + j] for j in range(3)]
        grouped_sacks.append(group)

    return grouped_sacks
