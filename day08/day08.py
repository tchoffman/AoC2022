forest = []
with open('input.txt') as input_data:
    for line in input_data.readlines():
        row = []
        for c in line.strip("\n"):
            row.append(int(c))
        forest.append(row)

h = len(forest)
w = len(forest[0])

north = [[(j == 0) for i in range(w)] for j in range(h)]
south = [[j == h - 1 for i in range(w)] for j in range(h)]
east = [[i == w - 1 for i in range(w)] for j in range(h)]
west = [[i == 0 for i in range(w)] for j in range(h)]

# View from North
for i in range(0, w):
    tallest = 0
    for j in range(1, h):
        tallest = max(tallest, forest[j - 1][i])
        north[j][i] = forest[j][i] > tallest

# View from South
for i in range(0, w):
    tallest = 0
    for j in range(h - 2, -1, -1):
        tallest = max(tallest, forest[j + 1][i])
        south[j][i] = forest[j][i] > tallest

# View from East
for j in range(0, h):
    tallest = 0
    for i in range(w - 2, -1, -1):
        tallest = max(tallest, forest[j][i + 1])
        east[j][i] = forest[j][i] > tallest

# View from West
for j in range(0, h):
    tallest = 0
    for i in range(1, w):
        tallest = max(tallest, forest[j][i - 1])
        west[j][i] = forest[j][i] > tallest

visible = [[int(north[j][i] or south[j][i] or east[j][i] or west[j][i]) for i in range(w)] for j in range(h)]

print("w", w, "h", h)
count = 0
for j in range(h):
    # print(visible[j])
    for i in range(w):
        count += visible[j][i]

print("Part A: ", count)


# PART 2
scene = [[0 for i in range(w)] for j in range(h)]


def linear_view(view):
    blocked = False
    distance = 0
    i = 1
    while (not blocked) and (i < len(view)):
        distance += 1
        if view[0] <= view[i]:
            blocked = True
        i += 1
    # print(view, " : ", distance)
    return distance

best_score = 0
for i in range(0, w):
    for j in range(0, h):
        # print("=====")
        view_n = linear_view([forest[k][i] for k in range(j, -1, -1)])
        view_s = linear_view([forest[k][i] for k in range(j, h)])
        view_e = linear_view([forest[j][k] for k in range(i, w)])
        view_w = linear_view([forest[j][k] for k in range(i, -1, -1)])
        best_score = max(best_score, view_n * view_s * view_e * view_w)

print("Part B: ", best_score)