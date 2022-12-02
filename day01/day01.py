with open('input.txt') as input_data:
    current = 0
    max = 0
    for line in input_data.readlines():
        if line != "\n":
            current += int(line)
        else:
            if current > max:
                max = current
            current = 0
print("Part1: ", max)

elves = []
with open('input.txt') as input_data:
    current = 0

    for line in input_data.readlines():
        if line != "\n":
            current += int(line)
        else:
            elves.append(current)
            current = 0

elves.sort(reverse=True)
print(elves[0:3])
print("Part2: ", sum(elves[0:3]))

