with open('input.txt') as input_data:
    signal = ""
    for line in input_data.readlines():
        signal += line


def get_marker(signal, n=4):
    for i in range(n, len(signal)):
        if len(set(signal[i-n:i])) == n:
            return i


print("Part1:", get_marker(signal, 4))

print("Part2:", get_marker(signal, 14))



