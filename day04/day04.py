with open('input.txt') as input_data:
    count = 0
    for line in input_data.readlines():
        elfA, elfB = line.split(",")
        elfA = [int(i) for i in elfA.split("-")]
        elfB = [int(i) for i in elfB.split("-")]
        #print("A:", elfA, "B:", elfB)
        if elfA[0] >= elfB[0] and elfA[1] <= elfB[1]:
            count += 1
        elif elfB[0] >= elfA[0] and elfB[1] <= elfA[1]:
            count += 1
    print("PartA: ", count)


with open('input.txt') as input_data:
    count = 0
    for line in input_data.readlines():
        elfA, elfB = line.split(",")
        elfA = [int(i) for i in elfA.split("-")]
        elfB = [int(i) for i in elfB.split("-")]
        #print("A:", elfA, "B:", elfB)
        if (elfA[0] <= elfB[1] and elfA[0] >= elfB[0]) or (elfB[0] <= elfA[1] and elfB[0] >= elfA[0]):
            count += 1
    print("PartB: ", count)
