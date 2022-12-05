with open('input.txt') as input_data:

    stacks = [[] for i in range(9)]
    commands = []
    for line in input_data.readlines():
        if '[' in line:
            for i in range(0, 9):
                loc = (i * 4) + 1
                if loc <= len(line):
                    crate = line[loc]
                    if crate != " ":
                        stacks[i].append(crate)
        if "move" in line:
            l = line.split(" ")
            move = {"n": int(l[1]),
                    "loc": int(l[3]),
                    "dest": int(l[5])}
            commands.append(move)
    for stack in stacks:
        stack.reverse()

    #print(commands)
    print(stacks)
    for cmd in commands:
        for i in range(cmd['n']):
            i = cmd['dest'] - 1
            j = cmd['loc'] - 1
            stacks[i].append(stacks[j].pop())
    print("".join([i[-1] for i in stacks]))



