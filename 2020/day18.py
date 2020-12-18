from aoc.tools import read_input
import re

data = read_input("2020/data/day18.txt")

# when encounter "-" do multiplication
class op:
    def __init__(self, v):
        self.v = v
    def __add__(self, other):
        return op(self.v + other.v)
    def __sub__(self, other):
        return op(self.v * other.v)

t = 0
for line in data:
    line = line.replace("*", "-")
    for d in range(10):line = line.replace(f"{d}", f"op({d})")
    t += eval(line, {"op": op}).v
print(t)


# same logic for part two
class op:
    def __init__(self, v):
        self.v = v
    def __add__(self, other):
        return op(self.v + other.v)
    def __sub__(self, other):
        return op(self.v * other.v)
    def __mul__(self, other):
        return op(self.v + other.v)

t = 0
for line in data:
    print(line)
    line = line.replace("*", "-")
    line = line.replace("+", "*")
    print(line)
    for d in range(10):line = line.replace(f"{d}", f"op({d})")
    t += eval(line, {"op": op}).v
print(t)
