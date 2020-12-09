from aoc.tools import read_input
from itertools import combinations


path = "2020/data/day09.txt"
data = list(map(int ,read_input(path)))

preamble = 25

def check_sum(target, search_range):
    all_combos = list(combinations(search_range, 2))
    while all_combos:
        a, b = all_combos.pop()
        if target == a + b:
            return True
    return False

def find_rule_breaker(data, preamble):
    fit_the_rule = True
    i = 0
    while fit_the_rule:
        target = data[preamble + i]
        search_range = data[i : i + preamble]
        i += 1
        fit_the_rule = check_sum(target, search_range)
    return target

rule_breaker = find_rule_breaker(data, preamble)
print(rule_breaker)

window_size = 2
i = 0
answer = None
while not answer:
    # when reach the end of list with current window
    if i + window_size > len(data):
        window_size += 1
        i = 0
    cur_window = data[i : i + window_size]
    if sum(cur_window) == rule_breaker:
        answer = sum((min(cur_window), max(cur_window)))
        break
    i += 1
print(answer)