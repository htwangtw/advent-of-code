from aoc.tools import read_input

path = "2020/data/day10.txt"
data = list(map(int ,read_input(path)))

test_1 = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
test_2 = [28,
33,
18,
42,
31,
14,
46,
20,
48,
47,
24,
23,
49,
45,
19,
38,
39,
11,
1,
32,
25,
35,
8,
17,
7,
9,
4,
2,
34,
10,
3]

def sort_adapters(input):
    data = input.copy()
    max_jol = max(input) + 3
    connected = [0]
    start = 0
    while max(input) in data:
        options = [i + start for i in range(1, 4) if i + start in data]
        cur_adapter = options[0] if len(options) == 1 else min(options)
        data.remove(cur_adapter)
        connected.append(cur_adapter)
        start = cur_adapter
    assert max_jol - 3 <= connected[-1] <= max_jol
    connected.append(max_jol)
    return connected

def count_diff(data, n):
    diff = [abs(data[i] - data[i + 1]) for i in range(len(data) - 1)]
    return diff.count(n)


# t1 = sort_adapters(test_1)
# print(count_diff(t1, 1))
# print(count_diff(t1, 3))

# t2 = sort_adapters(test_2)
# print(count_diff(t2, 1))
# print(count_diff(t2, 3))

connected = sort_adapters(data)
print(count_diff(connected, 1) * count_diff(connected, 3))


# part 1 alt
data = list(map(int ,read_input(path)))
data.append(0)
data.append(3 + max(data))
data.sort()
diff = [j - i for i, j in zip(data[:-1], data[1:])]
print(diff.count(1) * diff.count(3))


# reading part two make me realise
# it's a graph

data = list(map(int ,read_input(path)))
data.append(0)
data.append(3 + max(data))
data.sort()

adapter_map = {n: 0 for n in data}
adapter_map[0] = 1

# walk through the map
for node, gone_pass in adapter_map.items():
    for i in range(1, 4):
        if node + i in adapter_map:
            adapter_map[node + i] += gone_pass

print(f"part 2:{adapter_map[max(data)]}")

# directed graph solution found on reddit
# adjacencies = [[0 for x in range(len(data))] for y in range(len(data))]
# for i in range(len(data)):
#     for j in range(i+1, len(data)):
#         if data[j] <= data[i] + 3:
#             adjacencies[i][j] = 1

# adj = np.array(adjacencies)
# curr = adj
# total = 0
# for d in data:
#     curr = np.matmul(curr, adj)
#     total += curr[0][-1]

# print(total)