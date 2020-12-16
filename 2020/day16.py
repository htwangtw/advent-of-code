from aoc.tools import read_input
import re

data = read_input("2020/data/day16.txt")
def get_ticket(data):
    info = {}
    tickets = {}
    for line in data:
        arr_dep = re.search("(^[a-z ]*): (\d*)-(\d*) or (\d*)-(\d*)",
                            line)
        if arr_dep is not None:
            label = arr_dep.group(1)
            info[label] = list(range(int(arr_dep.group(2)),
                                     int(arr_dep.group(3)) + 1))+\
                          list(range(int(arr_dep.group(4)),
                                     int(arr_dep.group(5)) + 1))
        elif "ticket" in line:
            label = line.split(":")[0]
            tickets[label] = []
        elif line != "":
            tickets[label].append(list(map(int, line.split(","))))
    return info, tickets


test_data = ["class: 1-3 or 5-7",
"row: 6-11 or 33-44",
"seat: 13-40 or 45-50",
"",
"your ticket:",
"7,1,14",
"",
"nearby tickets:",
"7,3,47",
"40,4,50",
"55,2,20",
"38,6,12"]

def part_1(data):
    choochoo, tickets = get_ticket(data)

    check_range = []
    for values in choochoo.values():
        check_range += values

    return sum(
        n for nt in tickets["nearby tickets"] for n in nt if n not in check_range)

print(part_1(data))


# parse data for part 2
def remove_bad(data):
    info, tickets = get_ticket(data)

    check_range = []
    for values in info.values():
        check_range += values

    keep_list = [
        nt
        for idx, nt in enumerate(tickets["nearby tickets"])
            if sum(1 for n in nt if n not in check_range) ==0
    ]
    tickets["nearby tickets"] = keep_list
    return info, tickets

def get_fitted_col(info, tickets):
    possible_list = {}
    for key, values in choochoo.items():
        check_col = {}
        for i in range(len(tickets["your ticket"][0])):
            cur_col = [nt[i] in values for nt in tickets["nearby tickets"]]
            check_col[i] = cur_col
        possible_list[key] = {col
            for col, check in check_col.items()
            if all(check) == True}
    return possible_list

def sort_list(remain, results=dict()):
    possible_list = remain.copy()

    if len(results) > 0 and len(results)!=20:
        found = set(results.values())
        for key in possible_list.keys():
            possible_list[key] = possible_list[key].difference(found)

    if len(possible_list) == 1:
        key, idx = possible_list.popitem()
        results[key] = list(idx)[0]
        return results

    shortest = len(possible_list)
    name = None
    for key, items in possible_list.items():
        if len(items) < shortest and len(items) > 0:
            shortest = len(items)
            name = key
    results[name] = list(possible_list[name])[0]
    possible_list.pop(name)
    return sort_list(possible_list, results)


test_data = ["class: 0-1 or 4-19",
"row: 0-5 or 8-19",
"seat: 0-13 or 16-19",
"",
"your ticket:",
"11,12,13",
"",
"nearby tickets:",
"3,9,18",
"15,1,5",
"5,14,9"]
# choochoo, tickets = get_ticket(test_data)
choochoo, tickets = remove_bad(data)
remain = get_fitted_col(choochoo, tickets)
results = sort_list(remain)

ans = 1
for key, item in results.items():
    if "depart" in key:
        ans *= tickets["your ticket"][0][item]
print(ans)