data = "394618527"
test = "389125467"
array = [int(c) for c in test]
current = array[0]
for count in range(100):
    print(count + 1)
    i = array.index(current)
    print(array)
    print(f"current {current}")
    picked = []
    for _ in range(3):
        if (i + 1) < len(array):
            picked.append(array.pop(i + 1))
        else:
            picked.append(array.pop(0))
    next_current = array[0] if (i + 1) >= len(array) else array[i + 1]
    dest = current - 1
    while dest not in array:
        dest -= 1
        if dest < min(array):
            dest = max(array)
    dest_idx = array.index(dest)
    print(f"picked up {picked}")
    print(f"destination {dest}")
    array = array[0 : dest_idx + 1] + picked + array[dest_idx + 1:]
    current = next_current
print("final")
print(array)
idx_one = array.index(1)
print("".join(map(str, array[idx_one + 1 :] + array[:idx_one])))


test = "389125467"
array = [int(c) for c in test] + list(range(10, int(1e6) + 1))
current = array[0]
for count in range(10000000):
    if count % 100000 == 0:
        print(count)
    i = array.index(current)

    picked = []
    for _ in range(3):
        if (i + 1) < len(array):
            picked.append(array.pop(i + 1))
        else:
            picked.append(array.pop(0))
    dest = current - 1
    while dest not in array:
        dest -= 1
        if dest < min(array):
            dest = max(array)
    dest_idx = array.index(dest)
    if count > 9:
        array.append(count + 1)
    next_current = array[0] if (i + 1) >= len(array) else array[i + 1]
    array = array[0 : dest_idx + 1] + picked + array[dest_idx + 1:]
    current = next_current
idx_one = array.index(1)
print(array[idx_one : idx_one + 2])