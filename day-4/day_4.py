def solution():
    full_overlaps = 0
    total_overlaps = 0
    with open("./day-4/input.txt") as f:
        content = f.read().split("\n")

    pairs = [x.split(",") for x in content]
    for pair in pairs:
        range_1 = pair[0].split("-")
        range_2 = pair[1].split("-")

        numbers_1 = list(range(int(range_1[0]), int(range_1[1]) + 1))
        numbers_2 = list(range(int(range_2[0]), int(range_2[1]) + 1))

        if set(numbers_1).issubset(numbers_2) or set(numbers_2).issubset(numbers_1):
            full_overlaps += 1

        common = set(numbers_1).intersection(numbers_2)
        if common:
            total_overlaps += 1

    print(full_overlaps)
    print(total_overlaps)


solution()
