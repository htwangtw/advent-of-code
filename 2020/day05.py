from aoc.tools import read_input

path = "2020/data/day05.txt"

data = read_input(path)

all_seats = set()
for line in data:
    line = line.replace("F", "0").replace("B", "1")
    line = line.replace("L", "0").replace("R", "1")
    num = int(line, 2)
    all_seats.add(num)

print(max(all_seats))

print(set(range(min(all_seats), max(all_seats) + 1)) - all_seats)