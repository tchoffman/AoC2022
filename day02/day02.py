moves = {"A": "R", "X": "R", "B": "P", "Y": "P", "C": "S", "Z": "S"}
points = {"R": 1, "P": 2, "S": 3}
outcomes = {"X": 1, "Y": 2, "Z": 0}


def rpc_result(opponent, player):
    o = points[opponent]
    p = points[player]
    result_score = ((((p - o) % 3) + 1) % 3) * 3
    move_score = p
    return result_score, move_score


total = 0
with open('input.txt') as input_data:
    for line in input_data.readlines():
        opp = moves[line[0]]
        plr = moves[line[2]]
        score = rpc_result(opp, plr)
        # print(opp, "-", plr, " : ", score)
        total += sum(score)

print("Part1: ", total)


def get_plr_move(opponent, outcome):
    o = points[opponent]
    p = (o + outcome) % 3
    return ["R", "P", "S"][p]


total = 0

with open('input.txt') as input_data:
    for line in input_data.readlines():
        opp = moves[line[0]]
        out = outcomes[line[2]]

        plr = get_plr_move(opp, out)
        print(opp, line[2], plr)
        score = rpc_result(opp, plr)
        total += sum(score)

print("Part2: ", total)
