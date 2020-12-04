import re

from aoc.tools import read_input


def parse_doc(path):
    data = read_input(path)
    cur_entry = ""
    people = []
    for l in data:
        if l == "":
            doc = {item.split(":")[0]: item.split(":")[1] for item in cur_entry.split()}
            people.append(doc)
            cur_entry = ""
        else:
            cur_entry += l + " "
    doc = {item.split(":")[0]: item.split(":")[1] for item in cur_entry.split()}
    people.append(doc) # last entry
    return people


path = "2020/data/day04.txt"
fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"}
people = parse_doc(path)

def validator(person, fields):
    info = set(person.keys())
    return fields - info == {"cid"} or len(fields - info) == 0

valid = sum(int(validator(person, fields)) for person in people)
print(valid)

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
#     If cm, the number must be at least 150 and at most 193.
#     If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.

def check_range(input, min, max):
    return int(min <= input <= max)

def check_text(input, pattern):
    return int(re.match(pattern, input) is not None)

patterns = {
    "byr": (1920, 2002),
    "iyr": (2010, 2020),
    "eyr": (2020, 2030),
    "hgt": {"cm":(150, 193), "in":(59, 76)},
    "hcl": r"^#[0-9a-f]{6}$",
    "ecl": r"^amb$|^blu$|^brn$|^gry$|^grn$|^hzl$|^oth$",
    "pid": r"^[0-9]{9}$",
    "cid": None
}

valid = 0
for person in people:
    if validator(person, fields) == True:
        count = 0
        for key, item in person.items():
            if type(patterns[key]) is tuple:
                count += check_range(int(item), patterns[key][0], patterns[key][1])
            elif type(patterns[key]) is str:
                count += check_text(item, patterns[key])
            elif check_text(item, r"^[0-9]*cm$|^[0-9]*in$"):
                count += check_range(int(item[:-2]),
                                    patterns[key][item[-2:]][0],
                                    patterns[key][item[-2:]][1])

        if count == 7:
            valid += 1

print(valid)
