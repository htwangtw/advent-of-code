def read_input(path):
    with open(path, "r") as f:
        data = [l for l in f.read().splitlines()]
    return data