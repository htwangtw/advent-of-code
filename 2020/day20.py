from itertools import product
from math import prod


with open("2020/data/day20.txt", "r") as f:
    data = f.read().split("\n\n")

test = """
Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...
""".split("\n\n")

def parse_tiles(data):
    tiles = {}
    for tile in data:
        tile = tile.split()
        key = int(tile[1].split(":")[0])
        tiles[key] = tile[2:]
    return tiles


def flip_tile(tile):
    # original, vertical flip, mirror, mirror verticle flip
    return [tile, tile[::-1],
            [l[::-1] for l in tile],
            [l[::-1] for l in tile][::-1]]

def get_border(tile):
    # get boarder clockwise
    return (
        tile[0],
        "".join(l[-1] for l in tile),
        tile[-1],
        "".join(l[0] for l in tile)
    )

def break_tile(tile):
    return [[a for a in l] for l in tile]

def rotate_tile(tile):
    # top left as the corner, rotate clockwise
    last  = tile
    rotate = [["".join(l) for l in tile]]
    for _ in range(3):
        tile = [l[:] for l in tile]
        for x in range(len(tile)):
            for y in range(len(tile[x])):
                tile[x][y] = last[len(tile[x])-y-1][x]
        last = tile
        rotate.append(["".join(l) for l in tile])
    return rotate


# part 1
tiles = parse_tiles(data)

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
connected = {}
for a, b in product(boarders.keys(), repeat=2):
    if a != b:
        connections = boarders[a].intersection(boarders[b])
        if len(connections) > 0:
            if a in connected:
                connected[a].append(b)
            else:
                connected[a] = [b]

# there should be 4 tiles with 2 connections only
print("part 1:")
print(prod(key for key, c in connected.items() if len(c) == 2))

