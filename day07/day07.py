with open('input.txt') as input_data:
    directories = {'root': 0}
    path = []
    for line in input_data.readlines():
        # Adjust Path
        print("\n", line.strip("\n"))
        if "$ cd" in line:
            directory = line.split(" ")[2].strip("\n")
            if directory == "/":
                directory = "root"
            if directory == "..":
                path.pop()
            else:
                path.append(directory)
            print("path update")
        # Update Directory Listing
        elif line.split(" ")[0] == "dir":
            new_directory = "-".join(path) + "-" + line.split(" ")[1].strip("\n")
            directories[new_directory] = 0
            print("dir update")
        # Update Directory Sizes
        elif line.split(" ")[0] != "$":
            size = int(line.split(" ")[0])
            for i in range(len(path)):
                target_directory = "-".join(path[:i+1])
                directories[target_directory] += size
            print("file update")
        else:
            print("none")

print(directories)
bites = 0
for key, value in directories.items():
    if value <= 100000:
        print(key, value)
        bites += value

print("PartA: ", bites)


filesystem = 70000000
needed_size = 30000000
current_size = directories['root']
target = needed_size - (filesystem - current_size)
print("Target:", target)

best_size = current_size
for key, value in directories.items():
    if value >= target:
        if value < best_size:
            best_size = value

print("PartB: ", best_size)
