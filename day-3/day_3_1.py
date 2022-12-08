import string

characters = string.ascii_letters


def organize():
    values = []
    with open("./day-3/input.txt") as f:
        content = f.read().split("\n")
    for data in content:
        compartment_size = int(len(data) / 2)

        c1_items = data[0:compartment_size]
        c2_items = data[compartment_size:]

        common = "".join(set(c1_items).intersection(c2_items))
        if common:
            values.append(characters.index(common) + 1)

    print(sum(values))


organize()
