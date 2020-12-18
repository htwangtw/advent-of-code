from aoc.tools import read_input
from itertools import product

data = read_input("2020/data/day17.txt")

test = [".#.",
"..#",
"###"]

def get_map(data, ndim):
    light_map = {}
    for y, line in enumerate(data):
        for x, cell in enumerate(line):
            coord = (x, y) + (0, ) * (ndim - 2)
            light_map[coord] = int(cell == "#")
    return light_map

def check_state(state, total_on):
    if (state == 1 and total_on in [2, 3]) \
       or (state == 0 and total_on == 3):
        return 1
    else:
        return 0

def get_current_range(light_map, idx):
    lower = min(k[idx] for k in light_map.keys()) - 1
    upper = max(k[idx] for k in light_map.keys()) + 2
    return (lower, upper)

def get_neighbour(coord, light_map):
    total = 0
    neighbour_range = [-1, 0, 1]
    for delta in product(neighbour_range, repeat=len(coord)):
        check = tuple(map(sum, zip(coord, delta)))
        if sum(int(d == 0) for d in delta) == len(coord):
            continue
        elif light_map.get(check, False):
            total += 1
    return total

def walk_grid(light_map, ndim):
    current = {}
    xl, xu = get_current_range(light_map, 0)
    yl, yu = get_current_range(light_map, 1)
    zl, zu = get_current_range(light_map, 2)
    for x in range(xl, xu):
        for y in range(yl, yu):
            for z in range(zl, zu):
                state = light_map.get((x, y, z), 0)
                total_on = get_neighbour((x, y, z), light_map)
                current[(x, y, z)] = check_state(state, total_on)
    return current

def run_light(data, ndim, walk_grid):
    data = get_map(data, ndim)
    for _ in range(6):
        data = walk_grid(data, ndim)
    return sum(data.values())


def walk_4dgrid(light_map, ndim):
    current = {}
    xl, xu = get_current_range(light_map, 0)
    yl, yu = get_current_range(light_map, 1)
    zl, zu = get_current_range(light_map, 2)
    wl, wu = get_current_range(light_map, 3)
    for x in range(xl, xu):
        for y in range(yl, yu):
            for z in range(zl, zu):
                for w in range(wl, wu):
                    state = light_map.get((x, y, z, w), 0)
                    total_on = get_neighbour((x, y, z, w), light_map)
                    current[(x, y, z,w )] = check_state(state, total_on)
    return current

assert run_light(test, 3, walk_grid) == 112
print(run_light(data, 3, walk_grid))
print(run_light(data, 4, walk_4dgrid))