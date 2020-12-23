data = "394618527"
test = "389125467"
cups = [int(c) for c in test]
# current = cups[0]
# for count in range(10):
#     print(count + 1)
#     i = cups.index(current)
#     print(cups)
#     print(f"current {current}")
#     picked = []
#     for _ in range(3):
#         if (i + 1) < len(cups):
#             picked.append(cups.pop(i + 1))
#         else:
#             picked.append(cups.pop(0))
#     next_current = cups[0] if (i + 1) >= len(cups) else cups[i + 1]
#     dest = current - 1
#     while dest not in cups:
#         dest -= 1
#         if dest < min(cups):
#             dest = max(cups)
#     dest_idx = cups.index(dest)
#     print(f"picked up {picked}")
#     print(f"destination {dest}")
#     cups = cups[0 : dest_idx + 1] + picked + cups[dest_idx + 1:]
#     current = next_current
# print("final")
# print(cups)
# idx_one = cups.index(1)
# print("".join(map(str, cups[idx_one + 1 :] + cups[:idx_one])))


# hint from tom: linked list
cups = [int(c) for c in data] + list(range(10, int(1e6 + 1)))
next_cup_list = {current: next_cup for current, next_cup in zip(cups, cups[1:] + [cups[0]])}
n_max = len(cups)

current = cups[0]
for _ in range(int(1e7)):
    picked = [next_cup_list[current],
        next_cup_list[next_cup_list[current]],
        next_cup_list[next_cup_list[next_cup_list[current]]]]

    dest = current - 1 if current > 1 else n_max
    while dest in picked:
        if dest > 1:
            dest -= 1
        else:
            dest = n_max

    next_cup_list[current] = next_cup_list[picked[-1]]
    next_cup_list[picked[-1]] = next_cup_list[dest]
    next_cup_list[dest] = picked[0]
    current = next_cup_list[current]

# current = 1
# cup_state = []
# for _ in range(n_max - 1):
#     current = next_cup_list[current]
#     cup_state.append(current)
# print("".join(map(str, cup_state)))

result = next_cup_list[1] * next_cup_list[next_cup_list[1]]
print("Part 2:", result)