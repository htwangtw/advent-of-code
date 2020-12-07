from aoc.tools import read_input
import re


def parse_rules(path):
    data = read_input(path)
    rules = {}
    for rule in data:
        key = re.search("^([a-z\ ]*) bags contain", rule).group(1)
        contents = re.findall("([0-9]) ([a-z\ ]*) bag", rule)
        if len(contents) == 0:
            rules[key] = None
        else:
            rules[key] = {c[1]: int(c[0]) for c in contents}

    return rules

rules = parse_rules("2020/data/day07.txt")
target = "shiny gold"

def outer_bag(target):
    bags_to_find = {target}
    found_bags = set()
    while bags_to_find:
        find = bags_to_find.pop()
        bags = [
            key
            for key, content in rules.items()
            if content and find in content.keys()
        ]
        bags_to_find.update(bags)
        found_bags.update(bags)
    return len(found_bags)

print(outer_bag(target))

def innner_bags(color):
    contain = rules[color]
    if contain is None:
        return 0
    else:
        return sum(contain[key] * innner_bags(key) + contain[key] for key in contain.keys())

print(innner_bags(target))