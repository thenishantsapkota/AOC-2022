import string

characters = string.ascii_letters


def organize():
    values = []
    with open("./day-3/input.txt") as f:
        content = f.read().split("\n")

    group_items = [content[pos : pos + 3] for pos in range(0, len(content), 3)]

    for items in group_items:
        common = "".join(set(items[0]).intersection(items[1]).intersection(items[2]))
        if common:
            values.append(characters.index(common) + 1)

    print(sum(values))


organize()
