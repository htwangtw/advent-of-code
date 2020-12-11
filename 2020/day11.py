from aoc.tools import read_input

path = "2020/data/day11.txt"

def parse_seat_map(data):
    # get coordinate
    seats = {(x, y): state for x, row in enumerate(data) for y, state in enumerate(row)}
    return seats

seat_map = parse_seat_map(read_input(path))

test_map = ["L.LL.LL.LL",
"LLLLLLL.LL",
"L.L.L..L..",
"LLLL.LL.LL",
"L.LL.LL.LL",
"L.LLLLL.LL",
"..L.L.....",
"LLLLLLLLLL",
"L.LLLLLL.L",
"L.LLLLL.LL"]

test_map = parse_seat_map(test_map)

def check_neighbour(location, seat_map, part2=False):
    state = seat_map[location]
    # check surroundings
    surroundings = [(-1, 1), (-1, 0), (-1, -1),
                    (0, 1), (0, -1),
                    (1, 1), (1, 0), (1, -1)]
    tiles = []
    for dx, dy in surroundings:
        n = (location[0] + dx, location[1] + dy)
        while part2 and n in seat_map and seat_map[n] == ".":
            n = (n[0] + dx, n[1] + dy)
        if n in seat_map:
            tiles.append(seat_map[n])

    lim = 4 if part2 else 3

    if state == "L" and "#" not in tiles:
        return "#"
    elif state == "#" and tiles.count("#") > lim:
        return "L"
    else:
        return state

def stablise(seat_map, part2=False):
    current_map = seat_map.copy()
    old_map = None
    while current_map != old_map:
        old_map = current_map.copy()
        for location, state in current_map.items():
            if state != ".":
                new_state = check_neighbour(location, old_map, part2)
                current_map[location] = new_state
    return list(current_map.values()).count("#")
print(stablise(test_map))
print(stablise(seat_map))


test_map = ["L.LL.LL.LL",
"LLLLLLL.LL",
"L.L.L..L..",
"LLLL.LL.LL",
"L.LL.LL.LL",
"L.LLLLL.LL",
"..L.L.....",
"LLLLLLLLLL",
"L.LLLLLL.L",
"L.LLLLL.LL",]
test_map = parse_seat_map(test_map)
print(stablise(test_map, True))
print(stablise(seat_map, True))
