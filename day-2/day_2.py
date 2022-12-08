SCORES_1 = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6,
}


def part_one():
    total_score = 0
    with open("./day-2/input.txt") as f:
        content = f.read().split("\n")

    print(content[0])
    for data in content:
        total_score += SCORES_1[data]

    print(total_score)


part_one()

SCORES_2 = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7,
}


def part_two():
    total_score = 0
    with open("./day-2/input.txt") as f:
        content = f.read().split("\n")

    print(content[0])
    for data in content:
        total_score += SCORES_2[data]

    print(total_score)


part_two()
