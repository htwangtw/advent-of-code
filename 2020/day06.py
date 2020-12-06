from aoc.tools import read_input

def parse_doc(path):
    data = read_input(path)
    cur_entry = ""
    groups = []
    for l in data:
        if l == "":
            groups.append(cur_entry)
            cur_entry = ""
        else:
            cur_entry += l + " "
    groups.append(cur_entry) # last entry
    return groups

groups = parse_doc("2020/data/day06.txt")
print(sum(len(set(group)) - 1 for group in groups))  # remove space in the count

count = 0
for group in groups:
    items = group.split()
    common = None
    while len(items) > 0:
        i = set(items.pop())
        common = i if common is None else common.intersection(i)
    count += len(common)

print(count)