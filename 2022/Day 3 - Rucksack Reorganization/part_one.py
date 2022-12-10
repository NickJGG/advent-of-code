from util import read_file, find_nonunique_item, calculate_priority

def part_one():
    rucksacks = read_file()

    total_priorities = 0

    for sack in rucksacks:
        group = split_sack(sack)

        nonunique_item = find_nonunique_item(group)
        priority = calculate_priority(nonunique_item)

        total_priorities += priority
    
    print(f"1. The sum of all priorities is { total_priorities }")

def split_sack(sack):
    compartment_length = int(len(sack) / 2)

    return [
        sack[:compartment_length],
        sack[compartment_length:]
    ]
