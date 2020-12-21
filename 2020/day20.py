from itertools import product
from math import prod


with open("2020/data/day20.txt", "r") as f:
    data = f.read().split("\n\n")

def parse_tiles(data):
    tiles = {}
    for tile in data:
        tile = tile.split()
        key = int(tile[1].split(":")[0])
        tiles[key] = tile[2:]
    return tiles

def get_border(tile):
    # get boarder clockwise from top
    return (
        tile[0],
        "".join(l[-1] for l in tile),
        tile[-1],
        "".join(l[0] for l in tile)
    )

def break_tile(tile):
    return [[a for a in l] for l in tile]

# part 1
tiles = parse_tiles(data)

# all possible boarder
boarders = {}
for key, tile in tiles.items():
    # get boarders
    flipped = flip_tile(tile)
    bds = set()
    for f in flipped:
        bd = get_border(f)
        bds.update(bd)
    boarders[key] = bds

# find connected tiles
connections = {}
for a, b in product(boarders.keys(), repeat=2):
    if a != b:
        common = boarders[a].intersection(boarders[b])
        if len(common) > 0:
            if a in connections:
                connections[a].append(b)
            else:
                connections[a] = [b]

# there should be 4 tiles with 2 connections only
print("part 1:")
print(prod(key for key, c in connections.items() if len(c) == 2))

# part 2
def rotate_tile(tile):
    # top left as the corner, rotate 90 degrees cloack wise
    last  = tile
    tile = [l[:] for l in tile]
    for x in range(len(tile)):
        for y in range(len(tile[x])):
            tile[x][y] = last[len(tile[x]) - y - 1][x]
    last = tile
    return ["".join(l) for l in tile]

def mirror_x(a):
    # mirror tile bottom to top
    return a[::-1]

def mirror_y(a):
    # mirror tile left to right
    return [l[::-1] for l in a]

# can start -> end achive walking in the edge length only
def walk_edge(start_tile, sides, path=[]):
    if len(path) == 0:
        path = [start_tile]

    buffer = sides.copy()
    buffer.pop(start_tile)
    ct = corners.copy()
    ct.remove(path[0])

    if not buffer:
        return path
    candidates = [t for t in connections[start_tile] if t in list(buffer.keys())]
    path.append(candidates[0])
    return walk_edge(path[-1], buffer, path)

def fill_edge(edge, tile_map={}):
    for i, t in enumerate(edge):
        base = int(i / (grid_size[0] - 1))
        if base % 2 == 0:
            x = (grid_size[0] - 1) * int(base / 2)
            y = -(grid_size[0] - 1) * int(base / 2)
            if i < grid_size[0]:
                x += i % (grid_size[0] - 1)
            else:
                x -= i % (grid_size[0] - 1)
        else:
            x = (grid_size[0] - 1) * (1 - int(base / 2))
            y = -(grid_size[0] - 1) * int(base / 2)
            if i < (grid_size[0]*2 -2):
                y -= i % (grid_size[0] - 1)
            else:
                y += i % (grid_size[0] - 1)
        tile_map[(abs(x), abs(y))] = t
    return tile_map

def remove_boarder(tile):
    return [l[1:-1]for l in tile[1:-1]]

def fill_map(start, tile_map, middle):
    if not middle:
        return tile_map
    else:
        remaining = middle.copy()
        bl = tile_map[start]
        br = tile_map[(start[0] + 1, start[1])]
        tl = tile_map[(start[0], start[1] +1)]
        target = (start[0] + 1, start[1] + 1)
        if not tile_map.get(target, False):
            br = set(connections[br])
            tl = set(connections[tl])
            coord = br.intersection(tl)
            coord.discard(bl)
            tile_map[target] = coord.pop()
            remaining.remove(tile_map[target])
            start = (start[0], start[1] + 1) # new start
        else:
            # reach the top
            start = (start[0] + 1, 0)
        return fill_map(start, tile_map, remaining)

n_connection = [len(v) for v in connections.values()]
print(f"centre tiles: {n_connection.count(4)}")
print(f"edge tiles: {n_connection.count(3)}")
print(f"solve: x**2 - {n_connection.count(3) / 2} = {n_connection.count(4)}")
print(f"solve: y = {n_connection.count(3) / 2} - x")

# I don't know how to solve this in python but I can do it by hand:
grid_size = (12, 12)

# get all the side tiles
sides = {k: i for k, i in connections.items() if len(i) <= 3}
corners = [k for k, i in connections.items() if len(i) == 2]
middle = [k for k, i in connections.items() if len(i) == 4]
edges = walk_edge(corners[0], sides)
tile_no_map = fill_edge(edges, tile_map={})
tile_no_map = fill_map((0, 0), tile_no_map, middle)

# find the tile pattern that joins together
# calibrate one corner (0,0) (three tiles)
centre = tiles[tile_no_map[(0, 0)]]
down = tiles[tile_no_map[(0, 1)]]
right = tiles[tile_no_map[(1, 0)]]

a = boarders[tile_no_map[(0, 0)]].intersection(boarders[tile_no_map[(1, 0)]])
b = boarders[tile_no_map[(0, 0)]].intersection(boarders[tile_no_map[(0, 1)]])

while get_border(centre)[2] not in b:
    centre = rotate_tile(break_tile(centre))

if get_border(centre)[1] not in a:
    centre = mirror_y(centre)

while get_border(right)[-1] not in a:
    right = rotate_tile(break_tile(right))

if get_border(right)[-1] != get_border(centre)[1]:
    right = mirror_x(right)

while get_border(down)[0] not in b:
    down = rotate_tile(break_tile(down))

if get_border(down)[0] != get_border(centre)[2]:
    down = mirror_y(down)

tiles[tile_no_map[(0, 0)]] = centre
tiles[tile_no_map[(0, 1)]] = down
tiles[tile_no_map[(1, 0)]] = right

# fill the map
tile_map = {}
prev = None
prev_coord = None
for coord, num in sorted(tile_no_map.items()):
    current = tiles[num]
    x, y = coord
    if not prev:
        prev = current
        prev_coord = coord
    elif x == 0: # use bottum of the previsous as ref
        target = get_border(prev)[2]
        while get_border(current)[0] not in [target, target[::-1]]:
            current = rotate_tile(break_tile(current))
        if get_border(current)[0] == target[::-1]:
            current = mirror_y(current)
        prev = current
        prev_coord = (x, y)
    else:  # use left as ref
        prev_coord = (x - 1, y)
        prev = tiles[tile_no_map[prev_coord]]
        target = get_border(prev)[1]
        while get_border(current)[-1] not in [target, target[::-1]]:
            current = rotate_tile(break_tile(current))
        if get_border(current)[-1] == target[::-1]:
            current = mirror_x(current)
    tiles[num] = current
    tile_map[coord] = current

for y in range(grid_size[0]):
    cur_row = [""] * (len(tile) - 2)
    for x in range(grid_size[0]):
        for i, l in enumerate(remove_boarder(tile_map[(x, y)])):
            cur_row[i] = cur_row[i] + l
    if y == 0:
        full_map = cur_row
    else:
        full_map += cur_row


def parse_map(full_map):
    tmp = break_tile(full_map)
    full_map = break_tile(full_map)
    for x in range(len(tmp)):
        for y in range(len(tmp)):
            full_map[y][x] = int(full_map[y][x]=="#")
    return full_map

monster = """
                  # \n
#    ##    ##    ###\n
 #  #  #  #  #  #   \n"""

def element_mul(a, b):
    for i in range(len(a)):
        for j in range(len(a[0])):
            a[i][j] *= b[i][j]
    return a

# get all possible maps
def all_the_maps(full_map):
    all_maps = [full_map]
    for _ in range(3):
        last = rotate_tile(break_tile(all_maps[-1]))
        all_maps.append(last)

    flipped_maps = []
    for m in all_maps:
        flipped_maps.append(mirror_x(m))
        flipped_maps.append(mirror_y(m))
    return all_maps + flipped_maps

bin_monster = [[int(i == "#") for i in l] for l in break_tile(monster.split("\n")) if l]

all_maps = all_the_maps(full_map)

for m in all_maps:
    n_monster = 0
    bin_map = parse_map(m)
    for y in range(len(bin_map) - len(bin_monster) + 1):
        y_end = y + len(bin_monster)
        for x in range(len(bin_map) - len(bin_monster[0]) + 1):
            x_end = x + len(bin_monster[0])
            current_range = [l[x:x_end] for l in bin_map[y : y_end]]
            look = element_mul(current_range, bin_monster)
            if look == bin_monster:
                n_monster += 1
    if n_monster != 0:
        break

print("part: 2")
print(sum(sum(l) for l in bin_map) - sum(sum(l) for l in bin_monster) * n_monster)