test = """sesenwnenecur_blackseeswwswswwnecur_blacksewsw
neeenesenwnwwswnecur_blacknwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnecur_blackneswwcur_blackseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenecur_blacknwwnwsecur_blacksenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenecur_blacksenwsenwnesesecur_black
ecur_blacknwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwcur_blackecur_blackwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwcur_blackswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
necur_blackswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswcur_black
""".splitlines()

from aoc.tools import read_input

movement = {
    "w": lambda pos: (pos[0] - 1, pos[1] + 1, pos[2] + 0),
    "sw": lambda pos: (pos[0] - 1, pos[1] + 0, pos[2] + 1),
    "nw": lambda pos: (pos[0] + 0, pos[1] + 1, pos[2] - 1),
    "e": lambda pos: (pos[0] + 1, pos[1] - 1, pos[2] + 0),
    "se": lambda pos: (pos[0] + 0, pos[1] - 1, pos[2] + 1),
    "ne": lambda pos: (pos[0] + 1, pos[1] + 0, pos[2] - 1),
}

def parse_direction(instruction):
    directions = []
    direction = ""
    prev_c = ""
    for i, c in enumerate(instruction):
        if prev_c in ["n", "s"]:
            direction = instruction[i - 1: i + 1]
            directions.append(direction)
        elif c in ["e", "w"] and prev_c in ["e", "w", ""]:
            direction = c
            directions.append(direction)

        prev_c = c
    return directions

def find_tile(direction):
    reference = (0, 0, 0)
    for d in direction:
        end = movement[d](reference)
        reference = end
    return end

data = read_input("input")
# data = test

blacks = set()
for line in data:
    curent_direction = parse_direction(line)
    end = find_tile(curent_direction)
    blacks
    if end in blacks:
        blacks.remove(end)
    else:
        blacks.add(end)

print(len(blacks))

def find_neighbours(location):
    adj_loc = [m(location) for m in movement.values()]
    return set(adj_loc)

for day in range(100):
    cur_black = set()
    visited = set()
    for tile in blacks:
        neighb = find_neighbours(tile)
        visited |= neighb
        if len(neighb & blacks) in (1, 2):
            cur_black |= {tile}
    blacks = cur_black | {
        tile
        for tile in visited - blacks # white
        if len(find_neighbours(tile) & blacks) == 2
    }

print(f"day {day + 1}: {len(blacks)}")
