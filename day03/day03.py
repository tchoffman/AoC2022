def find_item(left, right):
    for i in left:
        for j in right:
            if i == j:
                return i

def score_item(item):
    A = ord('A')
    a = ord('a')
    i = ord(item)
    if i < a:
        return i - A + 27
    else:
        return i - a + 1


with open('input.txt') as input_data:
    total = 0
    for line in input_data.readlines():
        rucksack = [c for c in line.strip("\n")]
        size = len(rucksack)
        mid = int(size / 2)
        item = find_item(rucksack[0:mid], rucksack[mid:size])
        #print(item, score_item(item))
        total += score_item(item)
    print("Part1: ", total)
