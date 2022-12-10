def read_file():
    file = open("input.txt", "r")
    all_text = file.read()
    lines = all_text.split("\n")

    if lines[-1] == "":
        lines.pop()

    return lines

def find_nonunique_item(group):
    item_count = {}

    max_length = max([len(sack) for sack in group])
    group_length = len(group)

    for i in range(max_length):
        items = []

        for j, sack in enumerate(group):
            if i < len(sack):
                items.append([sack[i], j])

        for item, sack in items:
            if item in item_count and sack in item_count[item]:
                continue

            item_count[item] = item_count[item] + [sack] if item in item_count else [sack]

            if len(item_count[item]) == group_length:
                return item

def calculate_priority(item):
    subtractee = ord(item)
    subtractor = ord('A') if item.isupper() else ord('a')

    priority = subtractee - subtractor + 1
    priority = priority + 26 if item.isupper() else priority

    return priority
