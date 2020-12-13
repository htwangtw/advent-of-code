from aoc.tools import read_input

path = "2020/data/day12.txt"

def parse_instructions(path):
    # get coordinate
    data = read_input(path)
    return [(row[0], int(row[1:])) for row in data]

instr = parse_instructions(path)

# instr = [("F", 10),
# ("N", 3), ("F", 7),
# ("R", 90),
# ("F", 11)
# ]

delta_x = {"N": 0, "S": 0, "E": 1, "W": -1}
delta_y = {"N": 1, "S": -1, "E": 0, "W": 0}
angle_to_direction = {0: "E", 90: "S", 180: "W", 270: "N"}
x, y = 0, 0
angle = 0
for direction, unit in instr:
    if direction == "F":
        cur_dir = angle_to_direction[angle]
        x += unit * delta_x[cur_dir]
        y += unit * delta_y[cur_dir]
    elif direction == "L":
        angle = (angle - unit) % 360
    elif direction == "R":
        angle = (angle + unit) % 360
    else:
        x += unit * delta_x[direction]
        y += unit * delta_y[direction]

print(abs(x) + abs(y))

way_point= [10, 1]
ship = [0, 0]
for direction, unit in instr:
    if direction == "F":
        ship[0] += way_point[0] * unit
        ship[1] += way_point[1] * unit
    elif direction == "L":
        turning = {90: [-way_point[1], way_point[0]],
                   180: [-way_point[0], -way_point[1]],
                   270: [way_point[1], -way_point[0]]}
        way_point = turning[unit]
    elif direction == "R":
        turning = {90: [way_point[1], -way_point[0]],
                   180: [-way_point[0], -way_point[1]],
                   270: [-way_point[1], way_point[0]]}
        way_point = turning[unit]
    else:
        way_point[0] += unit * delta_x[direction]
        way_point[1] += unit * delta_y[direction]

print(abs(ship[0]) + abs(ship[1]))