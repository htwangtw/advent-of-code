def read_input(path):
    with open(path, "r") as f:
        data = [l for l in f.read().splitlines()]
    return data

def ski(right, down):
    x, y = 0, 0
    width, length = len(forrest_pattern[0]), len(forrest_pattern)
    route = []
    while y < length:
        block = forrest_pattern[y][x]
        route.append(block)

        x += right
        y += down
        if x >= width: # extend map in x direction
            x -= width
    return route.count("#")

forrest_pattern = read_input("2020/data/day03.txt")

print(ski(3, 1))

print(ski(1, 1) * \
      ski(3, 1) * \
      ski(5, 1) * \
      ski(7, 1) * \
      ski(1, 2))