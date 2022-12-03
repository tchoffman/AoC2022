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


def common_item(lists):
    target = len(lists)
    items = dict()
    for l in lists:
        s = set(l)
        for i in s:
            if i in items.keys():
                items[i] += 1
            else:
                items[i] = 1
            if items[i] == target:
                return i


with open('input.txt') as input_data:
    total = 0
    group = []
    for line in input_data.readlines():
        rucksack = [c for c in line.strip("\n")]
        group.append(rucksack)
        if len(group) == 3:
            common = common_item(group)
            group = []
            total += score_item(common)
            print(common, score_item(common))

    print("Part2: ", total)
