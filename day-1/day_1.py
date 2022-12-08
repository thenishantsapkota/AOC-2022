def most_calories():
    with open("./day-1/input.txt") as f:
        content = f.read()

    string = content.split("\n\n")
    sum_array = []
    for data in string:
        calories = [int(i) for i in data.split("\n")]
        sum_array.append(sum(calories))

    sum_array.sort(reverse=True)
    print(sum_array[0])  # Elf carrying highest calories
    print(sum(sum_array[0:3]))  # Total calories carried by top 3 elves


most_calories()
